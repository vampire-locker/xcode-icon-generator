# Xcode 图标批量生成工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

中文文档 | [English](README.md)

一个 Python 工具，可以从单个 1024×1024 的源图像自动生成所有 iOS/iPadOS 应用所需的图标尺寸。

## 特性

- 🚀 **一键生成**：生成 Xcode 所需的全部 13 种图标尺寸
- ✅ **Xcode 就绪**：自动创建 `Contents.json` 配置文件
- 🔍 **输入验证**：检查图片格式、尺寸和透明度
- 🎨 **自动缩放**：可选自动缩放非 1024 尺寸的图片
- 📦 **零配置**：开箱即用，使用合理的默认设置
- 💻 **双模式**：支持命令行参数和交互式输入

## 生成的图标尺寸

该工具会生成 iOS 和 iPadOS 所需的以下尺寸：

| 尺寸 (像素) | 用途 |
|-----------|------|
| 20, 40, 60 | iPhone 通知、设置、Spotlight |
| 29, 58, 87 | iPhone 设置 |
| 80, 120, 180 | iPhone 应用图标 |
| 76, 152 | iPad 应用图标 |
| 167 | iPad Pro 应用图标 |
| 1024 | App Store |

## 系统要求

- Python 3.6 或更高版本
- Pillow (PIL) 10.0.0+

## 安装

1. 克隆此仓库：
```bash
git clone https://github.com/yourusername/BatchResizePicForXcode.git
cd BatchResizePicForXcode
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

### 交互式模式

直接运行脚本并按照提示操作：

```bash
python batch_resize_icon.py
```

### 命令行模式

```bash
# 基本用法
python batch_resize_icon.py icon_1024.png

# 指定自定义输出目录
python batch_resize_icon.py icon_1024.png -o MyAppIcon.appiconset

# 自动缩放非 1024x1024 的图片
python batch_resize_icon.py icon_512.png --auto-scale

# 启用详细输出
python batch_resize_icon.py icon_1024.png -v
```

### 命令行选项

| 选项 | 说明 |
|------|------|
| `input_image` | 源图片路径（推荐 1024×1024 PNG 格式） |
| `-o, --output DIR` | 自定义输出目录名称 |
| `-a, --auto-scale` | 自动缩放非 1024×1024 的图片 |
| `-v, --verbose` | 启用详细输出 |
| `--version` | 显示版本信息 |
| `-h, --help` | 显示帮助信息 |

## 最佳实践

为了获得最佳效果，您的源图片应该：
- **1024×1024 像素** - App Store 要求的尺寸
- **PNG 格式** - 支持透明度
- **透明背景** - iOS 图标标准
- **正方形** - iOS 要求

## 输出结果

工具会创建一个文件夹（例如 `AppIcon.appiconset_1234567890`），包含：
- 13 个 PNG 文件，涵盖所有需要的图标尺寸（命名为 `_20.png`、`_29.png` 等）
- `Contents.json` - Xcode 配置文件

您可以将整个文件夹直接拖入 Xcode 项目的 Assets.xcassets 中。

## 使用示例

```bash
$ python batch_resize_icon.py my_icon_1024.png
INFO: Output directory: /path/to/AppIcon.appiconset_1701234567
INFO: Starting icon generation...
INFO: Successfully generated 13/13 icons
INFO: Generated: Contents.json

✓ All icons generated successfully!
Output location: /path/to/AppIcon.appiconset_1701234567

You can now drag the 'AppIcon.appiconset_1701234567' folder into Xcode.
```

## 在 Xcode 中使用

1. 运行工具生成图标
2. 打开您的 Xcode 项目
3. 导航到 `Assets.xcassets`
4. 删除现有的 `AppIcon` 资源（如果有）
5. 将生成的 `.appiconset` 文件夹拖入 Assets.xcassets
6. 如需要，将其重命名为 `AppIcon`

## 常见问题

### "Image must be 1024x1024"（图片必须是 1024x1024）
您的源图片尺寸不正确。使用 `--auto-scale` 参数自动调整大小：
```bash
python batch_resize_icon.py icon.png --auto-scale
```

### "Unsupported format"（不支持的格式）
工具仅支持 PNG、JPG 和 JPEG 格式。请先转换您的图片。

### "Image doesn't have transparency"（图片没有透明度）
这是一个警告而非错误。iOS 图标通常使用透明背景，但如果您的设计需要纯色背景，可以继续使用。

## 贡献

欢迎贡献！请随时提交 Pull Request。

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请见 [LICENSE](LICENSE) 文件。

## 更新日志

### 版本 2.0 (2025)
- 使用现代 Python 实践进行完全重构
- 添加命令行参数支持
- 添加输入验证和错误处理
- 修复已弃用的 PIL API 使用
- 添加自动缩放功能
- 改进日志记录和用户反馈
- 添加完整文档

### 版本 1.0 (2018)
- 初始版本
- 基本图标生成功能

## 作者

原作者：vampire (2018)
重构：2025

## 致谢

- 使用 [Pillow (PIL)](https://python-pillow.org/) 构建
- 图标尺寸要求基于 [Apple 人机界面指南](https://developer.apple.com/design/human-interface-guidelines/)

---

如果这个工具对您有帮助，请在 GitHub 上给它一个 ⭐️！
