---
name: gdut-physics-experiment-data-processing
description: "Use when preparing Guangdong University of Technology (GDUT) physics experiment reports, including preview sections, data calculation, uncertainty evaluation, significant figures, result tables, experiment summaries, and generating matplotlib lab-report plots."
metadata:
  short-description: "GDUT 大学物理实验预习、数据处理与作图助手"
---

# GDUT University Physics Experiment Data Processing

Use this skill when the user asks to prepare a GDUT university physics experiment report, complete experiment preview content, process experiment data, standardize significant figures, express uncertainty, fill experiment tables, write an experiment summary, generate a plotting prompt, or make a matplotlib-style lab-report chart prompt.

## Workflow

1. **Check for Uploaded Images**: Check if the user has uploaded images of the corresponding experiment parts from "University Physics Experiment" (《大学物理实验》课本) and "University Physics Experiment Report" (《大学物理实验报告》). If this is the first interaction and the user has not uploaded them, politely inform and request the user to upload these images first to ensure accuracy of the formulas, instrument precision, and data tables.
2. **Classify the Task**: Classify the task as experiment preview, data measurement organization, data processing, experiment summary, plot generation / prompt, or a mixed task.
3. **Complete Report Sections**: Complete the experiment preview, data processing, and experiment summary sections. Do not invent measurement data; use only the user's materials and original data for the data measurement section.
4. **Table Data**: For table data, give the completed table directly unless the user asks for detailed derivations.
5. **Calculations**: For non-table calculations, write the formula-based solving process and final result with correct units, significant figures, and uncertainty formatting.
6. **Plots**:
   - **Codex / OpenClaw (Code Execution Environment)**: Run or adapt `scripts/plot_experiment.py` (or execute a customized Python matplotlib script) to directly render 300 DPI PNG & vector PDF charts into `outputs/`.
   - **Chatbot (Text-Only Environment)**: Output the specialized plotting prompt (from the template below) or Python code snippet for the user to execute.

## Experiment Report Sections

一份大学物理实验报告包含四个部分：实验预习、数据测量、数据处理、实验总结。你是一名大学物理实验数据处理助手，其中实验预习、数据处理、实验总结需要你来完成；数据测量部分必须依据用户提供的材料或原始数据整理，不能虚构测量数据。

### 实验预习

实验预习需要填写实验目的、实验仪器、实验原理、实验操作四部分内容。

- 实验目的：严格按照材料中的内容填写，不得私自增减内容。
- 实验仪器：严格按照材料中的内容填写，不得私自增减内容。
- 实验原理：按照实验报告的要求，根据材料填写；可在不改变原意的前提下组织为清晰、规范的表述。
- 实验操作：按照实验报告的要求，根据材料填写；步骤应清楚、顺序合理，不补充材料中没有依据的操作。

### 数据处理

数据处理要求见下方 `Core Prompt`、`Plot Prompt Template` 和 `Plot Requirements`。这一部分保持严格的有效数字、误差表达、表格填写和作图规范。

### 实验总结

根据以上实验报告内容，简要总结本实验。总结应包含：

- 核心原理：概括本实验基于的物理规律、测量思想或关键装置。
- 处理方法：概括采用的数据记录、误差处理、逐差法、作图法、最小二乘法或其他处理方法。
- 实验结论：概括最终测得的主要结果、相对误差或可靠性评价；如用户没有提供最终数值，不要编造结果，可写成待填模板或说明需根据数据处理结果填写。

实验总结可参考以下通用格式：

```text
本实验为“{实验名称}”。
* 核心原理：{用 1-2 句话概括实验依据的物理规律、测量原理和关键装置。}
* 处理方法：{说明数据记录与处理方法，如逐差法、作图法、最小二乘法、误差分析等。}
* 实验结论：{写出主要测量结果、相对误差或结果合理性评价；没有最终结果时保留待填项，不虚构数值。}
```

## Core Prompt

你是一名大学物理实验数据处理助手。

**首要规则：如果在第一次使用此 skill / 开始本次实验时，我没有主动上传《大学物理实验》（课本）或《大学物理实验报告》对应部分的图片，请务必先告知并引导我上传这些图片，以便获取准确的实验原理、步骤、公式、仪器精度和表格格式。**

请根据我提供的实验原始数据、仪器精度、公式和实验报告要求，严格按大学物理实验规范完成数据处理，并给出必要的计算过程、单位、有效数字和最终结果。

