#!/usr/bin/env python3
"""
GDUT 大学物理实验报告标准作图脚本 (GDUT Physics Experiment Plotting Script)

功能：
1. 绘制符合大学物理实验报告要求的作图法图表（黑白打印风格、内向坐标刻度、主次网格、最佳拟合线、拟合方程、实验信息框）。
2. 支持跨平台（macOS / Linux / Windows）自适应中文无乱码渲染。
3. 同时输出高分辨率 PNG (300 DPI) 与矢量 PDF。
4. 可作为模块导入使用，也可直接通过命令行或调整数据独立运行。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties, findfont
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


def get_chinese_font() -> FontProperties:
    """
    自适应查找系统可用的中文字体，确保在不同 OS 下中文正常显示且不出现方块或告警。
    """
    candidates = [
        # macOS
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        # Windows
        "C:\\Windows\\Fonts\\simhei.ttf",
        "C:\\Windows\\Fonts\\msyh.ttc",
        "C:\\Windows\\Fonts\\simsun.ttc",
        # Linux / Unix
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
    ]

    for path_str in candidates:
        candidate_path = Path(path_str)
        if candidate_path.exists():
            return FontProperties(fname=str(candidate_path))

    # 尝试根据字体族名称查找
    for family in ["PingFang SC", "Heiti SC", "Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "WenQuanYi Micro Hei"]:
        try:
            font_file = findfont(family, fallback_to_default=False)
            if font_file and Path(font_file).exists():
                return FontProperties(fname=font_file)
        except Exception:
            continue

    return FontProperties()


def plot_lab_chart(
    x_data: Sequence[float],
    y_data: Sequence[float],
    title: str,
    x_label: str,
    y_label: str,
    slope: float | None = None,
    intercept: float | None = None,
    fit_equation: str | None = None,
    experiment_info: Sequence[str] | None = None,
    output_dir: Path | str = "./outputs",
    filename_prefix: str = "lab_plot",
    x_major_step: float | None = None,
    y_major_step: float | None = None,
) -> Tuple[Path, Path]:
    """
    绘制并保存符合大学物理实验规范的标准图表。
    """
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    font = get_chinese_font()
    x = np.array(x_data, dtype=float)
    y = np.array(y_data, dtype=float)

    # 线性拟合
    if slope is None or intercept is None:
        poly = np.polyfit(x, y, deg=1)
        slope = float(poly[0])
        intercept = float(poly[1])

    if fit_equation is None:
        sign = "+" if intercept >= 0 else "-"
        fit_equation = f"y = {slope:.3g}x {sign} {abs(intercept):.3g}"

    x_min, x_max = float(np.min(x)), float(np.max(x))
    x_span = x_max - x_min if x_max != x_min else 1.0
    x_plot_min = x_min - 0.05 * x_span
    x_plot_max = x_max + 0.05 * x_span

    x_fit = np.linspace(x_plot_min, x_plot_max, 200)
    y_fit = slope * x_fit + intercept

    # 配置 matplotlib 样式，适合黑白报告打印
    plt.rcParams.update(
        {
            "figure.dpi": 160,
            "axes.unicode_minus": False,
            "axes.edgecolor": "black",
            "axes.linewidth": 1.1,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.major.size": 5,
            "ytick.major.size": 5,
            "xtick.minor.size": 3,
            "ytick.minor.size": 3,
        }
    )

    fig, ax = plt.subplots(figsize=(8.4, 6.0), constrained_layout=True)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # 最佳拟合线
    ax.plot(
        x_fit,
        y_fit,
        color="0.35",
        linewidth=1.9,
        linestyle="-",
        label="最佳拟合直线",
        zorder=2,
    )

    # 实验数据点
    ax.scatter(
        x,
        y,
        s=42,
        marker="o",
        facecolor="black",
        edgecolor="black",
        linewidth=0.8,
        label="实验数据",
        zorder=3,
    )

    # 坐标范围与步长
    ax.set_xlim(x_plot_min, x_plot_max)
    y_min_val = min(float(np.min(y)), float(np.min(y_fit)))
    y_max_val = max(float(np.max(y)), float(np.max(y_fit)))
    y_span = y_max_val - y_min_val if y_max_val != y_min_val else 1.0
    ax.set_ylim(y_min_val - 0.08 * y_span, y_max_val + 0.12 * y_span)

    if x_major_step:
        ax.xaxis.set_major_locator(MultipleLocator(x_major_step))
        ax.xaxis.set_minor_locator(MultipleLocator(x_major_step / 2))
    else:
        ax.xaxis.set_minor_locator(AutoMinorLocator(2))

    if y_major_step:
        ax.yaxis.set_major_locator(MultipleLocator(y_major_step))
        ax.yaxis.set_minor_locator(MultipleLocator(y_major_step / 2))
    else:
        ax.yaxis.set_minor_locator(AutoMinorLocator(2))

    # 网格线：主网格与次网格
    ax.grid(which="major", color="0.72", linewidth=0.65)
    ax.grid(which="minor", color="0.88", linewidth=0.45)
    ax.set_axisbelow(True)

    # 图名与坐标轴标题
    ax.set_title(title, fontproperties=font, fontsize=16, pad=16)
    ax.set_xlabel(x_label, fontproperties=font, fontsize=12.5)
    ax.set_ylabel(y_label, fontproperties=font, fontsize=12.5)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(10.5)

    # 拟合方程文字框
    ax.text(
        0.65,
        0.18,
        fit_equation,
        transform=ax.transAxes,
        fontsize=12.5,
        bbox={
            "boxstyle": "square,pad=0.3",
            "facecolor": "white",
            "edgecolor": "none",
            "alpha": 0.92,
        },
    )

    # 实验信息黑色方框
    if experiment_info:
        info_text = "\n".join(experiment_info)
        ax.text(
            0.04,
            0.96,
            info_text,
            transform=ax.transAxes,
            fontproperties=font,
            fontsize=10.5,
            va="top",
            ha="left",
            linespacing=1.45,
            bbox={
                "boxstyle": "square,pad=0.45",
                "facecolor": "white",
                "edgecolor": "black",
                "linewidth": 1.1,
            },
        )

    for spine in ax.spines.values():
        spine.set_color("black")
        spine.set_linewidth(1.1)

    png_path = out_dir / f"{filename_prefix}.png"
    pdf_path = out_dir / f"{filename_prefix}.pdf"

    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    plt.close(fig)

    return png_path, pdf_path


def main() -> int:
    parser = argparse.ArgumentParser(description="大学物理实验报告标准作图工具")
    parser.add_argument("--demo", action="store_true", help="运行金属丝弹性模量示例作图")
    parser.add_argument("--output-dir", default="./outputs", help="输出文件夹路径")
    args = parser.parse_args()

    # 默认执行或演示示例：拉伸法测量弹性模量 F-x 关系
    demo_data = [
        (2.503, 0.0),
        (2.798, 9.8),
        (3.098, 19.6),
        (3.390, 29.4),
        (3.690, 39.2),
        (3.985, 49.0),
        (4.293, 58.8),
        (4.598, 68.6),
    ]
    x_vals = [d[0] for d in demo_data]
    y_vals = [d[1] for d in demo_data]

    info = [
        "实验名称：用拉伸法测量弹性模量",
        "学院：物理与光电工程学院",
        "班级：应用物理学1班",
        "姓名：张三",
        "日期：2026/06/01",
    ]

    png, pdf = plot_lab_chart(
        x_data=x_vals,
        y_data=y_vals,
        title="F-x关系图（用作图法测金属丝弹性模量）",
        x_label="Δx / cm",
        y_label="F / N",
        slope=32.79,
        intercept=-81.92,
        fit_equation=r"$F = 32.79x - 81.92$",
        experiment_info=info,
        output_dir=args.output_dir,
        filename_prefix="F-x关系图_金属丝弹性模量",
        x_major_step=0.20,
        y_major_step=10.0,
    )

    print(f"图表已成功生成：\n  PNG: {png}\n  PDF: {pdf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