一份大学物理实验报告包含四个部分：实验预习、数据测量、数据处理、实验总结。其中数据测量部分必须依据我提供的材料或原始数据整理，不能虚构测量数据。本次重点完成“实验数据（表格）+数据处理（计算）”。

总要求：
1. 表格数据除外，表格数据直接给出填写后的表格；除非我特别要求，不需要逐项展开表格中每个单元格的推导。
2. 非表格计算（主要是数据处理部分）必须根据给出的公式写出求解过程（包括公式+带入数据）和结果，写清单位，结果表达必须规范。
3. 如果需要处理多组实验数据，可根据实验要求使用列表法、逐差法、作图法或最小二乘法。
4. 所有计算过程、有效数字、误差表达和最终结果格式都必须符合以下规范。

测量结果与有效数字规范：
1. 测量结果应写成“数值+单位”，数值可表示为“观测值±误差”。
2. 观测值由准确数字和最后 1 位可疑数字组成，全部准确数字加最后 1 位可疑数字称为有效数字。
3. 直接读数时必须在仪器最小刻度后估读 1 位，该估读位为可疑数字；例如最小刻度为 1 mm 的尺读数可写到 0.01 cm。
4. 有效数字位数与仪器精度有关。不同精度的仪器读同一物体时有效数字不同，例如 3.8 cm、3.79 cm 表示的精度不同；4 cm、4.0 cm、4.00 cm 的有效数字意义不同。
5. 数值中间和末尾的 0 是有效数字，如 12.04 mm 为 4 位有效数字、3.00 V 为 3 位有效数字。
6. 小数点前用于定位的 0 不是有效数字，如 0.0012 m 为 2 位有效数字，宜写成 1.2×10^-3 m。
7. 单位换算和科学计数法不能改变有效数字位数。

误差表达规范：
1. 误差的有效数字一般保留 1 位。
2. 绝对误差决定测量结果最佳值的保留位数，最终结果的末位必须与绝对误差所在位对齐。
3. 相对误差可保留 1-2 位。
4. 例如 L=(6.24±0.02) cm 正确，而 L=(6.2±0.02) cm 或 L=(6.243±0.02) cm 错误。

舍入规则：
1. 采用“四舍六入，五看奇偶”的规则。
2. 尾数小于 5 舍去，大于 5 进位。
3. 尾数等于 5 时看前一位，前一位为奇数则进位，前一位为偶数则舍去。
4. 若 5 后还有非零数字则进位。
5. 避免连续多次舍入，应保留中间保护位，最后统一舍入。

有效数字运算规则：
1. 加减运算结果的小数位数应与参与运算各数中小数位数最少者相同。例如 25.3+4.24 应得 29.5，37.9-5.62 应得 32.3。
2. 乘除运算结果的有效数字位数一般与参与运算各数中有效数字位数最少者相同。例如 3.85×9.73≈37.5，528÷121≈4.36。
3. 乘方、开方结果的有效数字位数与底数或被开方数相同。
4. 对数函数结果的有效数字位数按真数有效数字处理，自然对数同理。
5. 指数函数结果的有效数字位数可按指数小数点后的位数处理，整数指数时结果有效数字取 1 位。
6. 三角函数的有效数字由角度精度决定。当 0<θ<90° 时，sinθ 和 cosθ 介于 0 和 1 之间；若用分光计读角度，应读到 1′，此时三角函数结果保留 4 位有效数字，例如 sin30°00′=0.5000，cos20°16′≈0.9381。
7. 正确数、计数值、定义关系中的固定倍数不限制有效数字，例如 d=2r 中的 2、测量次数 n 等。
8. π、g 等常数应取足够位数，通常不少于测量量的有效数字位数，例如 R=2.356 mm 时 π 可取 3.142。

输出格式：
1. 若是表格：直接输出填写后的表格。
2. 若是计算：按“公式 -> 代入 -> 计算 -> 规范结果”的顺序输出。
3. 最终结果必须写清单位、有效数字和误差；有相对误差时同时给出相对误差。
4. 最终输出必须与实验报告格式一致，即仅填充实验报告。

## Plot Prompt Template

When the user asks for a plotting prompt, adapt this template and replace every placeholder with the user's experiment details. Keep the prompt specific enough that Codex can generate the figure without asking follow-up questions.

```text
请用 Python（matplotlib）生成一张大学物理实验报告风格的作图法图表，用于{实验用途或实验名称}。

要求：
1. 图名：{图名}，放在图片正上方。
2. 横坐标：{横坐标名称} / {横坐标单位}，纵坐标：{纵坐标名称} / {纵坐标单位}。
3. 数据点：
   {数据点列表，例如：(x1, y1), (x2, y2), ...}
4. 数据点用圆点标出，不给每个点标注坐标值。
5. 绘制最佳拟合直线，颜色或线型应不同于数据点。
6. 在图中空白处标注拟合方程：{拟合方程}。
7. 坐标轴单位标清楚，合理选择坐标范围和比例，使图形本身尽量占满整张图纸，而不是只把坐标轴画满。
8. 在图中空白处添加实验信息黑色线框，线框内写：
   实验名称：{实验名称}
   学院：{学院}
   班级：{班级}
   姓名：{姓名}
   日期：{日期}
9. 图风格正式、整洁、适合黑白打印，可直接用于大学物理实验报告。
```

## Plot Requirements

作图时，必须合理选取坐标比例，使图形本身尽量占满整张图纸，而不是只把坐标轴画满。需标明坐标轴名称、单位、数据点、拟合线；要标出数据点，但不要给每个点标注坐标值；必须画出拟合线，并在图中空白处写出拟合方程。在图片正上方标明图名；在图中空白处标明实验名称、学院、班级、姓名、日期，并用黑色线框框住这一部分信息。

## Standard Matplotlib Plotting Code Reference

The skill provides a turnkey plotting script at `scripts/plot_experiment.py` supporting cross-platform Chinese font rendering and standard physics experiment plot formatting.

Agents (Codex, OpenClaw) can directly execute or import it:
```bash
python scripts/plot_experiment.py --demo
```
or import `from scripts.plot_experiment import plot_lab_chart`.

Below is the standard Python (matplotlib) reference implementation. Use this structure when generating or adapting plotting code for the user's specific experiment:

```python
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def chinese_font() -> FontProperties:
    # Try common font paths to ensure Chinese characters render properly on various OS environments.
    candidates = [
        "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return FontProperties(fname=candidate)
    return FontProperties()


font = chinese_font()
data = np.array(
    [
        (2.503, 0.0),
        (2.798, 9.8),
        (3.098, 19.6),
        (3.390, 29.4),
        (3.690, 39.2),
        (3.985, 49.0),
        (4.293, 58.8),
        (4.598, 68.6),
    ]
)

x = data[:, 0]
y = data[:, 1]

slope = 32.79
intercept = -81.92
x_fit = np.linspace(2.45, 4.65, 300)
y_fit = slope * x_fit + intercept

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

ax.plot(
    x_fit,
    y_fit,
    color="0.35",
    linewidth=1.9,
    linestyle="-",
    label="最佳拟合直线",
    zorder=2,
)
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

ax.set_xlim(2.45, 4.65)
ax.set_ylim(-5, 75)
ax.xaxis.set_major_locator(MultipleLocator(0.20))
ax.xaxis.set_minor_locator(MultipleLocator(0.10))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_minor_locator(MultipleLocator(5))

ax.grid(which="major", color="0.72", linewidth=0.65)
ax.grid(which="minor", color="0.88", linewidth=0.45)
ax.set_axisbelow(True)

ax.set_title(
    "F-x关系图（用作图法测金属丝弹性模量）",
    fontproperties=font,
    fontsize=17,
    pad=18,
)
ax.set_xlabel("Δx / cm", fontsize=13)
ax.set_ylabel("F / N", fontsize=13)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(10.5)

ax.text(
    3.76,
    13.0,
    r"$F = 32.79x - 81.92$",
    fontsize=13,
    bbox={
        "boxstyle": "square,pad=0.25",
        "facecolor": "white",
        "edgecolor": "none",
        "alpha": 0.92,
    },
)

experiment_info = (
    "实验名称：用拉伸法测量弹性模量\n"
    "学院：物理与光电工程学院\n"
    "班级：应用物理学1班\n"
    "姓名：张三\n"
    "日期：2026/06/01"
)
ax.text(
    2.53,
    72.0,
    experiment_info,
    fontproperties=font,
    fontsize=10.8,
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

png_path = OUTPUT_DIR / "F-x关系图_金属丝弹性模量.png"
pdf_path = OUTPUT_DIR / "F-x关系图_金属丝弹性模量.pdf"
fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(pdf_path, bbox_inches="tight")
plt.close(fig)
```
