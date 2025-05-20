# Example Clients
Source: https://modelcontextprotocol.io/clients
# 示例客户来源: https://modelcontextprotocol.io/clients

A list of applications that support MCP integrations
支持 MCP 集成的应用程序列表

This page provides an overview of applications that support the Model Context Protocol (MCP). Each client may support different MCP features, allowing for varying levels of integration with MCP servers.
本页提供了支持模型上下文协议（MCP）的应用程序的概述。每个客户端可能支持不同的 MCP 功能，允许与 MCP 服务器进行不同程度的集成。

## Feature support matrix
## 功能支持矩阵

| Client                               | [Resources] | [Prompts] | [Tools] | [Sampling] | Roots | Notes                                                                                           |
| ------------------------------------ | ----------- | --------- | ------- | ---------- | ----- | ----------------------------------------------------------------------------------------------- |
| [5ire][5ire]                         | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools.                                                                                 |
| [Apify MCP Tester][Apify MCP Tester] | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools                                                                                  |
| [BeeAI Framework][BeeAI Framework]   | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools in agentic workflows.                                                            |
| [Claude Code][Claude Code]           | ❌           | ✅         | ✅       | ❌          | ❌     | Supports prompts and tools                                                                      |
| [Claude Desktop App][Claude Desktop] | ✅           | ✅         | ✅       | ❌          | ❌     | Supports tools, prompts, and resources.                                                         |
| [Cline][Cline]                       | ✅           | ❌         | ✅       | ❌          | ❌     | Supports tools and resources.                                                                   |
| [Continue][Continue]                 | ✅           | ✅         | ✅       | ❌          | ❌     | Supports tools, prompts, and resources.                                                         |
| [Copilot-MCP][CopilotMCP]            | ✅           | ❌         | ✅       | ❌          | ❌     | Supports tools and resources.                                                                   |
| [Cursor][Cursor]                     | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools.                                                                                 |
| [Daydreams Agents][Daydreams]        | ✅           | ✅         | ✅       | ❌          | ❌     | Support for drop in Servers to Daydreams agents                                                 |
| [Emacs Mcp][Mcp.el]                  | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools in Emacs.                                                                        |
| [fast-agent][fast-agent]             | ✅           | ✅         | ✅       | ✅          | ✅     | Full multimodal MCP support, with end-to-end tests                                              |
| [Genkit][Genkit]                     | ⚠️          | ✅         | ✅       | ❌          | ❌     | Supports resource list and lookup through tools.                                                |
| [GenAIScript][GenAIScript]           | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools.                                                                                 |
| [Goose][Goose]                       | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools.                                                                                 |
| [LibreChat][LibreChat]               | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools for Agents                                                                       |
| [mcp-agent][mcp-agent]               | ❌           | ❌         | ✅       | ⚠️         | ❌     | Supports tools, server connection management, and agent workflows.                              |
| [Microsoft Copilot Studio]           | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools                                                                                  |
| [OpenSumi][OpenSumi]                 | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools in OpenSumi                                                                      |
| [oterm][oterm]                       | ❌           | ✅         | ✅       | ✅          | ❌     | Supports tools, prompts and sampling for Ollama.                                                |
| [Roo Code][Roo Code]                 | ✅           | ❌         | ✅       | ❌          | ❌     | Supports tools and resources.                                                                   |
| [Sourcegraph Cody][Cody]             | ✅           | ❌         | ❌       | ❌          | ❌     | Supports resources through OpenCTX                                                              |
| [SpinAI][SpinAI]                     | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools for Typescript AI Agents                                                         |
| [Superinterface][Superinterface]     | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools                                                                                  |
| [TheiaAI/TheiaIDE][TheiaAI/TheiaIDE] | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools for Agents in Theia AI and the AI-powered Theia IDE                              |
| [VS Code GitHub Copilot][VS Code]    | ❌           | ❌         | ✅       | ❌          | ✅     | Supports dynamic tool/roots discovery, secure secret configuration, and explicit tool prompting |
| [Windsurf Editor][Windsurf]          | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools with AI Flow for collaborative development.                                      |
| [Witsy][Witsy]                       | ❌           | ❌         | ✅       | ❌          | ❌     | Supports tools in Witsy.                                                                        |
| [Zed][Zed]                           | ❌           | ✅         | ❌       | ❌          | ❌     | Prompts appear as slash commands                                                                |
| 客户端 | [资源] | [提示] | [工具] | [采样] | 根 | 备注 | | ------------------------------------ | ----------- | --------- | ------- | ---------- | ----- | ----------------------------------------------------------------------------------------------- | | [5ire][5ire] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持工具。 | | [Apify MCP 测试器][Apify MCP 测试器] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持工具 | | [BeeAI 框架][BeeAI 框架] | ❌ | ❌ | ✅ | ❌ | ❌ | 在代理工作流程中支持工具。 | | [Claude 代码][Claude 代码] | ❌ | ✅ | ✅ | ❌ | ❌ | 支持提示和工具 | | [Claude 桌面应用][Claude 桌面] | ✅ | ✅ | ✅ | ❌ | ❌ | 支持工具、提示和资源。 | | [Cline][Cline] | ✅ | ❌ | ✅ | ❌ | ❌ | 支持工具和资源。 | | [Continue][Continue] | ✅ | ✅ | ✅ | ❌ | ❌ | 支持工具、提示和资源。 | | [Copilot-MCP][CopilotMCP] | ✅ | ❌ | ✅ | ❌ | ❌ | 支持工具和资源。 | | [Cursor][Cursor] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持工具。 | | [Daydreams 代理][Daydreams] | ✅ | ✅ | ✅ | ❌ | ❌ | 支持将服务器直接嵌入 Daydreams 代理。 | | [Emacs Mcp][Mcp.el] | ❌ | ❌ | ✅ | ❌ | ❌ | 在 Emacs 中支持工具。 | | | [fast-agent][fast-agent] | ✅ | ✅ | ✅ | ✅ | ✅ | 全多模态 MCP 支持，具有端到端测试 | | [Genkit][Genkit] | ⚠️ | ✅ | ✅ | ❌ | ❌ | 支持通过工具的资源列表和查找。 | | [GenAIScript][GenAIScript] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持工具。 | | [Goose][Goose] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持工具。 | | [LibreChat][LibreChat] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持为代理的工具。 | | [mcp-agent][mcp-agent] | ❌ | ❌ | ✅ | ⚠️ | ❌ | 支持工具、服务器连接管理和代理工作流程。 | | [Microsoft Copilot Studio] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持工具 | | [OpenSumi][OpenSumi] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持 OpenSumi 中的工具 | | [oterm][oterm] | ❌ | ✅ | ✅ | ✅ | ❌ | 支持工具、提示和 Ollama 的采样。 | | [Roo Code][Roo Code] | ✅ | ❌ | ✅ | ❌ | ❌ | 支持工具和资源。 | | [Sourcegraph Cody][Cody] | ✅ | ❌ | ❌ | ❌ | ❌ | 通过 OpenCTX 支持资源 | | [SpinAI][SpinAI] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持为 TypeScript AI 代理提供工具 | | [Superinterface][Superinterface] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持工具 | | [TheiaAI/TheiaIDE][TheiaAI/TheiaIDE] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持在 Theia AI 和 AI 驱动的 Theia IDE 中的代理工具 | | [VS Code GitHub Copilot][VS Code] | ❌ | ❌ | ✅ | ❌ | ✅ | 支持动态工具/根发现、安全密钥配置和显式工具提示 | | [Windsurf Editor][Windsurf] | ❌ | ❌ | ✅ | ❌ | ❌ | 支持具有 AI 流的协作开发工具 | | [Witsy][Witsy] | ❌ | ❌ | ✅ | ❌ | ❌ | 在 Witsy 中支持工具 | | [Zed][Zed] | ❌ | ✅ | ❌ | ❌ | ❌ | 提示以斜杠命令的形式出现 |

[5ire]: https://github.com/nanbingxyz/5ire

[Apify MCP Tester]: https://apify.com/jiri.spilka/tester-mcp-client

[BeeAI Framework]: https://i-am-bee.github.io/beeai-framework

[Claude Code]: https://claude.ai/code

[Claude Desktop]: https://claude.ai/download
[Claude 桌面]: https://claude.ai/download

[Cline]: https://github.com/cline/cline

[Continue]: https://github.com/continuedev/continue

[CopilotMCP]: https://github.com/VikashLoomba/copilot-mcp

[Cursor]: https://cursor.com

[Daydreams]: https://github.com/daydreamsai/daydreams

[Mcp.el]: https://github.com/lizqwerscott/mcp.el

[fast-agent]: https://github.com/evalstate/fast-agent

[Genkit]: https://github.com/firebase/genkit

[GenAIScript]: https://microsoft.github.io/genaiscript/reference/scripts/mcp-tools/

[Goose]: https://block.github.io/goose/docs/goose-architecture/#interoperability-with-extensions

[LibreChat]: https://github.com/danny-avila/LibreChat

[mcp-agent]: https://github.com/lastmile-ai/mcp-agent

[Microsoft Copilot Studio]: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp

[OpenSumi]: https://github.com/opensumi/core

[oterm]: https://github.com/ggozad/oterm

[Roo Code]: https://roocode.com

[Cody]: https://sourcegraph.com/cody

[SpinAI]: https://spinai.dev

[Superinterface]: https://superinterface.ai
[超级接口]: https://superinterface.ai

[TheiaAI/TheiaIDE]: https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/

[VS Code]: https://code.visualstudio.com/

[Windsurf]: https://codeium.com/windsurf

[Witsy]: https://github.com/nbonamy/witsy

[Zed]: https://zed.dev

[Resources]: https://modelcontextprotocol.io/docs/concepts/resources
[资源]: https://modelcontextprotocol.io/docs/concepts/resources

[Prompts]: https://modelcontextprotocol.io/docs/concepts/prompts
[提示]: https://modelcontextprotocol.io/docs/concepts/prompts

[Tools]: https://modelcontextprotocol.io/docs/concepts/tools
[工具]: https://modelcontextprotocol.io/docs/concepts/tools

[Sampling]: https://modelcontextprotocol.io/docs/concepts/sampling
[采样]: https://modelcontextprotocol.io/docs/concepts/sampling

## Client details  ## 客户详情

### 5ire

[5ire](https://github.com/nanbingxyz/5ire) is an open source cross-platform desktop AI assistant that supports tools through MCP servers.
[5ire](https://github.com/nanbingxyz/5ire) 是一个开源的跨平台桌面 AI 助手，支持通过 MCP 服务器使用工具。

**Key features:**  **主要功能：**

* Built-in MCP servers can be quickly enabled and disabled.
* Users can add more servers by modifying the configuration file.
* It is open-source and user-friendly, suitable for beginners.
* Future support for MCP will be continuously improved.
* 内置 MCP 服务器可以快速启用和禁用。* 用户可以通过修改配置文件添加更多服务器。* 它是开源且用户友好的，适合初学者。* 未来将对 MCP 的支持持续改进。

### Apify MCP Tester  ### Apify MCP 测试器

[Apify MCP Tester](https://github.com/apify/tester-mcp-client) is an open-source client that connects to any MCP server using Server-Sent Events (SSE).
It is a standalone Apify Actor designed for testing MCP servers over SSE, with support for Authorization headers.
It uses plain JavaScript (old-school style) and is hosted on Apify, allowing you to run it without any setup.
[Apify MCP 测试器](https://github.com/apify/tester-mcp-client) 是一个开源客户端，可以通过服务器端事件（SSE）连接到任何 MCP 服务器。它是一个独立的 Apify Actor，用于通过 SSE 测试 MCP 服务器，支持授权头。它使用纯 JavaScript（老式风格）并在 Apify 上托管，允许您无需任何设置即可运行。

**Key features:**  **主要功能：**

* Connects to any MCP server via SSE.
* Works with the [Apify MCP Server](https://apify.com/apify/actors-mcp-server) to interact with one or more Apify [Actors](https://apify.com/store).
* Dynamically utilizes tools based on context and user queries (if supported by the server).
* 通过 SSE 连接到任何 MCP 服务器。 * 与 [Apify MCP 服务器](https://apify.com/apify/actors-mcp-server) 配合使用，以与一个或多个 Apify [Actor](https://apify.com/store) 交互。 * 根据上下文和用户查询动态使用工具（如果服务器支持）。

### BeeAI Framework  ### BeeAI 框架

[BeeAI Framework](https://i-am-bee.github.io/beeai-framework) is an open-source framework for building, deploying, and serving powerful agentic workflows at scale. The framework includes the **MCP Tool**, a native feature that simplifies the integration of MCP servers into agentic workflows.
[BeeAI 框架](https://i-am-bee.github.io/beeai-framework) 是一个开源框架，用于构建、部署和大规模服务强大的代理工作流程。该框架包括 **MCP 工具**，这是一个本地功能，简化了将 MCP 服务器集成到代理工作流程中。

**Key features:**  **关键特性：**

* Seamlessly incorporate MCP tools into agentic workflows.
* Quickly instantiate framework-native tools from connected MCP client(s).
* Planned future support for agentic MCP capabilities.
* 无缝将 MCP 工具集成到代理工作流程中。 * 快速从连接的 MCP 客户端实例化框架原生工具。 * 计划支持未来的代理 MCP 功能。

**Learn more:**  **了解更多：**

* [Example of using MCP tools in agentic workflow](https://i-am-bee.github.io/beeai-framework/#/typescript/tools?id=using-the-mcptool-class)
* [使用 MCP 工具的代理工作流程示例](https://i-am-bee.github.io/beeai-framework/#/typescript/tools?id=using-the-mcptool-class)

### Claude Code  ### Claude 代码

Claude Code is an interactive agentic coding tool from Anthropic that helps you code faster through natural language commands. It supports MCP integration for prompts and tools, and also functions as an MCP server to integrate with other clients.
Claude 代码是 Anthropic 推出的一款交互式代理编码工具，通过自然语言命令帮助您更快地编码。它支持 MCP 集成以用于提示和工具，并可作为 MCP 服务器与其他客户端集成。

**Key features:**  **主要功能：**

* Tool and prompt support for MCP servers
* Offers its own tools through an MCP server for integrating with other MCP clients
* MCP 服务器工具和提示支持 * 通过 MCP 服务器提供自己的工具，以与其他 MCP 客户端集成

### Claude Desktop App  ### Claude 桌面应用程序

The Claude desktop application provides comprehensive support for MCP, enabling deep integration with local tools and data sources.
Claude 桌面应用程序为 MCP 提供全面支持，能够与本地工具和数据源深度集成。

**Key features:**  **主要功能：**

* Full support for resources, allowing attachment of local files and data
* Support for prompt templates
* Tool integration for executing commands and scripts
* Local server connections for enhanced privacy and security
* 全面的资源支持，允许附加本地文件和数据 * 支持提示模板 * 工具集成以执行命令和脚本 * 本地服务器连接以增强隐私和安全

> ⓘ Note: The Claude.ai web application does not currently support MCP. MCP features are only available in the desktop application.
ⓘ 注意：Claude.ai 网络应用程序目前不支持 MCP。MCP 功能仅在桌面应用程序中可用。

### Cline

[Cline](https://github.com/cline/cline) is an autonomous coding agent in VS Code that edits files, runs commands, uses a browser, and more–with your permission at each step.
[Cline](https://github.com/cline/cline) 是 VS Code 中的自主编码代理，在您的许可下编辑文件、运行命令、使用浏览器等。

**Key features:**  **关键特性：**

* Create and add tools through natural language (e.g. "add a tool that searches the web")
* Share custom MCP servers Cline creates with others via the `~/Documents/Cline/MCP` directory
* Displays configured MCP servers along with their tools, resources, and any error logs
* 通过自然语言创建和添加工具（例如：“添加一个搜索网络的工具”） * 将 Cline 创建的定制 MCP 服务器与他人共享到`~/Documents/Cline/MCP`目录下 * 显示配置的 MCP 服务器及其工具、资源和任何错误日志

### Continue  ### 继续阅读

[Continue](https://github.com/continuedev/continue) is an open-source AI code assistant, with built-in support for all MCP features.
[继续](https://github.com/continuedev/continue) 是一个开源的 AI 代码助手，内置所有 MCP 功能支持。

**Key features**  **关键特性**

* Type "@" to mention MCP resources
* Prompt templates surface as slash commands
* Use both built-in and MCP tools directly in chat
* Supports VS Code and JetBrains IDEs, with any LLM
* 输入 "@" 以提及 MCP 资源 * 提示模板以斜杠命令的形式呈现 * 可直接在聊天中使用内置和 MCP 工具 * 支持 VS Code 和 JetBrains IDE，任何 LLM

### Copilot-MCP

[Copilot-MCP](https://github.com/VikashLoomba/copilot-mcp) enables AI coding assistance via MCP.
[Copilot-MCP](https://github.com/VikashLoomba/copilot-mcp) 通过 MCP 提供人工智能编码辅助。

**Key features:**  **关键特性：**

* Support for MCP tools and resources
* Integration with development workflows
* Extensible AI capabilities
* 支持 MCP 工具和资源 * 集成开发工作流程 * 可扩展的 AI 能力

### Cursor  ### 光标

[Cursor](https://docs.cursor.com/advanced/model-context-protocol) is an AI code editor.
[光标](https://docs.cursor.com/advanced/model-context-protocol) 是一个 AI 代码编辑器。

**Key Features**:  **关键特性**:

* Support for MCP tools in Cursor Composer
* Support for both STDIO and SSE
* 支持 Cursor Composer 中的 MCP 工具 * 支持 STDIO 和 SSE

### Daydreams  ### 梦幻

[Daydreams](https://github.com/daydreamsai/daydreams) is a generative agent framework for executing anything onchain
[梦幻](https://github.com/daydreamsai/daydreams) 是一个用于在链上执行任何操作的生成代理框架

**Key features:**  **关键特性：**

* Supports MCP Servers in config
* Exposes MCP Client
* 支持配置中的 MCP 服务器 * 暴露 MCP 客户端

### Emacs Mcp

[Emacs Mcp](https://github.com/lizqwerscott/mcp.el) is an Emacs client designed to interface with MCP servers, enabling seamless connections and interactions. It provides MCP tool invocation support for AI plugins like [gptel](https://github.com/karthink/gptel) and [llm](https://github.com/ahyatt/llm), adhering to Emacs' standard tool invocation format. This integration enhances the functionality of AI tools within the Emacs ecosystem.
[Emacs Mcp](https://github.com/lizqwerscott/mcp.el) 是一个用于与 MCP 服务器交互的 Emacs 客户端，实现了无缝连接和交互。它为 AI 插件如[gptel](https://github.com/karthink/gptel)和[llm](https://github.com/ahyatt/llm)提供了 MCP 工具调用支持，遵循 Emacs 标准的工具调用格式。这种集成增强了 Emacs 生态系统中 AI 工具的功能。

**Key features:**  **关键特性：**

* Provides MCP tool support for Emacs.
* 提供 Emacs 的 MCP 工具支持。

### fast-agent

[fast-agent](https://github.com/evalstate/fast-agent) is a Python Agent framework, with simple declarative support for creating Agents and Workflows, with full multi-modal support for Anthropic and OpenAI models.
[fast-agent](https://github.com/evalstate/fast-agent) 是一个 Python 代理框架，具有简单的声明性支持用于创建代理和工作流程，以及全面的多模态支持用于 Anthropic 和 OpenAI 模型。

**Key features:**  **关键特性：**

* PDF and Image support, based on MCP Native types
* Interactive front-end to develop and diagnose Agent applications, including passthrough and playback simulators
* Built in support for "Building Effective Agents" workflows.
* Deploy Agents as MCP Servers
* 基于 MCP 本地类型的 PDF 和图像支持 * 提供交互式前端以开发和诊断代理应用程序，包括透传和回放模拟器 * 内置“构建有效代理”工作流支持 * 将代理作为 MCP 服务器部署

### Genkit

[Genkit](https://github.com/firebase/genkit) is a cross-language SDK for building and integrating GenAI features into applications. The [genkitx-mcp](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) plugin enables consuming MCP servers as a client or creating MCP servers from Genkit tools and prompts.
[Genkit](https://github.com/firebase/genkit) 是一个跨语言 SDK，用于构建和集成 GenAI 功能到应用程序中。[genkitx-mcp](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 插件允许作为客户端消费 MCP 服务器或从 Genkit 工具和提示中创建 MCP 服务器。

**Key features:**  **关键特性：**

* Client support for tools and prompts (resources partially supported)
* Rich discovery with support in Genkit's Dev UI playground
* Seamless interoperability with Genkit's existing tools and prompts
* Works across a wide variety of GenAI models from top providers
* 工具和提示（资源部分支持）的客户支持 * 支持在 Genkit 的 Dev UI 游乐场中进行丰富的发现 * 与 Genkit 现有工具和提示的无缝互操作性 * 支持来自顶级提供商的广泛各种 GenAI 模型

### GenAIScript

Programmatically assemble prompts for LLMs using [GenAIScript](https://microsoft.github.io/genaiscript/) (in JavaScript). Orchestrate LLMs, tools, and data in JavaScript.
使用[GenAIScript](https://microsoft.github.io/genaiscript/)（JavaScript）编程组装针对LLMs的提示。使用 JavaScript 编排LLMs、工具和数据。

**Key features:**  **关键特性：**

* JavaScript toolbox to work with prompts
* Abstraction to make it easy and productive
* Seamless Visual Studio Code integration
* JavaScript 工具箱，用于处理提示 * 提供抽象，使工作轻松高效 * 与 Visual Studio Code 无缝集成

### Goose  ### 鹅

[Goose](https://github.com/block/goose) is an open source AI agent that supercharges your software development by automating coding tasks.
[鹅](https://github.com/block/goose) 是一个开源的 AI 代理，通过自动化编码任务来增强您的软件开发。

**Key features:**  **关键特性：**

* Expose MCP functionality to Goose through tools.
* MCPs can be installed directly via the [extensions directory](https://block.github.io/goose/v1/extensions/), CLI, or UI.
* Goose allows you to extend its functionality by [building your own MCP servers](https://block.github.io/goose/docs/tutorials/custom-extensions).
* Includes built-in tools for development, web scraping, automation, memory, and integrations with JetBrains and Google Drive.
* 将 MCP 功能通过工具暴露给 Goose。* MCP 可以直接通过[扩展目录](https://block.github.io/goose/v1/extensions/)、CLI 或 UI 进行安装。* Goose 允许您通过[构建自己的 MCP 服务器](https://block.github.io/goose/docs/tutorials/custom-extensions)来扩展其功能。* 包含内置的开发、网络爬取、自动化、内存和与 JetBrains 和 Google Drive 集成的工具。

### LibreChat

[LibreChat](https://github.com/danny-avila/LibreChat) is an open-source, customizable AI chat UI that supports multiple AI providers, now including MCP integration.
[LibreChat](https://github.com/danny-avila/LibreChat) 是一个开源、可定制的 AI 聊天 UI，支持多个 AI 提供商，现在包括 MCP 集成。

**Key features:**  **关键特性：**

* Extend current tool ecosystem, including [Code Interpreter](https://www.librechat.ai/docs/features/code_interpreter) and Image generation tools, through MCP servers
* Add tools to customizable [Agents](https://www.librechat.ai/docs/features/agents), using a variety of LLMs from top providers
* Open-source and self-hostable, with secure multi-user support
* Future roadmap includes expanded MCP feature support
* 扩展当前工具生态系统，包括 [代码解释器](https://www.librechat.ai/docs/features/code_interpreter) 和图像生成工具，通过 MCP 服务器 * 将工具添加到可定制的 [代理](https://www.librechat.ai/docs/features/agents)，使用来自顶级提供商的 LLMs 多种选择 * 开源且可自托管，支持安全的多用户环境 * 未来路线图包括扩展 MCP 功能支持

### mcp-agent

[mcp-agent] is a simple, composable framework to build agents using Model Context Protocol.
[mcp-agent] 是一个简单、可组合的框架，用于使用模型上下文协议构建代理。

**Key features:**  **关键特性：**

* Automatic connection management of MCP servers.
* Expose tools from multiple servers to an LLM.
* Implements every pattern defined in [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents).
* Supports workflow pause/resume signals, such as waiting for human feedback.
* 自动管理 MCP 服务器连接。 * 将多个服务器的工具暴露给LLM。 * 实现了[构建有效代理](https://www.anthropic.com/research/building-effective-agents)中定义的每个模式。 * 支持工作流程暂停/恢复信号，例如等待人工反馈。

### Microsoft Copilot Studio
### 微软 Copilot 工作室

[Microsoft Copilot Studio]  is a robust SaaS platform designed for building custom AI-driven applications and intelligent agents, empowering developers to create, deploy, and manage sophisticated AI solutions.
[微软 Copilot 工作室] 是一个强大的 SaaS 平台，旨在构建定制的 AI 驱动应用程序和智能代理，使开发者能够创建、部署和管理复杂的 AI 解决方案。

**Key features:**  **关键特性：**

* Support for MCP tools
* Extend Copilot Studio agents with MCP servers
* Leveraging Microsoft unified, governed, and secure API management solutions
* 支持 MCP 工具 * 通过 MCP 服务器扩展 Copilot Studio 代理 * 利用微软统一、受管理和安全的 API 管理解决方案

### OpenSumi

[OpenSumi](https://github.com/opensumi/core) is a framework helps you quickly build AI Native IDE products.
[OpenSumi](https://github.com/opensumi/core) 是一个框架，帮助您快速构建 AI 原生 IDE 产品。

**Key features:**  **关键特性：**

* Supports MCP tools in OpenSumi
* Supports built-in IDE MCP servers and custom MCP servers
* 支持 OpenSumi 中的 MCP 工具 * 支持内置 IDE MCP 服务器和自定义 MCP 服务器

### oterm

[oterm] is a terminal client for Ollama allowing users to create chats/agents.
[oterm] 是 Ollama 的终端客户端，允许用户创建聊天/代理。

**Key features:**  **关键特性：**

* Support for multiple fully customizable chat sessions with Ollama connected with tools.
* Support for MCP tools.
* 支持与 Ollama 连接并集成工具的多个可自定义聊天会话。 * 支持 MCP 工具。

### Roo Code  ### Roo 代码

[Roo Code](https://roocode.com) enables AI coding assistance via MCP.
[Roo 代码](https://roocode.com) 通过 MCP 提供 AI 编码辅助。

**Key features:**  **关键特性：**

* Support for MCP tools and resources
* Integration with development workflows
* Extensible AI capabilities
* 支持 MCP 工具和资源 * 集成开发工作流程 * 可扩展的 AI 能力

### Sourcegraph Cody

[Cody](https://openctx.org/docs/providers/modelcontextprotocol) is Sourcegraph's AI coding assistant, which implements MCP through OpenCTX.
[Cody](https://openctx.org/docs/providers/modelcontextprotocol) 是 Sourcegraph 的 AI 编码助手，通过 OpenCTX 实现 MCP。

**Key features:**  **关键特性：**

* Support for MCP resources
* Integration with Sourcegraph's code intelligence
* Uses OpenCTX as an abstraction layer
* Future support planned for additional MCP features
* 支持 MCP 资源 * 与 Sourcegraph 代码智能集成 * 使用 OpenCTX 作为抽象层 * 计划支持更多 MCP 特性

### SpinAI

[SpinAI](https://spinai.dev) is an open-source TypeScript framework for building observable AI agents. The framework provides native MCP compatibility, allowing agents to seamlessly integrate with MCP servers and tools.
[SpinAI](https://spinai.dev) 是一个开源的 TypeScript 框架，用于构建可观察的 AI 代理。该框架提供原生 MCP 兼容性，允许代理无缝集成到 MCP 服务器和工具中。

**Key features:**  **关键特性：**

* Built-in MCP compatibility for AI agents
* Open-source TypeScript framework
* Observable agent architecture
* Native support for MCP tools integration
* 内置 MCP 兼容性，支持 AI 代理 * 开源 TypeScript 框架 * 可观察的代理架构 * 原生支持 MCP 工具集成

### Superinterface  ### 超级接口

[Superinterface](https://superinterface.ai) is AI infrastructure and a developer platform to build in-app AI assistants with support for MCP, interactive components, client-side function calling and more.
[超级接口](https://superinterface.ai) 是 AI 基础设施和开发者平台，用于构建支持 MCP、交互组件、客户端函数调用等功能的应用内 AI 助手。

**Key features:**  **关键特性：**

* Use tools from MCP servers in assistants embedded via React components or script tags
* SSE transport support
* Use any AI model from any AI provider (OpenAI, Anthropic, Ollama, others)
* 使用 MCP 服务器中的工具，通过 React 组件或脚本标签嵌入助手 * SSE 传输支持 * 使用任何 AI 提供商（OpenAI、Anthropic、Ollama 等）的 AI 模型

### TheiaAI/TheiaIDE

[Theia AI](https://eclipsesource.com/blogs/2024/10/07/introducing-theia-ai/) is a framework for building AI-enhanced tools and IDEs. The [AI-powered Theia IDE](https://eclipsesource.com/blogs/2024/10/08/introducting-ai-theia-ide/) is an open and flexible development environment built on Theia AI.
[Theia AI](https://eclipsesource.com/blogs/2024/10/07/introducing-theia-ai/) 是一个用于构建 AI 增强工具和 IDE 的框架。[AI 驱动的 Theia IDE](https://eclipsesource.com/blogs/2024/10/08/introducting-ai-theia-ide/) 是一个基于 Theia AI 的开放和灵活的开发环境。

**Key features:**  **关键特性：**

* **Tool Integration**: Theia AI enables AI agents, including those in the Theia IDE, to utilize MCP servers for seamless tool interaction.
* **Customizable Prompts**: The Theia IDE allows users to define and adapt prompts, dynamically integrating MCP servers for tailored workflows.
* **Custom agents**: The Theia IDE supports creating custom agents that leverage MCP capabilities, enabling users to design dedicated workflows on the fly.
**工具集成**：Theia AI 允许 AI 代理，包括 Theia IDE 中的代理，利用 MCP 服务器实现无缝的工具交互。**可定制提示**：Theia IDE 允许用户定义和调整提示，动态集成 MCP 服务器以实现定制的工作流程。**自定义代理**：Theia IDE 支持创建利用 MCP 功能的自定义代理，使用户能够即时设计专用的工作流程。

Theia AI and Theia IDE's MCP integration provide users with flexibility, making them powerful platforms for exploring and adapting MCP.
Theia AI 和 Theia IDE 的 MCP 集成为用户提供灵活性，使它们成为探索和适应 MCP 的强大平台。

**Learn more:**  **了解更多：**

* [Theia IDE and Theia AI MCP Announcement](https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/)
* [Download the AI-powered Theia IDE](https://theia-ide.org/)
* [Theia IDE 和 Theia AI MCP 公告](https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/) * [下载 AI 驱动的 Theia IDE](https://theia-ide.org/)

### VS Code GitHub Copilot

[VS Code](https://code.visualstudio.com/) integrates MCP with GitHub Copilot through [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode), allowing direct interaction with MCP-provided tools within your agentic coding workflow. Configure servers in Claude Desktop, workspace or user settings, with guided MCP installation and secure handling of keys in input variables to avoid leaking hard-coded keys.
[VS Code](https://code.visualstudio.com/) 通过 [代理模式](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) 将 MCP 与 GitHub Copilot 集成，允许在您的代理编码工作流程中直接与 MCP 提供的工具进行交互。在 Claude Desktop、工作区或用户设置中配置服务器，通过引导式 MCP 安装和输入变量中密钥的安全处理来避免硬编码密钥泄露。

**Key features:**  **关键特性：**

* Support for stdio and server-sent events (SSE) transport
* Per-session selection of tools per agent session for optimal performance
* Easy server debugging with restart commands and output logging
* Tool calls with editable inputs and always-allow toggle
* Integration with existing VS Code extension system to register MCP servers from extensions
* 支持 stdio 和服务器发送事件 (SSE) 传输 * 每个代理会话选择工具以实现最佳性能 * 使用重启命令和输出日志轻松进行服务器调试 * 可编辑输入和始终允许切换的工具调用 * 与现有 VS Code 扩展系统集成，以从扩展中注册 MCP 服务器

### Windsurf Editor  ### 风帆编辑器

[Windsurf Editor](https://codeium.com/windsurf) is an agentic IDE that combines AI assistance with developer workflows. It features an innovative AI Flow system that enables both collaborative and independent AI interactions while maintaining developer control.
[Windsurf 编辑器](https://codeium.com/windsurf) 是一个结合 AI 辅助与开发者工作流程的代理 IDE。它具有创新的 AI 流系统，能够实现协作和独立的人工智能交互，同时保持开发者的控制权。

**Key features:**  **关键特性：**

* Revolutionary AI Flow paradigm for human-AI collaboration
* Intelligent code generation and understanding
* Rich development tools with multi-model support
* 革命性的 AI 流范式，实现人机协作 * 智能代码生成和理解 * 丰富的开发工具，支持多模型

### Witsy

[Witsy](https://github.com/nbonamy/witsy) is an AI desktop assistant, supoorting Anthropic models and MCP servers as LLM tools.
[Witsy](https://github.com/nbonamy/witsy) 是一款 AI 桌面助手，支持 Anthropic 模型和 MCP 服务器作为 LLM 工具。

**Key features:**  **主要功能：**

* Multiple MCP servers support
* Tool integration for executing commands and scripts
* Local server connections for enhanced privacy and security
* Easy-install from Smithery.ai
* Open-source, available for macOS, Windows and Linux
* 多个 MCP 服务器支持 * 工具集成以执行命令和脚本 * 本地服务器连接以增强隐私和安全 * 从 Smithery.ai 易于安装 * 开源，适用于 macOS、Windows 和 Linux

### Zed

[Zed](https://zed.dev/docs/assistant/model-context-protocol) is a high-performance code editor with built-in MCP support, focusing on prompt templates and tool integration.
[Zed](https://zed.dev/docs/assistant/model-context-protocol) 是一款高性能的代码编辑器，内置 MCP 支持，专注于提示模板和工具集成。

**Key features:**  **主要功能：**

* Prompt templates surface as slash commands in the editor
* Tool integration for enhanced coding workflows
* Tight integration with editor features and workspace context
* Does not support MCP resources
* 提示模板以斜杠命令的形式在编辑器中呈现 * 工具集成，增强编码工作流程 * 与编辑器功能和工作区上下文紧密集成 * 不支持 MCP 资源

## Adding MCP support to your application
## 将 MCP 支持添加到您的应用程序

If you've added MCP support to your application, we encourage you to submit a pull request to add it to this list. MCP integration can provide your users with powerful contextual AI capabilities and make your application part of the growing MCP ecosystem.
如果您已将 MCP 支持添加到您的应用程序中，我们鼓励您提交一个拉取请求将其添加到这个列表中。MCP 集成可以为您的用户提供强大的上下文 AI 功能，并使您的应用程序成为不断发展的 MCP 生态系统的一部分。

Benefits of adding MCP support:
添加 MCP 支持的好处：

* Enable users to bring their own context and tools
* Join a growing ecosystem of interoperable AI applications
* Provide users with flexible integration options
* Support local-first AI workflows
* 允许用户携带自己的上下文和工具 * 加入日益壮大的互操作 AI 应用程序生态系统 * 为用户提供灵活的集成选项 * 支持本地优先的 AI 工作流程

To get started with implementing MCP in your application, check out our [Python](https://github.com/modelcontextprotocol/python-sdk) or [TypeScript SDK Documentation](https://github.com/modelcontextprotocol/typescript-sdk)
要开始在您的应用程序中实现 MCP，请查看我们的[Python](https://github.com/modelcontextprotocol/python-sdk)或[TypeScript SDK 文档](https://github.com/modelcontextprotocol/typescript-sdk)

## Updates and corrections
更新和更正

This list is maintained by the community. If you notice any inaccuracies or would like to update information about MCP support in your application, please submit a pull request or [open an issue in our documentation repository](https://github.com/modelcontextprotocol/modelcontextprotocol/issues).
此列表由社区维护。如果您发现任何不准确之处或希望更新您应用程序中 MCP 支持的信息，请提交一个拉取请求或[在我们的文档仓库中打开一个 issue](https://github.com/modelcontextprotocol/modelcontextprotocol/issues)。


# Contributing
Source: https://modelcontextprotocol.io/development/contributing
# 贡献来源: https://modelcontextprotocol.io/development/contributing

How to participate in Model Context Protocol development
如何参与模型上下文协议的开发

We welcome contributions from the community! Please review our [contributing guidelines](https://github.com/modelcontextprotocol/.github/blob/main/CONTRIBUTING.md) for details on how to submit changes.
我们欢迎社区贡献！请查阅我们的[贡献指南](https://github.com/modelcontextprotocol/.github/blob/main/CONTRIBUTING.md)，了解提交更改的详细信息。

All contributors must adhere to our [Code of Conduct](https://github.com/modelcontextprotocol/.github/blob/main/CODE_OF_CONDUCT.md).
所有贡献者都必须遵守我们的[行为准则](https://github.com/modelcontextprotocol/.github/blob/main/CODE_OF_CONDUCT.md)。

For questions and discussions, please use [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions).
如有疑问和讨论，请使用[GitHub 讨论区](https://github.com/orgs/modelcontextprotocol/discussions)。


# Roadmap
Source: https://modelcontextprotocol.io/development/roadmap
# 路线图来源：https://modelcontextprotocol.io/development/roadmap

Our plans for evolving Model Context Protocol
我们对演进模型上下文协议的计划

<Info>Last updated: **2025-03-27**</Info>
最后更新时间：**2025-03-27**

The Model Context Protocol is rapidly evolving. This page outlines our current thinking on key priorities and direction for approximately **the next six months**, though these may change significantly as the project develops. To see what's changed recently, check out the **[specification changelog](/specification/2025-03-26/changelog/)**.
模型上下文协议正在快速发展。本页面概述了我们当前对关键优先事项和未来约**六个月**的方向的思考，尽管随着项目的发展，这些内容可能会发生重大变化。要查看最近的变化，请查看**[规范变更日志](/specification/2025-03-26/changelog/)**。

<Note>The ideas presented here are not commitments—we may solve these challenges differently than described, or some may not materialize at all. This is also not an *exhaustive* list; we may incorporate work that isn't mentioned here.</Note>
此处提出的思想并非承诺——我们可能以不同的方式解决这些挑战，或者其中一些可能根本不会实现。这也不是一个**详尽无遗**的列表；我们可能会纳入此处未提及的工作。

We value community participation! Each section links to relevant discussions where you can learn more and contribute your thoughts.
我们重视社区参与！每个部分都链接到相关的讨论，您可以在那里了解更多信息并贡献您的想法。

For a technical view of our standardization process, visit the [Standards Track](https://github.com/orgs/modelcontextprotocol/projects/2/views/2) on GitHub, which tracks how proposals progress toward inclusion in the official [MCP specification](https://spec.modelcontextprotocol.io).
想了解我们标准化流程的技术视角，请访问 GitHub 上的[标准跟踪](https://github.com/orgs/modelcontextprotocol/projects/2/views/2)，它跟踪提案如何进展到官方[MCP 规范](https://spec.modelcontextprotocol.io)的纳入。

## Validation  ## 验证

To foster a robust developer ecosystem, we plan to invest in:
为培养一个强大的开发者生态系统，我们计划投资于：

* **Reference Client Implementations**: demonstrating protocol features with high-quality AI applications
* **Compliance Test Suites**: automated verification that clients, servers, and SDKs properly implement the specification
**参考客户端实现**：使用高质量 AI 应用展示协议功能 **合规测试套件**：自动验证客户端、服务器和 SDK 正确实现规范

These tools will help developers confidently implement MCP while ensuring consistent behavior across the ecosystem.
这些工具将帮助开发者自信地实现 MCP，同时确保整个生态系统的行为一致性。

## Registry  ## 注册表

For MCP to reach its full potential, we need streamlined ways to distribute and discover MCP servers.
为了让 MCP 充分发挥其潜力，我们需要简化的方式来分发和发现 MCP 服务器。

We plan to develop an [**MCP Registry**](https://github.com/orgs/modelcontextprotocol/discussions/159) that will enable centralized server discovery and metadata. This registry will primarily function as an API layer that third-party marketplaces and discovery services can build upon.
我们计划开发一个[**MCP 注册表**](https://github.com/orgs/modelcontextprotocol/discussions/159)，该注册表将实现集中式服务器发现和元数据。此注册表将主要作为一个 API 层，第三方市场和服务可以发现并在此基础上构建。

## Agents  ## 代理

As MCP increasingly becomes part of agentic workflows, we're exploring [improvements](https://github.com/modelcontextprotocol/specification/discussions/111) such as:
随着 MCP 越来越多地成为代理工作流程的一部分，我们正在探索以下改进：

* **[Agent Graphs](https://github.com/modelcontextprotocol/specification/discussions/94)**: enabling complex agent topologies through namespacing and graph-aware communication patterns
* **Interactive Workflows**: improving human-in-the-loop experiences with granular permissioning, standardized interaction patterns, and [ways to directly communicate](https://github.com/modelcontextprotocol/specification/issues/97) with the end user
* **[代理图](https://github.com/modelcontextprotocol/specification/discussions/94)**：通过命名空间和图感知通信模式实现复杂的代理拓扑 * **交互式工作流程**：通过细粒度权限、标准化的交互模式和[直接与最终用户沟通的方式](https://github.com/modelcontextprotocol/specification/issues/97)来改善人机交互体验

## Multimodality  多模态

Supporting the full spectrum of AI capabilities in MCP, including:
支持 MCP 中 AI 能力的全谱系，包括：

* **Additional Modalities**: video and other media types
* **[Streaming](https://github.com/modelcontextprotocol/specification/issues/117)**: multipart, chunked messages, and bidirectional communication for interactive experiences
* **附加模态**：视频和其他媒体类型 * **[流式传输](https://github.com/modelcontextprotocol/specification/issues/117)**：多部分、分块消息和双向通信以实现交互式体验

## Governance  ## 治理

We're implementing governance structures that prioritize:
我们正在实施优先考虑治理结构的：

* **Community-Led Development**: fostering a collaborative ecosystem where community members and AI developers can all participate in MCP's evolution, ensuring it serves diverse applications and use cases
* **Transparent Standardization**: establishing clear processes for contributing to the specification, while exploring formal standardization via industry bodies
* **社区主导开发**：培育一个社区成员和 AI 开发者都能参与的协作生态系统，确保 MCP 服务于多样化的应用和用例 * **透明标准化**：建立明确的贡献规范流程，同时探索通过行业机构进行正式标准化

## Get Involved  ## 参与其中

We welcome your contributions to MCP's future! Join our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to share ideas, provide feedback, or participate in the development process.
我们欢迎您为 MCP 的未来做出贡献！加入我们的[GitHub 讨论](https://github.com/orgs/modelcontextprotocol/discussions)，分享想法、提供反馈或参与开发过程。


# What's New
Source: https://modelcontextprotocol.io/development/updates
# 新功能来源：https://modelcontextprotocol.io/development/updates

The latest updates and improvements to MCP
MCP 的最新更新和改进

<Update label="2025-04-10" description="Java SDK 0.9.0 released">
  * Version [0.9.0](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.9.0) of the MCP Java SDK has been released.
  * Refactored logging system to use exchange mechanism
  * Custom Context Paths
  * Server Instructions
  * CallToolResult Enhancement
</Update>
 * MCP Java SDK [0.9.0](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.9.0)版本已发布。 * 重构日志系统以使用交换机制 * 自定义上下文路径 * 服务器说明 * CallToolResult 增强 

<Update label="2025-03-26" description="Kotlin SDK 0.4.0 released">
  * Fix issues and cleanup API
  * Added binary compatibility tracking to avoid breaking changes
  * Drop jdk requirements to JDK8
  * Added Claude Desktop integration with sample
  * The full changelog can be found here: [https://github.com/modelcontextprotocol/kotlin-sdk/releases/tag/0.4.0](https://github.com/modelcontextprotocol/kotlin-sdk/releases/tag/0.4.0)
</Update>
 * 修复问题和清理 API * 添加二进制兼容性跟踪以避免破坏性更改 * 降低 JDK 要求至 JDK8 * 添加 Claude 桌面集成示例 * 完整的变更日志请见此处：[https://github.com/modelcontextprotocol/kotlin-sdk/releases/tag/0.4.0](https://github.com/modelcontextprotocol/kotlin-sdk/releases/tag/0.4.0) 

<Update label="2025-03-26" description="Java SDK 0.8.1 released">
  * Version [0.8.1](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.8.1) of the MCP Java SDK has been released,
    providing important bug fixes.
</Update>
 * MCP Java SDK 的 [0.8.1](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.8.1) 版本已发布，提供了重要的错误修复。 

<Update label="2025-03-24" description="C# SDK released">
  * We are exited to announce the availability of the MCP
    [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk/) developed by
    [Peder Holdgaard Pedersen](http://github.com/PederHP) and Microsoft. This joins our growing
    list of supported languages. The C# SDK is also available as
    [NuGet package](https://www.nuget.org/packages/ModelContextProtocol)
  * Python SDK 1.5.0 was released with multiple fixes and improvements.
</Update>
 * 我们很高兴地宣布由 [Peder Holdgaard Pedersen](http://github.com/PederHP) 和 Microsoft 开发的 MCP [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk/) 现已可用。这增加了我们支持的语言列表。C# SDK 也作为 [NuGet 包](https://www.nuget.org/packages/ModelContextProtocol) 提供。* Python SDK 1.5.0 已发布，包含多个修复和改进。 

<Update label="2025-03-21" description="Java SDK 0.8.0 released">
  * Version [0.8.0](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.8.0) of the MCP Java SDK has been released,
    delivering important session management improvements and bug fixes.
</Update>
 * MCP Java SDK 的 [0.8.0](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.8.0) 版本已发布，提供了重要的会话管理改进和错误修复。 

<Update label="2025-03-10" description="Typescript SDK release">
  * Typescript SDK 1.7.0 was released with multiple fixes and improvements.
</Update>
 * Typescript SDK 1.7.0 已发布，包含多个修复和改进。 

<Update label="2025-02-14" description="Java SDK released">
  * We're excited to announce that the Java SDK developed by Spring AI at VMware Tanzu is now
    the official [Java SDK](https://github.com/modelcontextprotocol/java-sdk) for MCP.
    This joins our existing Kotlin SDK in our growing list of supported languages.
    The Spring AI team will maintain the SDK as an integral part of the Model Context Protocol
    organization. We're thrilled to welcome them to the MCP community!
</Update>
 * 我们非常高兴地宣布，由 Spring AI 在 VMware Tanzu 开发的 Java SDK 现在成为 MCP 的官方[Java SDK](https://github.com/modelcontextprotocol/java-sdk)。这使我们支持的语言列表进一步增长。Spring AI 团队将作为 Model Context Protocol 组织的一部分维护此 SDK。我们非常高兴欢迎他们加入 MCP 社区！ 

<Update label="2025-01-27" description="Python SDK 1.2.1">
  * Version [1.2.1](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.2.1) of the MCP Python SDK has been released,
    delivering important stability improvements and bug fixes.
</Update>
 * MCP Python SDK 的[1.2.1](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.2.1)版本已发布，提供了重要的稳定性改进和错误修复。 

<Update label="2025-01-18" description="SDK and Server Improvements">
  * Simplified, express-like API in the [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
  * Added 8 new clients to the [clients page](https://modelcontextprotocol.io/clients)
</Update>
 * 简化，类似表达式的 API 在[TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)中 * 已将 8 个新客户端添加到[客户端页面](https://modelcontextprotocol.io/clients) 

<Update label="2025-01-03" description="SDK and Server Improvements">
  * FastMCP API in the [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  * Dockerized MCP servers in the [servers repo](https://github.com/modelcontextprotocol/servers)
</Update>
<更新标签="2025-01-03" 描述="SDK 和服务器改进"> * FastMCP API 在[Python SDK](https://github.com/modelcontextprotocol/python-sdk)中 * Docker 化的 MCP 服务器在[servers 仓库](https://github.com/modelcontextprotocol/servers)中 

<Update label="2024-12-21" description="Kotlin SDK released">
  * Jetbrains released a Kotlin SDK for MCP!
  * For a sample MCP Kotlin server, check out [this repository](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/kotlin-mcp-server)
</Update>
<更新标签="2024-12-21" 描述="发布 Kotlin SDK"> * JetBrains 发布了 MCP 的 Kotlin SDK！ * 欲查看 MCP Kotlin 服务器的示例，请参阅[此仓库](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/kotlin-mcp-server) 


# Core architecture
Source: https://modelcontextprotocol.io/docs/concepts/architecture
# 核心架构 来源：https://modelcontextprotocol.io/docs/concepts/architecture

Understand how MCP connects clients, servers, and LLMs
了解 MCP 如何连接客户端、服务器和LLMs

The Model Context Protocol (MCP) is built on a flexible, extensible architecture that enables seamless communication between LLM applications and integrations. This document covers the core architectural components and concepts.
模型上下文协议（MCP）基于灵活、可扩展的架构，能够实现应用程序和集成之间的无缝通信。本文件涵盖了核心架构组件和概念。

## Overview  ## 概述

MCP follows a client-server architecture where:
MCP 采用客户端-服务器架构，其中：

* **Hosts** are LLM applications (like Claude Desktop or IDEs) that initiate connections
* **Clients** maintain 1:1 connections with servers, inside the host application
* **Servers** provide context, tools, and prompts to clients
* **主机**是应用程序（如 Claude 桌面或 IDE）* **客户端**与主机应用程序中的服务器保持 1:1 连接* **服务器**为客户端提供上下文、工具和提示

```mermaid
flowchart LR
    subgraph "Host"
        client1[MCP Client]
        client2[MCP Client]
    end
    subgraph "Server Process"
        server1[MCP Server]
    end
    subgraph "Server Process"
        server2[MCP Server]
    end
```mermaid 流程图 LR 子图 "主机" client1[MC 客户端] client2[MC 客户端] end 子图 "服务器进程" server1[MC 服务器] end 子图 "服务器进程" server2[MC 服务器] end

    client1 <-->|Transport Layer| server1
    client2 <-->|Transport Layer| server2
```
client1 <-->|传输层| server1 client2 <-->|传输层| server2

## Core components  ## 核心组件

### Protocol layer  ### 协议层

The protocol layer handles message framing, request/response linking, and high-level communication patterns.
协议层处理消息封装、请求/响应链接和高级通信模式。

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    class Protocol<Request, Notification, Result> {
        // Handle incoming requests
        setRequestHandler<T>(schema: T, handler: (request: T, extra: RequestHandlerExtra) => Promise<Result>): void
  ```typescript class Protocol { // 处理传入的请求 setRequestHandler(schema: T, handler: (request: T, extra: RequestHandlerExtra) => Promise): void

        // Handle incoming notifications
        setNotificationHandler<T>(schema: T, handler: (notification: T) => Promise<void>): void
// 处理传入的通知 setNotificationHandler(schema: T, handler: (notification: T) => Promise): void

        // Send requests and await responses
        request<T>(request: Request, schema: T, options?: RequestOptions): Promise<T>
// 发送请求并等待响应 request(request: Request, schema: T, options?: RequestOptions): Promise

        // Send one-way notifications
        notification(notification: Notification): Promise<void>
    }
    ```
  </Tab>
// 发送单向通知 notification(notification: Notification): Promise }

  <Tab title="Python">
    ```python
    class Session(BaseSession[RequestT, NotificationT, ResultT]):
        async def send_request(
            self,
            request: RequestT,
            result_type: type[Result]
        ) -> Result:
            """Send request and wait for response. Raises McpError if response contains error."""
            # Request handling implementation
 ```python class Session(BaseSession[RequestT, NotificationT, ResultT]): async def send_request( self, request: RequestT, result_type: type[Result] ) -> Result: """发送请求并等待响应。如果响应包含错误，则引发 McpError。""" # 请求处理实现

        async def send_notification(
            self,
            notification: NotificationT
        ) -> None:
            """Send one-way notification that doesn't expect response."""
            # Notification handling implementation
async def send_notification( self, notification: NotificationT ) -> None: """发送不需要响应的单向通知。""" # 通知处理实现

        async def _received_request(
            self,
            responder: RequestResponder[ReceiveRequestT, ResultT]
        ) -> None:
            """Handle incoming request from other side."""
            # Request handling implementation
async def _received_request( self, responder: RequestResponder[ReceiveRequestT, ResultT] ) -> None: """处理来自另一侧的请求。""" # 请求处理实现

        async def _received_notification(
            self,
            notification: ReceiveNotificationT
        ) -> None:
            """Handle incoming notification from other side."""
            # Notification handling implementation
    ```
  </Tab>
</Tabs>
async def _received_notification(self, notification: ReceiveNotificationT) -> None: """处理来自另一侧的传入通知。""" # 通知处理实现 ```  

Key classes include:  关键类包括：

* `Protocol`
* `Client`
* `Server`
* `协议` * `客户端` * `服务器`

### Transport layer  ### 传输层

The transport layer handles the actual communication between clients and servers. MCP supports multiple transport mechanisms:
传输层处理客户端和服务器之间的实际通信。MCP 支持多种传输机制：

1. **Stdio transport**
   * Uses standard input/output for communication
   * Ideal for local processes
1. **标准输入输出传输** * 使用标准输入/输出进行通信 * 适用于本地进程

2. **HTTP with SSE transport**
   * Uses Server-Sent Events for server-to-client messages
   * HTTP POST for client-to-server messages
2. **带有 SSE 的 HTTP 传输** * 使用服务器发送事件进行服务器到客户端的消息 * 使用 HTTP POST 进行客户端到服务器的消息

All transports use [JSON-RPC](https://www.jsonrpc.org/) 2.0 to exchange messages. See the [specification](/specification/) for detailed information about the Model Context Protocol message format.
所有传输都使用[JSON-RPC](https://www.jsonrpc.org/) 2.0 进行消息交换。请参阅[规范](/specification/)以获取有关模型上下文协议消息格式的详细信息。

### Message types  消息类型

MCP has these main types of messages:
MCP 具有以下主要消息类型：

1. **Requests** expect a response from the other side:
   ```typescript
   interface Request {
     method: string;
     params?: { ... };
   }
   ```
1. **请求**期望从另一端获得响应：```typescript interface Request { method: string; params?: { ... }; } ```

2. **Results** are successful responses to requests:
   ```typescript
   interface Result {
     [key: string]: unknown;
   }
   ```
2. **结果**是针对请求的成功响应：```typescript interface Result { [key: string]: unknown; } ```

3. **Errors** indicate that a request failed:
   ```typescript
   interface Error {
     code: number;
     message: string;
     data?: unknown;
   }
   ```
3. **错误**表示请求失败：```typescript interface Error { code: number; message: string; data?: unknown; } ```

4. **Notifications** are one-way messages that don't expect a response:
   ```typescript
   interface Notification {
     method: string;
     params?: { ... };
   }
   ```
4. **通知**是单向消息，不需要响应：```typescript interface Notification { method: string; params?: { ... }; } ```

## Connection lifecycle  ## 连接生命周期

### 1. Initialization  ### 1. 初始化

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Client->>Server: initialize request
    Server->>Client: initialize response
    Client->>Server: initialized notification
客户端->>服务器: 初始化请求 服务器->>客户端: 初始化响应 客户端->>服务器: 初始化通知

    Note over Client,Server: Connection ready for use
```
Note over 客户端,服务器: 连接就绪可供使用

1. Client sends `initialize` request with protocol version and capabilities
2. Server responds with its protocol version and capabilities
3. Client sends `initialized` notification as acknowledgment
4. Normal message exchange begins
1. 客户端发送带有协议版本和功能的 `initialize` 请求 2. 服务器响应其协议版本和功能 3. 客户端发送 `initialized` 通知作为确认 4. 正常消息交换开始

### 2. Message exchange  ### 2. 消息交换

After initialization, the following patterns are supported:
初始化后，支持以下模式：

* **Request-Response**: Client or server sends requests, the other responds
* **Notifications**: Either party sends one-way messages
* **请求-响应**：客户端或服务器发送请求，另一方响应 * **通知**：任一方发送单向消息

### 3. Termination  ### 3. 终止

Either party can terminate the connection:
任何一方均可终止连接：

* Clean shutdown via `close()`
* Transport disconnection
* Error conditions
* 通过 `close()` 进行干净关闭 * 传输断开 * 错误条件

## Error handling  ## 错误处理

MCP defines these standard error codes:
MCP 定义了这些标准错误代码：

```typescript
enum ErrorCode {
  // Standard JSON-RPC error codes
  ParseError = -32700,
  InvalidRequest = -32600,
  MethodNotFound = -32601,
  InvalidParams = -32602,
  InternalError = -32603
}
```
```typescript 枚举 ErrorCode { // 标准 JSON-RPC 错误代码 ParseError = -32700, InvalidRequest = -32600, MethodNotFound = -32601, InvalidParams = -32602, InternalError = -32603 } ```

SDKs and applications can define their own error codes above -32000.
SDK 和应用程序可以定义它们自己的错误代码，高于-32000。

Errors are propagated through:
错误通过以下方式传播：

* Error responses to requests
* Error events on transports
* Protocol-level error handlers
* 请求的错误响应 * 传输上的错误事件 * 协议级别的错误处理器

## Implementation example
实现示例

Here's a basic example of implementing an MCP server:
这里是一个实现 MCP 服务器的基本示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    import { Server } from "@modelcontextprotocol/sdk/server/index.js";
    import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {
        resources: {}
      }
    });

    // Handle requests
    server.setRequestHandler(ListResourcesRequestSchema, async () => {
      return {
        resources: [
          {
            uri: "example://resource",
            name: "Example Resource"
          }
        ]
      };
    });
// 处理请求 server.setRequestHandler(ListResourcesRequestSchema, async () => { return { resources: [ { uri: "example://resource", name: "Example Resource" } ] }; });

    // Connect transport
    const transport = new StdioServerTransport();
    await server.connect(transport);
    ```
  </Tab>
// 连接传输 const transport = new StdioServerTransport(); await server.connect(transport); ``` 

  <Tab title="Python">
    ```python
    import asyncio
    import mcp.types as types
    from mcp.server import Server
    from mcp.server.stdio import stdio_server

    app = Server("example-server")

    @app.list_resources()
    async def list_resources() -> list[types.Resource]:
        return [
            types.Resource(
                uri="example://resource",
                name="Example Resource"
            )
        ]
@app.list_resources() async def list_resources() -> list[types.Resource]: return [types.Resource(uri="example://resource", name="Example Resource")]

    async def main():
        async with stdio_server() as streams:
            await app.run(
                streams[0],
                streams[1],
                app.create_initialization_options()
            )
async def main(): async with stdio_server() as streams: await app.run(streams[0], streams[1], app.create_initialization_options())

    if __name__ == "__main__":
        asyncio.run(main())
    ```
  </Tab>
</Tabs>
if __name__ == "__main__": asyncio.run(main())

## Best practices  ## 最佳实践

### Transport selection  ### 交通选择

1. **Local communication**
   * Use stdio transport for local processes
   * Efficient for same-machine communication
   * Simple process management
1. **本地通信** * 使用 stdio 传输用于本地进程 * 适用于同一机器通信 * 简单的过程管理

2. **Remote communication**
   * Use SSE for scenarios requiring HTTP compatibility
   * Consider security implications including authentication and authorization
2. **远程通信** * 在需要 HTTP 兼容性的场景中使用 SSE * 考虑安全影响，包括身份验证和授权

### Message handling  ### 消息处理

1. **Request processing**
   * Validate inputs thoroughly
   * Use type-safe schemas
   * Handle errors gracefully
   * Implement timeouts
1. **请求处理** * 严格验证输入 * 使用类型安全的模式 * 优雅地处理错误 * 实现超时

2. **Progress reporting**
   * Use progress tokens for long operations
   * Report progress incrementally
   * Include total progress when known
2. **进度报告** * 使用进度令牌进行长时间操作 * 逐步报告进度 * 当已知时包含总进度

3. **Error management**
   * Use appropriate error codes
   * Include helpful error messages
   * Clean up resources on errors
3. **错误管理** * 使用适当的错误代码 * 包含有用的错误信息 * 在错误时清理资源

## Security considerations
## 安全考虑

1. **Transport security**
   * Use TLS for remote connections
   * Validate connection origins
   * Implement authentication when needed
1. **运输安全** * 使用 TLS 进行远程连接 * 验证连接来源 * 需要时实施身份验证

2. **Message validation**
   * Validate all incoming messages
   * Sanitize inputs
   * Check message size limits
   * Verify JSON-RPC format
2. **消息验证** * 验证所有传入消息 * 清理输入 * 检查消息大小限制 * 验证 JSON-RPC 格式

3. **Resource protection**
   * Implement access controls
   * Validate resource paths
   * Monitor resource usage
   * Rate limit requests
3. **资源保护** * 实施访问控制 * 验证资源路径 * 监控资源使用 * 限制请求速率

4. **Error handling**
   * Don't leak sensitive information
   * Log security-relevant errors
   * Implement proper cleanup
   * Handle DoS scenarios
4. **错误处理** * 不要泄露敏感信息 * 记录安全相关错误 * 实施适当的清理 * 处理拒绝服务攻击场景

## Debugging and monitoring
调试与监控

1. **Logging**
   * Log protocol events
   * Track message flow
   * Monitor performance
   * Record errors
1. **日志记录** * 记录协议事件 * 跟踪消息流 * 监控性能 * 记录错误

2. **Diagnostics**
   * Implement health checks
   * Monitor connection state
   * Track resource usage
   * Profile performance
2. **诊断** * 实施健康检查 * 监控连接状态 * 跟踪资源使用 * 性能分析

3. **Testing**
   * Test different transports
   * Verify error handling
   * Check edge cases
   * Load test servers
3. **测试** * 测试不同传输方式 * 验证错误处理 * 检查边缘情况 * 压力测试服务器


# Prompts
Source: https://modelcontextprotocol.io/docs/concepts/prompts
# 源地址: https://modelcontextprotocol.io/docs/concepts/prompts

Create reusable prompt templates and workflows
创建可重用的提示模板和工作流程

Prompts enable servers to define reusable prompt templates and workflows that clients can easily surface to users and LLMs. They provide a powerful way to standardize and share common LLM interactions.
提示允许服务器定义可重用的提示模板和工作流程，客户端可以轻松地向用户展示，并提供了一种强大的标准化和共享常见交互的方式。LLMs。它们提供了一种强大的标准化和共享常见交互的方式。

<Note>
  Prompts are designed to be **user-controlled**, meaning they are exposed from servers to clients with the intention of the user being able to explicitly select them for use.
</Note>
<注意> 提示旨在由 **用户控制**，这意味着它们从服务器暴露给客户端，目的是让用户能够明确选择它们进行使用。

## Overview  ## 概述

Prompts in MCP are predefined templates that can:
MCP 中的提示是预定义的模板，可以：

* Accept dynamic arguments
* Include context from resources
* Chain multiple interactions
* Guide specific workflows
* Surface as UI elements (like slash commands)
* 接受动态参数 * 包含资源上下文 * 连接多个交互 * 指导特定工作流程 * 以 UI 元素（如 slash 命令）的形式呈现

## Prompt structure  ## 提示结构

Each prompt is defined with:
每个提示都由以下定义：

```typescript
{
  name: string;              // Unique identifier for the prompt
  description?: string;      // Human-readable description
  arguments?: [              // Optional list of arguments
    {
      name: string;          // Argument identifier
      description?: string;  // Argument description
      required?: boolean;    // Whether argument is required
    }
  ]
}
```
```typescript { name: string; // 唯一标识符 for the prompt description?: string; // 可读性描述 arguments?: [ // 可选参数列表 { name: string; // 参数标识符 description?: string; // 参数描述 required?: boolean; // 参数是否必需 } ] } ```

## Discovering prompts  ## 发现提示

Clients can discover available prompts through the `prompts/list` endpoint:
客户可以通过 `prompts/list` 端点发现可用的提示：

```typescript
// Request
{
  method: "prompts/list"
}
```typescript // 请求 { method: "prompts/list" }

// Response
{
  prompts: [
    {
      name: "analyze-code",
      description: "Analyze code for potential improvements",
      arguments: [
        {
          name: "language",
          description: "Programming language",
          required: true
        }
      ]
    }
  ]
}
```
// 响应 { prompts: [ { name: "analyze-code", description: "分析代码以寻找潜在改进", arguments: [ { name: "language", description: "编程语言", required: true } ] } ] } ```

## Using prompts  ## 使用提示

To use a prompt, clients make a `prompts/get` request:
要使用提示，客户端需要发送一个 `prompts/get` 请求：

````typescript
// Request
{
  method: "prompts/get",
  params: {
    name: "analyze-code",
    arguments: {
      language: "python"
    }
  }
}
````typescript // 请求 { method: "prompts/get", params: { name: "analyze-code", arguments: { language: "python" } } }

// Response
{
  description: "Analyze Python code for potential improvements",
  messages: [
    {
      role: "user",
      content: {
        type: "text",
        text: "Please analyze the following Python code for potential improvements:\n\n```python\ndef calculate_sum(numbers):\n    total = 0\n    for num in numbers:\n        total = total + num\n    return total\n\nresult = calculate_sum([1, 2, 3, 4, 5])\nprint(result)\n```"
      }
    }
  ]
}
````
// 响应 { description: "分析 Python 代码以查找潜在改进", messages: [ { role: "user", content: { type: "text", text: "请分析以下 Python 代码以查找潜在改进：\n\n```python\ndef calculate_sum(numbers):\n total = 0\n for num in numbers:\n total = total + num\n return total\n\nresult = calculate_sum([1, 2, 3, 4, 5])\nprint(result)\n```" } } ] } ````

## Dynamic prompts  ## 动态提示

Prompts can be dynamic and include:
提示可以是动态的，并包括：

### Embedded resource context
### 嵌入资源上下文

```json
{
  "name": "analyze-project",
  "description": "Analyze project logs and code",
  "arguments": [
    {
      "name": "timeframe",
      "description": "Time period to analyze logs",
      "required": true
    },
    {
      "name": "fileUri",
      "description": "URI of code file to review",
      "required": true
    }
  ]
}
```
```json { "name": "analyze-project", "description": "分析项目日志和代码", "arguments": [ { "name": "timeframe", "description": "分析日志的时间段", "required": true }, { "name": "fileUri", "description": "要审查的代码文件的 URI", "required": true } ] } ```

When handling the `prompts/get` request:
当处理 `prompts/get` 请求时：

```json
{
  "messages": [
    {
      "role": "user",
      "content": {
        "type": "text",
        "text": "Analyze these system logs and the code file for any issues:"
      }
    },
    {
      "role": "user",
      "content": {
        "type": "resource",
        "resource": {
          "uri": "logs://recent?timeframe=1h",
          "text": "[2024-03-14 15:32:11] ERROR: Connection timeout in network.py:127\n[2024-03-14 15:32:15] WARN: Retrying connection (attempt 2/3)\n[2024-03-14 15:32:20] ERROR: Max retries exceeded",
          "mimeType": "text/plain"
        }
      }
    },
    {
      "role": "user",
      "content": {
        "type": "resource",
        "resource": {
          "uri": "file:///path/to/code.py",
          "text": "def connect_to_service(timeout=30):\n    retries = 3\n    for attempt in range(retries):\n        try:\n            return establish_connection(timeout)\n        except TimeoutError:\n            if attempt == retries - 1:\n                raise\n            time.sleep(5)\n\ndef establish_connection(timeout):\n    # Connection implementation\n    pass",
          "mimeType": "text/x-python"
        }
      }
    }
  ]
}
```
```json { "messages": [ { "role": "user", "content": { "type": "text", "text": "分析这些系统日志和代码文件中的任何问题：" } }, { "role": "user", "content": { "type": "resource", "resource": { "uri": "logs://recent?timeframe=1h", "text": "[2024-03-14 15:32:11] ERROR: 网络连接超时 in network.py:127\n[2024-03-14 15:32:15] WARN: 正在重试连接 (尝试 2/3)\n[2024-03-14 15:32:20] ERROR: 超过最大重试次数", "mimeType": "text/plain" } } }, { "role": "user", "content": { "type": "resource", "resource": { "uri": "file:///path/to/code.py", "text": "def connect_to_service(timeout=30):\n retries = 3\n for attempt in range(retries):\n try:\n return establish_connection(timeout)\n except TimeoutError:\n if attempt == retries - 1:\n raise\n time.sleep(5)\n\ndef establish_connection(timeout):\n # 连接实现\n pass", "mimeType": "text/x-python" } } } ] } ```

### Multi-step workflows  ### 多步骤工作流程

```typescript
const debugWorkflow = {
  name: "debug-error",
  async getMessages(error: string) {
    return [
      {
        role: "user",
        content: {
          type: "text",
          text: `Here's an error I'm seeing: ${error}`
        }
      },
      {
        role: "assistant",
        content: {
          type: "text",
          text: "I'll help analyze this error. What have you tried so far?"
        }
      },
      {
        role: "user",
        content: {
          type: "text",
          text: "I've tried restarting the service, but the error persists."
        }
      }
    ];
  }
};
```

## Example implementation
## 示例实现

Here's a complete example of implementing prompts in an MCP server:
这里是一个在 MCP 服务器中实现提示的完整示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    import { Server } from "@modelcontextprotocol/sdk/server";
    import {
      ListPromptsRequestSchema,
      GetPromptRequestSchema
    } from "@modelcontextprotocol/sdk/types";

    const PROMPTS = {
      "git-commit": {
        name: "git-commit",
        description: "Generate a Git commit message",
        arguments: [
          {
            name: "changes",
            description: "Git diff or description of changes",
            required: true
          }
        ]
      },
      "explain-code": {
        name: "explain-code",
        description: "Explain how code works",
        arguments: [
          {
            name: "code",
            description: "Code to explain",
            required: true
          },
          {
            name: "language",
            description: "Programming language",
            required: false
          }
        ]
      }
    };

    const server = new Server({
      name: "example-prompts-server",
      version: "1.0.0"
    }, {
      capabilities: {
        prompts: {}
      }
    });

    // List available prompts
    server.setRequestHandler(ListPromptsRequestSchema, async () => {
      return {
        prompts: Object.values(PROMPTS)
      };
    });

    // Get specific prompt
    server.setRequestHandler(GetPromptRequestSchema, async (request) => {
      const prompt = PROMPTS[request.params.name];
      if (!prompt) {
        throw new Error(`Prompt not found: ${request.params.name}`);
      }

      if (request.params.name === "git-commit") {
        return {
          messages: [
            {
              role: "user",
              content: {
                type: "text",
                text: `Generate a concise but descriptive commit message for these changes:\n\n${request.params.arguments?.changes}`
              }
            }
          ]
        };
      }
if (request.params.name === "git-commit") { return { messages: [ { role: "user", content: { type: "text", text: `生成一个简洁但描述性的提交信息，用于以下更改：\n\n${request.params.arguments?.changes}` } } ] }; }

      if (request.params.name === "explain-code") {
        const language = request.params.arguments?.language || "Unknown";
        return {
          messages: [
            {
              role: "user",
              content: {
                type: "text",
                text: `Explain how this ${language} code works:\n\n${request.params.arguments?.code}`
              }
            }
          ]
        };
      }
if (request.params.name === "explain-code") { const language = request.params.arguments?.language || "Unknown"; return { messages: [ { role: "user", content: { type: "text", text: `解释以下 ${language} 代码的工作原理：\n\n${request.params.arguments?.code}` } } ] }; }

      throw new Error("Prompt implementation not found");
    });
    ```
  </Tab>
throw new Error("提示实现未找到"); });

  <Tab title="Python">
    ```python
    from mcp.server import Server
    import mcp.types as types

    # Define available prompts
    PROMPTS = {
        "git-commit": types.Prompt(
            name="git-commit",
            description="Generate a Git commit message",
            arguments=[
                types.PromptArgument(
                    name="changes",
                    description="Git diff or description of changes",
                    required=True
                )
            ],
        ),
        "explain-code": types.Prompt(
            name="explain-code",
            description="Explain how code works",
            arguments=[
                types.PromptArgument(
                    name="code",
                    description="Code to explain",
                    required=True
                ),
                types.PromptArgument(
                    name="language",
                    description="Programming language",
                    required=False
                )
            ],
        )
    }
# 定义可用的提示 PROMPTS = { "git-commit": types.Prompt(名称="git-commit", 描述="生成 Git 提交信息", 参数=[types.PromptArgument(名称="changes", 描述="Git 差分或更改描述", 必选=True)]), "explain-code": types.Prompt(名称="explain-code", 描述="解释代码如何工作", 参数=[types.PromptArgument(名称="code", 描述="要解释的代码", 必选=True), types.PromptArgument(名称="language", 描述="编程语言", 必选=False)]), }

    # Initialize server
    app = Server("example-prompts-server")
# 初始化服务器应用 app = Server("example-prompts-server")

    @app.list_prompts()
    async def list_prompts() -> list[types.Prompt]:
        return list(PROMPTS.values())
# @app.list_prompts() async def list_prompts() -> list[types.Prompt]: return list(PROMPTS.values())

    @app.get_prompt()
    async def get_prompt(
        name: str, arguments: dict[str, str] | None = None
    ) -> types.GetPromptResult:
        if name not in PROMPTS:
            raise ValueError(f"Prompt not found: {name}")
# @app.get_prompt() async def get_prompt(名称: str, 参数: dict[str, str] | None = None) -> types.GetPromptResult: if name not in PROMPTS: raise ValueError(f"提示未找到: {name}")

        if name == "git-commit":
            changes = arguments.get("changes") if arguments else ""
            return types.GetPromptResult(
                messages=[
                    types.PromptMessage(
                        role="user",
                        content=types.TextContent(
                            type="text",
                            text=f"Generate a concise but descriptive commit message "
                            f"for these changes:\n\n{changes}"
                        )
                    )
                ]
            )
如果 name == "git-commit": changes = arguments.get("changes") if arguments else "" return types.GetPromptResult( messages=[ types.PromptMessage( role="user", content=types.TextContent( type="text", text=f"生成一个简洁但描述性的提交信息，用于以下更改：\n\n{changes}" ) ) ] )

        if name == "explain-code":
            code = arguments.get("code") if arguments else ""
            language = arguments.get("language", "Unknown") if arguments else "Unknown"
            return types.GetPromptResult(
                messages=[
                    types.PromptMessage(
                        role="user",
                        content=types.TextContent(
                            type="text",
                            text=f"Explain how this {language} code works:\n\n{code}"
                        )
                    )
                ]
            )
如果 name == "explain-code": code = arguments.get("code") if arguments else "" language = arguments.get("language", "Unknown") if arguments else "Unknown" return types.GetPromptResult( messages=[ types.PromptMessage( role="user", content=types.TextContent( type="text", text=f"解释这段 {language} 代码是如何工作的：\n\n{code}" ) ) ] )

        raise ValueError("Prompt implementation not found")
    ```
  </Tab>
</Tabs>

## Best practices  ## 最佳实践

When implementing prompts:
当实现提示时：

1. Use clear, descriptive prompt names
2. Provide detailed descriptions for prompts and arguments
3. Validate all required arguments
4. Handle missing arguments gracefully
5. Consider versioning for prompt templates
6. Cache dynamic content when appropriate
7. Implement error handling
8. Document expected argument formats
9. Consider prompt composability
10. Test prompts with various inputs
1. 使用清晰、描述性的提示名称 2. 为提示和参数提供详细描述 3. 验证所有必需参数 4. 优雅地处理缺失参数 5. 考虑提示模板的版本控制 6. 在适当的时候缓存动态内容 7. 实现错误处理 8. 记录预期的参数格式 9. 考虑提示的可组合性 10. 使用各种输入测试提示

## UI integration  ## UI 集成

Prompts can be surfaced in client UIs as:
提示可以以以下方式在客户端 UI 中呈现：

* Slash commands
* Quick actions
* Context menu items
* Command palette entries
* Guided workflows
* Interactive forms
* 命令行 * 快速操作 * 右键菜单项 * 命令面板条目 * 指导式工作流程 * 交互式表单

## Updates and changes  ## 更新和变更

Servers can notify clients about prompt changes:
服务器可以通知客户端关于提示变更：

1. Server capability: `prompts.listChanged`
2. Notification: `notifications/prompts/list_changed`
3. Client re-fetches prompt list
1. 服务器功能：`prompts.listChanged` 2. 通知：`notifications/prompts/list_changed` 3. 客户端重新获取提示列表

## Security considerations
安全注意事项

When implementing prompts:
当实现提示时：

* Validate all arguments
* Sanitize user input
* Consider rate limiting
* Implement access controls
* Audit prompt usage
* Handle sensitive data appropriately
* Validate generated content
* Implement timeouts
* Consider prompt injection risks
* Document security requirements
* 验证所有参数 * 清理用户输入 * 考虑速率限制 * 实施访问控制 * 审计提示使用 * 适当处理敏感数据 * 验证生成内容 * 实施超时 * 考虑提示注入风险 * 记录安全要求


# Resources
Source: https://modelcontextprotocol.io/docs/concepts/resources
# 资源来源：https://modelcontextprotocol.io/docs/concepts/resources

Expose data and content from your servers to LLMs
将您的服务器上的数据和内容暴露给LLMs

Resources are a core primitive in the Model Context Protocol (MCP) that allow servers to expose data and content that can be read by clients and used as context for LLM interactions.
资源是模型上下文协议（MCP）中的核心原语，允许服务器暴露数据内容和客户端可以读取并用于LLM交互的上下文。

<Note>
  Resources are designed to be **application-controlled**, meaning that the client application can decide how and when they should be used.
  Different MCP clients may handle resources differently. For example:
<注意> 资源设计为**应用程序控制**，这意味着客户端应用程序可以决定如何以及何时使用它们。不同的 MCP 客户端可能对资源有不同的处理方式。例如：

  * Claude Desktop currently requires users to explicitly select resources before they can be used
  * Other clients might automatically select resources based on heuristics
  * Some implementations may even allow the AI model itself to determine which resources to use
* Claude 桌面目前要求用户在使用之前明确选择资源 * 其他客户端可能会根据启发式方法自动选择资源 * 一些实现甚至允许 AI 模型本身决定使用哪些资源

  Server authors should be prepared to handle any of these interaction patterns when implementing resource support. In order to expose data to models automatically, server authors should use a **model-controlled** primitive such as [Tools](./tools).
</Note>
服务器作者在实现资源支持时应该准备好处理这些交互模式中的任何一种。为了自动将数据暴露给模型，服务器作者应使用**模型控制的**原语，例如[工具](./tools)。

## Overview  ## 概述

Resources represent any kind of data that an MCP server wants to make available to clients. This can include:
资源代表 MCP 服务器希望提供给客户端的任何类型的数据。这可以包括：

* File contents
* Database records
* API responses
* Live system data
* Screenshots and images
* Log files
* And more
* 文件内容 * 数据库记录 * API 响应 * 实时系统数据 * 截图和图像 * 日志文件 * 以及更多

Each resource is identified by a unique URI and can contain either text or binary data.
每个资源都通过一个唯一的 URI 进行标识，可以包含文本或二进制数据。

## Resource URIs  ## 资源 URI

Resources are identified using URIs that follow this format:
资源使用遵循此格式的 URI 进行标识：

```
[protocol]://[host]/[path]
```
``` [协议]://[主机]/[路径] ```

For example:  例如：

* `file:///home/user/documents/report.pdf`
* `postgres://database/customers/schema`
* `screen://localhost/display1`

The protocol and path structure is defined by the MCP server implementation. Servers can define their own custom URI schemes.
协议和路径结构由 MCP 服务器实现定义。服务器可以定义自己的自定义 URI 方案。

## Resource types  ## 资源类型

Resources can contain two types of content:
资源可以包含两种类型的内容：

### Text resources  ### 文本资源

Text resources contain UTF-8 encoded text data. These are suitable for:
文本资源包含 UTF-8 编码的文本数据。这些资源适用于：

* Source code
* Configuration files
* Log files
* JSON/XML data
* Plain text
* 源代码 * 配置文件 * 日志文件 * JSON/XML 数据 * 纯文本

### Binary resources  ### 二进制资源

Binary resources contain raw binary data encoded in base64. These are suitable for:
二进制资源包含原始的二进制数据，以 base64 编码。这些数据适用于：

* Images
* PDFs
* Audio files
* Video files
* Other non-text formats
* 图片 * PDF 文件 * 音频文件 * 视频文件 * 其他非文本格式

## Resource discovery  ## 资源发现

Clients can discover available resources through two main methods:
客户可以通过两种主要方法发现可用资源：

### Direct resources  ### 直接资源

Servers expose a list of concrete resources via the `resources/list` endpoint. Each resource includes:
服务器通过 `resources/list` 端点公开一个具体资源的列表。每个资源包括：

```typescript
{
  uri: string;           // Unique identifier for the resource
  name: string;          // Human-readable name
  description?: string;  // Optional description
  mimeType?: string;     // Optional MIME type
}
```
```typescript { uri: string; // 资源名称的唯一标识符 name: string; // 可读名称 description?: string; // 可选描述 mimeType?: string; // 可选 MIME 类型 } ```

### Resource templates  ### 资源模板

For dynamic resources, servers can expose [URI templates](https://datatracker.ietf.org/doc/html/rfc6570) that clients can use to construct valid resource URIs:
对于动态资源，服务器可以公开[URI 模板](https://datatracker.ietf.org/doc/html/rfc6570)，客户端可以使用这些模板来构造有效的资源 URI：

```typescript
{
  uriTemplate: string;   // URI template following RFC 6570
  name: string;          // Human-readable name for this type
  description?: string;  // Optional description
  mimeType?: string;     // Optional MIME type for all matching resources
}
```
```typescript { uriTemplate: string; // URI 模板遵循 RFC 6570 name: string; // 人类可读的名称 description?: string; // 可选描述 mimeType?: string; // 可选的匹配资源的 MIME 类型 } ```

## Reading resources  ## 读取资源

To read a resource, clients make a `resources/read` request with the resource URI.
读取资源时，客户端通过向`resources/read`请求发送资源 URI 来进行。

The server responds with a list of resource contents:
服务器将返回资源内容列表：

```typescript
{
  contents: [
    {
      uri: string;        // The URI of the resource
      mimeType?: string;  // Optional MIME type
```typescript { contents: [ { uri: string; // 资源 URI mimeType?: string; // 可选的 MIME 类型

      // One of:
      text?: string;      // For text resources
      blob?: string;      // For binary resources (base64 encoded)
    }
  ]
}
```
// 其中之一: text?: string; // 文本资源 blob?: string; // 二进制资源（base64 编码） } ] } ```

<Tip>
  Servers may return multiple resources in response to one `resources/read` request. This could be used, for example, to return a list of files inside a directory when the directory is read.
</Tip>
<提示>服务器可能在一个`resources/read`请求中返回多个资源。这可以用于，例如，当读取目录时返回目录内的文件列表。

## Resource updates  ## 资源更新

MCP supports real-time updates for resources through two mechanisms:
MCP 支持通过两种机制对资源进行实时更新：

### List changes  ### 列表变更

Servers can notify clients when their list of available resources changes via the `notifications/resources/list_changed` notification.
服务器可以通过 `notifications/resources/list_changed` 通知向客户端通知其可用资源列表的变化。

### Content changes  ### 内容变更

Clients can subscribe to updates for specific resources:
客户端可以订阅特定资源的更新：

1. Client sends `resources/subscribe` with resource URI
2. Server sends `notifications/resources/updated` when the resource changes
3. Client can fetch latest content with `resources/read`
4. Client can unsubscribe with `resources/unsubscribe`
1. 客户端发送 `resources/subscribe` 并提供资源 URI 2. 当资源发生变化时，服务器发送 `notifications/resources/updated` 通知 3. 客户端可以使用 `resources/read` 获取最新内容 4. 客户端可以使用 `resources/unsubscribe` 进行退订

## Example implementation
示例实现

Here's a simple example of implementing resource support in an MCP server:
这里是一个在 MCP 服务器中实现资源支持的简单示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {
        resources: {}
      }
    });

    // List available resources
    server.setRequestHandler(ListResourcesRequestSchema, async () => {
      return {
        resources: [
          {
            uri: "file:///logs/app.log",
            name: "Application Logs",
            mimeType: "text/plain"
          }
        ]
      };
    });
// 列出可用资源 server.setRequestHandler(ListResourcesRequestSchema, async () => { return { resources: [ { uri: "file:///logs/app.log", name: "Application Logs", mimeType: "text/plain" } ] }; });

    // Read resource contents
    server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const uri = request.params.uri;
// 读取资源内容 server.setRequestHandler(ReadResourceRequestSchema, 异步函数 (request) => { const uri = request.params.uri;

      if (uri === "file:///logs/app.log") {
        const logContents = await readLogFile();
        return {
          contents: [
            {
              uri,
              mimeType: "text/plain",
              text: logContents
            }
          ]
        };
      }

      throw new Error("Resource not found");
    });
    ```
  </Tab>
throw new Error("资源未找到"); }); ``` 

  <Tab title="Python">
    ```python
    app = Server("example-server")

    @app.list_resources()
    async def list_resources() -> list[types.Resource]:
        return [
            types.Resource(
                uri="file:///logs/app.log",
                name="Application Logs",
                mimeType="text/plain"
            )
        ]
@app.list_resources() async def list_resources() -> list[types.Resource]: return [types.Resource(uri="file:///logs/app.log", name="Application Logs", mimeType="text/plain")]

    @app.read_resource()
    async def read_resource(uri: AnyUrl) -> str:
        if str(uri) == "file:///logs/app.log":
            log_contents = await read_log_file()
            return log_contents

        raise ValueError("Resource not found")

    # Start server
    async with stdio_server() as streams:
        await app.run(
            streams[0],
            streams[1],
            app.create_initialization_options()
        )
    ```
  </Tab>
</Tabs>
# Start server async with stdio_server() as streams: await app.run(streams[0], streams[1], app.create_initialization_options()) ```  

## Best practices  最佳实践

When implementing resource support:
在实现资源支持时：

1. Use clear, descriptive resource names and URIs
2. Include helpful descriptions to guide LLM understanding
3. Set appropriate MIME types when known
4. Implement resource templates for dynamic content
5. Use subscriptions for frequently changing resources
6. Handle errors gracefully with clear error messages
7. Consider pagination for large resource lists
8. Cache resource contents when appropriate
9. Validate URIs before processing
10. Document your custom URI schemes
1. 使用清晰、描述性的资源名称和 URI 2. 包含有助于理解的描述 3. 当已知时设置适当的 MIME 类型 4. 实现资源模板以支持动态内容 5. 使用订阅来处理频繁更改的资源 6. 优雅地处理错误并给出清晰的错误信息 7. 考虑分页以处理大型资源列表 8. 在适当的情况下缓存资源内容 9. 在处理前验证 URI 10. 记录自定义 URI 方案

## Security considerations
安全考虑

When exposing resources:  当暴露资源时：

* Validate all resource URIs
* Implement appropriate access controls
* Sanitize file paths to prevent directory traversal
* Be cautious with binary data handling
* Consider rate limiting for resource reads
* Audit resource access
* Encrypt sensitive data in transit
* Validate MIME types
* Implement timeouts for long-running reads
* Handle resource cleanup appropriately
* 验证所有资源 URI * 实施适当的访问控制 * 清理文件路径以防止目录遍历 * 小心处理二进制数据 * 考虑资源读取的速率限制 * 审计资源访问 * 加密传输中的敏感数据 * 验证 MIME 类型 * 实施长时间读取的超时 * 适当处理资源清理


# Roots
Source: https://modelcontextprotocol.io/docs/concepts/roots
# Roots 源：https://modelcontextprotocol.io/docs/concepts/roots

Understanding roots in MCP
理解 MCP 中的 roots

Roots are a concept in MCP that define the boundaries where servers can operate. They provide a way for clients to inform servers about relevant resources and their locations.
根是 MCP 中的一个概念，定义了服务器可以操作的范围。它们提供了一种方式，让客户端向服务器告知相关资源及其位置。

## What are Roots?  什么是根？

A root is a URI that a client suggests a server should focus on. When a client connects to a server, it declares which roots the server should work with. While primarily used for filesystem paths, roots can be any valid URI including HTTP URLs.
根是一个客户端建议服务器关注的 URI。当客户端连接到服务器时，它会声明服务器应该与哪些根一起工作。虽然主要用于文件系统路径，但根可以是任何有效的 URI，包括 HTTP URL。

For example, roots could be:
例如，根可以是：

```
file:///home/user/projects/myapp
https://api.example.com/v1
```
``` 文件路径:/home/user/projects/myapp https://api.example.com/v1 ```

## Why Use Roots?  ## 为什么使用 Roots？

Roots serve several important purposes:
Roots 具有几个重要的用途：

1. **Guidance**: They inform servers about relevant resources and locations
2. **Clarity**: Roots make it clear which resources are part of your workspace
3. **Organization**: Multiple roots let you work with different resources simultaneously
1. **指导**：它们通知服务器有关相关资源和位置 2. **清晰**：Roots 使您清楚哪些资源属于您的项目空间 3. **组织**：多个 Roots 允许您同时处理不同的资源

## How Roots Work  根的工作原理

When a client supports roots, it:
当客户端支持根时，它：

1. Declares the `roots` capability during connection
2. Provides a list of suggested roots to the server
3. Notifies the server when roots change (if supported)
1. 在连接期间声明 `roots` 功能 2. 向服务器提供建议的根列表 3. 通知服务器根发生变化（如果支持）

While roots are informational and not strictly enforcing, servers should:
虽然“根”是信息性的，并不强制执行，但服务器应该：

1. Respect the provided roots
2. Use root URIs to locate and access resources
3. Prioritize operations within root boundaries
1. 尊重提供的根 2. 使用根 URI 定位和访问资源 3. 优先在根边界内进行操作

## Common Use Cases  ## 常见用例

Roots are commonly used to define:
根通常用于定义：

* Project directories
* Repository locations
* API endpoints
* Configuration locations
* Resource boundaries
* 项目目录 * 仓库位置 * API 端点 * 配置位置 * 资源边界

## Best Practices  最佳实践

When working with roots:  当与根目录一起工作时：

1. Only suggest necessary resources
2. Use clear, descriptive names for roots
3. Monitor root accessibility
4. Handle root changes gracefully
1. 仅建议必要的资源 2. 使用清晰、描述性的名称为根目录命名 3. 监控根目录的访问性 4. 优雅地处理根目录变更

## Example  ## 示例

Here's how a typical MCP client might expose roots:
这是一般 MCP 客户端如何暴露根目录的示例：

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/frontend",
      "name": "Frontend Repository"
    },
    {
      "uri": "https://api.example.com/v1",
      "name": "API Endpoint"
    }
  ]
}
```
```json { "roots": [ { "uri": "file:///home/user/projects/frontend", "name": "前端仓库" }, { "uri": "https://api.example.com/v1", "name": "API 端点" } ] } ```

This configuration suggests the server focus on both a local repository and an API endpoint while keeping them logically separated.
此配置表明服务器应同时关注本地仓库和 API 端点，同时保持它们在逻辑上分离。


# Sampling
Source: https://modelcontextprotocol.io/docs/concepts/sampling
# 样本来源：https://modelcontextprotocol.io/docs/concepts/sampling

Let your servers request completions from LLMs
让您的服务器从 LLMs 请求补全

Sampling is a powerful MCP feature that allows servers to request LLM completions through the client, enabling sophisticated agentic behaviors while maintaining security and privacy.
样本化是 MCP 的一个强大功能，允许服务器通过客户端请求 LLM 补全，实现复杂的代理行为，同时保持安全和隐私。

<Info>
  This feature of MCP is not yet supported in the Claude Desktop client.
</Info>
 MCP 的这个功能在 Claude 桌面客户端中尚未支持。 

## How sampling works  ## 样本化工作原理

The sampling flow follows these steps:
样本流程遵循以下步骤：

1. Server sends a `sampling/createMessage` request to the client
2. Client reviews the request and can modify it
3. Client samples from an LLM
4. Client reviews the completion
5. Client returns the result to the server
1. 服务器向客户端发送 `sampling/createMessage` 请求 2. 客户端审查请求并可以修改它 3. 客户端从 LLM 中采样 4. 客户端审查完成情况 5. 客户端将结果返回给服务器

This human-in-the-loop design ensures users maintain control over what the LLM sees and generates.
这种人机交互设计确保用户对 LLM 看到和生成的内容保持控制。

## Message format  ## 消息格式

Sampling requests use a standardized message format:
样本请求使用标准化的消息格式：

```typescript
{
  messages: [
    {
      role: "user" | "assistant",
      content: {
        type: "text" | "image",

        // For text:
        text?: string,

        // For images:
        data?: string,             // base64 encoded
        mimeType?: string
      }
    }
  ],
  modelPreferences?: {
    hints?: [{
      name?: string                // Suggested model name/family
    }],
    costPriority?: number,         // 0-1, importance of minimizing cost
    speedPriority?: number,        // 0-1, importance of low latency
    intelligencePriority?: number  // 0-1, importance of capabilities
  },
  systemPrompt?: string,
  includeContext?: "none" | "thisServer" | "allServers",
  temperature?: number,
  maxTokens: number,
  stopSequences?: string[],
  metadata?: Record<string, unknown>
}
```
// For images: data?: string, // base64 encoded mimeType?: string } ], modelPreferences?: { hints?: [{ name?: string // Suggested model name/family }], costPriority?: number, // 0-1, importance of minimizing cost speedPriority?: number, // 0-1, importance of low latency intelligencePriority?: number // 0-1, importance of capabilities }, systemPrompt?: string, includeContext?: "none" | "thisServer" | "allServers", temperature?: number, maxTokens: number, stopSequences?: string[], metadata?: Record } ```

## Request parameters  ## 请求参数

### Messages  ### 消息

The `messages` array contains the conversation history to send to the LLM. Each message has:
`messages` 数组包含要发送到 LLM 的对话历史。每条消息包含：

* `role`: Either "user" or "assistant"
* `content`: The message content, which can be:
  * Text content with a `text` field
  * Image content with `data` (base64) and `mimeType` fields
* `角色`：可以是 "用户" 或 "助手" * `内容`：可以是 * 文本内容，包含 `text` 字段 * 图片内容，包含 `data`（base64）和 `mimeType` 字段

### Model preferences  ### 模型偏好

The `modelPreferences` object allows servers to specify their model selection preferences:
`modelPreferences` 对象允许服务器指定其模型选择偏好：

* `hints`: Array of model name suggestions that clients can use to select an appropriate model:
  * `name`: String that can match full or partial model names (e.g. "claude-3", "sonnet")
  * Clients may map hints to equivalent models from different providers
  * Multiple hints are evaluated in preference order
* `hints`：客户端可以使用以选择适当模型的模型名称建议数组：* `name`：可以匹配完整或部分模型名称的字符串（例如："claude-3"，"sonnet"）* 客户端可以将提示映射到来自不同提供商的等效模型* 多个提示按优先级顺序评估

* Priority values (0-1 normalized):
  * `costPriority`: Importance of minimizing costs
  * `speedPriority`: Importance of low latency response
  * `intelligencePriority`: Importance of advanced model capabilities
* 优先级值（0-1 归一化）：* `costPriority`：最小化成本的重要性* `speedPriority`：低延迟响应的重要性* `intelligencePriority`：高级模型功能的重要性

Clients make the final model selection based on these preferences and their available models.
客户根据这些偏好和可用的模型进行最终模型选择。

### System prompt  ### 系统提示

An optional `systemPrompt` field allows servers to request a specific system prompt. The client may modify or ignore this.
可选的 `systemPrompt` 字段允许服务器请求特定的系统提示。客户端可以修改或忽略此提示。

### Context inclusion  ### 上下文包含

The `includeContext` parameter specifies what MCP context to include:
`includeContext` 参数指定要包含哪个 MCP 上下文：

* `"none"`: No additional context
* `"thisServer"`: Include context from the requesting server
* `"allServers"`: Include context from all connected MCP servers
* `"none"`：不包含额外上下文 * `"thisServer"`：包含请求服务器的上下文 * `"allServers"`：包含所有连接的 MCP 服务器上下文

The client controls what context is actually included.
客户端控制实际包含的上下文。

### Sampling parameters  ### 样本参数

Fine-tune the LLM sampling with:
调整LLM采样：

* `temperature`: Controls randomness (0.0 to 1.0)
* `maxTokens`: Maximum tokens to generate
* `stopSequences`: Array of sequences that stop generation
* `metadata`: Additional provider-specific parameters
* `温度`: 控制随机性（0.0 到 1.0）* `maxTokens`: 生成最大标记数* `stopSequences`: 停止生成的序列数组* `metadata`: 额外的提供者特定参数

## Response format  ## 响应格式

The client returns a completion result:
客户端返回完成结果：

```typescript
{
  model: string,  // Name of the model used
  stopReason?: "endTurn" | "stopSequence" | "maxTokens" | string,
  role: "user" | "assistant",
  content: {
    type: "text" | "image",
    text?: string,
    data?: string,
    mimeType?: string
  }
}
```
```typescript { 模型名称: string, // 使用模型的名称 stopReason?: "endTurn" | "stopSequence" | "maxTokens" | string, 角色: "user" | "assistant", 内容: { 类型: "text" | "image", 文本?: string, 数据?: string, MIME 类型?: string } } ```

## Example request  ## 示例请求

Here's an example of requesting sampling from a client:
这里是一个从客户端请求采样的示例：

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100
  }
}
```
```json { "method": "sampling/createMessage", "params": { "messages": [ { "role": "user", "content": { "type": "text", "text": "当前目录中有哪些文件？" } } ], "systemPrompt": "你是一个有用的文件系统助手。", "includeContext": "thisServer", "maxTokens": 100 } } ```

## Best practices  最佳实践

When implementing sampling:
在实施采样时：

1. Always provide clear, well-structured prompts
2. Handle both text and image content appropriately
3. Set reasonable token limits
4. Include relevant context through `includeContext`
5. Validate responses before using them
6. Handle errors gracefully
7. Consider rate limiting sampling requests
8. Document expected sampling behavior
9. Test with various model parameters
10. Monitor sampling costs
1. 总是提供清晰、结构良好的提示 2. 适当处理文本和图像内容 3. 设置合理的令牌限制 4. 通过 `includeContext` 包含相关上下文 5. 在使用之前验证响应 6. 优雅地处理错误 7. 考虑限制采样请求的速率 8. 记录预期的采样行为 9. 使用不同的模型参数进行测试 10. 监控采样成本

## Human in the loop controls
## 环境中的人类控制

Sampling is designed with human oversight in mind:
样本设计时考虑了人工监督：

### For prompts  ### 对于提示

* Clients should show users the proposed prompt
* Users should be able to modify or reject prompts
* System prompts can be filtered or modified
* Context inclusion is controlled by the client
* 客户应向用户展示拟定的提示 * 用户应能够修改或拒绝提示 * 系统提示可以被筛选或修改 * 上下文包含由客户控制

### For completions  ### 对于完成

* Clients should show users the completion
* Users should be able to modify or reject completions
* Clients can filter or modify completions
* Users control which model is used
* 客户应向用户展示完成情况 * 用户应能够修改或拒绝完成情况 * 客户可以筛选或修改完成情况 * 用户控制使用的模型

## Security considerations
## 安全考虑

When implementing sampling:
当实现采样时：

* Validate all message content
* Sanitize sensitive information
* Implement appropriate rate limits
* Monitor sampling usage
* Encrypt data in transit
* Handle user data privacy
* Audit sampling requests
* Control cost exposure
* Implement timeouts
* Handle model errors gracefully
* 验证所有消息内容 * 清洗敏感信息 * 实施适当的速率限制 * 监控采样使用情况 * 加密传输中的数据 * 处理用户数据隐私 * 审计采样请求 * 控制成本暴露 * 实施超时 * 优雅地处理模型错误

## Common patterns  常见模式

### Agentic workflows  ### 代理工作流程

Sampling enables agentic patterns like:
样本化使代理模式成为可能：

* Reading and analyzing resources
* Making decisions based on context
* Generating structured data
* Handling multi-step tasks
* Providing interactive assistance
* 阅读和分析资源 * 基于上下文做出决策 * 生成结构化数据 * 处理多步骤任务 * 提供交互式辅助

### Context management  ### 环境管理

Best practices for context:
环境管理的最佳实践：

* Request minimal necessary context
* Structure context clearly
* Handle context size limits
* Update context as needed
* Clean up stale context
* 请求最少的必要环境 * 清晰地结构化环境 * 处理环境大小限制 * 需要时更新环境 * 清理过时的环境

### Error handling  ### 错误处理

Robust error handling should:
严谨的错误处理应该：

* Catch sampling failures
* Handle timeout errors
* Manage rate limits
* Validate responses
* Provide fallback behaviors
* Log errors appropriately
* 捕获采样失败 * 处理超时错误 * 管理速率限制 * 验证响应 * 提供回退行为 * 适当地记录错误

## Limitations  ## 局限性

Be aware of these limitations:
注意以下局限性：

* Sampling depends on client capabilities
* Users control sampling behavior
* Context size has limits
* Rate limits may apply
* Costs should be considered
* Model availability varies
* Response times vary
* Not all content types supported
样本取决于客户端能力 用户控制采样行为 上下文大小有限 可能存在速率限制 应考虑成本 模型可用性不同 响应时间不同 并非所有内容类型都受支持


# Tools
Source: https://modelcontextprotocol.io/docs/concepts/tools
工具来源：https://modelcontextprotocol.io/docs/concepts/tools

Enable LLMs to perform actions through your server
启用 LLMs 通过您的服务器执行操作

Tools are a powerful primitive in the Model Context Protocol (MCP) that enable servers to expose executable functionality to clients. Through tools, LLMs can interact with external systems, perform computations, and take actions in the real world.
工具是模型上下文协议（MCP）中的一个强大原语，它使服务器能够向客户端暴露可执行功能。通过工具，LLMs 可以与外部系统交互，执行计算并在现实世界中采取行动。

<Note>
  Tools are designed to be **model-controlled**, meaning that tools are exposed from servers to clients with the intention of the AI model being able to automatically invoke them (with a human in the loop to grant approval).
</Note>
工具设计为**模型控制**，这意味着工具从服务器暴露给客户端，目的是让 AI 模型能够自动调用它们（由人工在旁监督批准）。

## Overview  ## 概述

Tools in MCP allow servers to expose executable functions that can be invoked by clients and used by LLMs to perform actions. Key aspects of tools include:
在 MCP 中，工具允许服务器暴露可执行的函数，这些函数可以被客户端调用并由LLMs执行操作。工具的关键特性包括：

* **Discovery**: Clients can list available tools through the `tools/list` endpoint
* **Invocation**: Tools are called using the `tools/call` endpoint, where servers perform the requested operation and return results
* **Flexibility**: Tools can range from simple calculations to complex API interactions
* **发现**：客户端可以通过`tools/list`端点列出可用的工具 * **调用**：使用`tools/call`端点调用工具，服务器执行请求的操作并返回结果 * **灵活性**：工具的范围从简单的计算到复杂的 API 交互

Like [resources](/docs/concepts/resources), tools are identified by unique names and can include descriptions to guide their usage. However, unlike resources, tools represent dynamic operations that can modify state or interact with external systems.
如[资源](/docs/concepts/resources)，工具通过唯一的名称进行标识，可以包含描述以指导其使用。然而，与资源不同，工具代表动态操作，可以修改状态或与外部系统交互。

## Tool definition structure
## 工具定义结构

Each tool is defined with the following structure:
每个工具都使用以下结构进行定义：

```typescript
{
  name: string;          // Unique identifier for the tool
  description?: string;  // Human-readable description
  inputSchema: {         // JSON Schema for the tool's parameters
    type: "object",
    properties: { ... }  // Tool-specific parameters
  },
  annotations?: {        // Optional hints about tool behavior
    title?: string;      // Human-readable title for the tool
    readOnlyHint?: boolean;    // If true, the tool does not modify its environment
    destructiveHint?: boolean; // If true, the tool may perform destructive updates
    idempotentHint?: boolean;  // If true, repeated calls with same args have no additional effect
    openWorldHint?: boolean;   // If true, tool interacts with external entities
  }
}
```
```typescript { name: string; // 工具的唯一标识符 description?: string; // 可读性描述 inputSchema: { // 工具参数的 JSON Schema type: "object", properties: { ... } // 工具特定的参数 }, annotations?: { // 关于工具行为的可选提示 title?: string; // 工具的可读性标题 readOnlyHint?: boolean; // 如果为 true，则工具不会修改其环境 destructiveHint?: boolean; // 如果为 true，则工具可能执行破坏性更新 idempotentHint?: boolean; // 如果为 true，则具有相同参数的重复调用没有额外效果 openWorldHint?: boolean; // 如果为 true，则工具与外部实体交互 } } ```

## Implementing tools  实现工具

Here's an example of implementing a basic tool in an MCP server:
以下是一个在 MCP 服务器中实现基本工具的示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {
        tools: {}
      }
    });

    // Define available tools
    server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [{
          name: "calculate_sum",
          description: "Add two numbers together",
          inputSchema: {
            type: "object",
            properties: {
              a: { type: "number" },
              b: { type: "number" }
            },
            required: ["a", "b"]
          }
        }]
      };
    });
// 定义可用的工具 server.setRequestHandler(ListToolsRequestSchema, async () => { return { tools: [{ name: "calculate_sum", description: "Add two numbers together", inputSchema: { type: "object", properties: { a: { type: "number" }, b: { type: "number" } }, required: ["a", "b"] } }] }; });

    // Handle tool execution
    server.setRequestHandler(CallToolRequestSchema, async (request) => {
      if (request.params.name === "calculate_sum") {
        const { a, b } = request.params.arguments;
        return {
          content: [
            {
              type: "text",
              text: String(a + b)
            }
          ]
        };
      }
      throw new Error("Tool not found");
    });
    ```
  </Tab>
// 处理工具执行服务器.setRequestHandler(CallToolRequestSchema, 异步 (request) => { if (request.params.name === "calculate_sum") { const { a, b } = request.params.arguments; return { content: [ { type: "text", text: String(a + b) } ] }; } throw new Error("工具未找到"); }); ``` 

  <Tab title="Python">
    ```python
    app = Server("example-server")

    @app.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="calculate_sum",
                description="Add two numbers together",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"}
                    },
                    "required": ["a", "b"]
                }
            )
        ]
@app.list_tools() 异步 def list_tools() -> list[types.Tool]: return [ types.Tool( name="calculate_sum", description="将两个数字相加", inputSchema={ "type": "object", "properties": { "a": {"type": "number"}, "b": {"type": "number"} }, "required": ["a", "b"] } ) ]

    @app.call_tool()
    async def call_tool(
        name: str,
        arguments: dict
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        if name == "calculate_sum":
            a = arguments["a"]
            b = arguments["b"]
            result = a + b
            return [types.TextContent(type="text", text=str(result))]
        raise ValueError(f"Tool not found: {name}")
    ```
  </Tab>
</Tabs>
@app.call_tool() 异步 def call_tool( name: str, arguments: dict ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]: if name == "calculate_sum": a = arguments["a"] b = arguments["b"] result = a + b return [types.TextContent(type="text", text=str(result))] raise ValueError(f"工具未找到: {name}") ```  

## Example tool patterns  示例工具模式

Here are some examples of types of tools that a server could provide:
以下是一些服务器可能提供的工具类型示例：

### System operations  ### 系统操作

Tools that interact with the local system:
与本地系统交互的工具：

```typescript
{
  name: "execute_command",
  description: "Run a shell command",
  inputSchema: {
    type: "object",
    properties: {
      command: { type: "string" },
      args: { type: "array", items: { type: "string" } }
    }
  }
}
```
```typescript { name: "execute_command", description: "运行 shell 命令", inputSchema: { type: "object", properties: { command: { type: "string" }, args: { type: "array", items: { type: "string" } } } } } ```

### API integrations  ### API 集成

Tools that wrap external APIs:
包装外部 API 的工具：

```typescript
{
  name: "github_create_issue",
  description: "Create a GitHub issue",
  inputSchema: {
    type: "object",
    properties: {
      title: { type: "string" },
      body: { type: "string" },
      labels: { type: "array", items: { type: "string" } }
    }
  }
}
```
```typescript { name: "github_create_issue", description: "创建 GitHub 问题", inputSchema: { type: "object", properties: { title: { type: "string" }, body: { type: "string" }, labels: { type: "array", items: { type: "string" } } } } } ```

### Data processing  数据处理

Tools that transform or analyze data:
用于转换或分析数据的工具：

```typescript
{
  name: "analyze_csv",
  description: "Analyze a CSV file",
  inputSchema: {
    type: "object",
    properties: {
      filepath: { type: "string" },
      operations: {
        type: "array",
        items: {
          enum: ["sum", "average", "count"]
        }
      }
    }
  }
}
```
```typescript { name: "analyze_csv", description: "分析 CSV 文件", inputSchema: { type: "object", properties: { filepath: { type: "string" }, operations: { type: "array", items: { enum: ["sum", "average", "count"] } } } } } ```

## Best practices  最佳实践

When implementing tools:  在实现工具时：

1. Provide clear, descriptive names and descriptions
2. Use detailed JSON Schema definitions for parameters
3. Include examples in tool descriptions to demonstrate how the model should use them
4. Implement proper error handling and validation
5. Use progress reporting for long operations
6. Keep tool operations focused and atomic
7. Document expected return value structures
8. Implement proper timeouts
9. Consider rate limiting for resource-intensive operations
10. Log tool usage for debugging and monitoring
1. 提供清晰、描述性的名称和描述 2. 使用详细的 JSON Schema 定义参数 3. 在工具描述中包含示例以展示模型如何使用它们 4. 实现适当的错误处理和验证 5. 对于长时间操作使用进度报告 6. 保持工具操作集中和原子化 7. 记录预期的返回值结构 8. 实现适当的超时 9. 考虑对资源密集型操作进行速率限制 10. 记录工具使用情况以供调试和监控

## Security considerations
## 安全考虑

When exposing tools:  当公开工具时：

### Input validation  ### 输入验证

* Validate all parameters against the schema
* Sanitize file paths and system commands
* Validate URLs and external identifiers
* Check parameter sizes and ranges
* Prevent command injection
* 验证所有参数是否符合模式 * 清理文件路径和系统命令 * 验证 URL 和外部标识符 * 检查参数大小和范围 * 防止命令注入

### Access control  ### 访问控制

* Implement authentication where needed
* Use appropriate authorization checks
* Audit tool usage
* Rate limit requests
* Monitor for abuse
* 在需要的地方实现身份验证 * 使用适当的授权检查 * 审计工具使用情况 * 限制请求速率 * 监控滥用行为

### Error handling  ### 错误处理

* Don't expose internal errors to clients
* Log security-relevant errors
* Handle timeouts appropriately
* Clean up resources after errors
* Validate return values
* 不要向客户端暴露内部错误 * 记录安全相关错误 * 适当地处理超时 * 错误后清理资源 * 验证返回值

## Tool discovery and updates
## 工具发现和更新

MCP supports dynamic tool discovery:
MCP 支持动态工具发现：

1. Clients can list available tools at any time
2. Servers can notify clients when tools change using `notifications/tools/list_changed`
3. Tools can be added or removed during runtime
4. Tool definitions can be updated (though this should be done carefully)
1. 客户可以随时列出可用的工具 2. 服务器可以使用 `notifications/tools/list_changed` 通知客户端工具变更 3. 工具可以在运行时添加或删除 4. 工具定义可以更新（尽管应该谨慎操作）

## Error handling  ## 错误处理

Tool errors should be reported within the result object, not as MCP protocol-level errors. This allows the LLM to see and potentially handle the error. When a tool encounters an error:
工具错误应在结果对象中报告，而不是作为 MCP 协议级别的错误。这允许 LLM 查看并可能处理错误。当工具遇到错误时：

1. Set `isError` to `true` in the result
2. Include error details in the `content` array
1. 在结果中将 `isError` 设置为 `true` 2. 在 `content` 数组中包含错误详情

Here's an example of proper error handling for tools:
这里是一个工具正确错误处理的示例：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    try {
      // Tool operation
      const result = performOperation();
      return {
        content: [
          {
            type: "text",
            text: `Operation successful: ${result}`
          }
        ]
      };
    } catch (error) {
      return {
        isError: true,
        content: [
          {
            type: "text",
            text: `Error: ${error.message}`
          }
        ]
      };
    }
    ```
  </Tab>
  ```typescript try { // 工具操作 const result = performOperation(); return { content: [ { type: "text", text: `操作成功: ${result}` } ] }; } catch (error) { return { isError: true, content: [ { type: "text", text: `错误: ${error.message}` } ] }; } ``` 

  <Tab title="Python">
    ```python
    try:
        # Tool operation
        result = perform_operation()
        return types.CallToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text=f"Operation successful: {result}"
                )
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[
                types.TextContent(
                    type="text",
                    text=f"Error: {str(error)}"
                )
            ]
        )
    ```
  </Tab>
</Tabs>
 ```python try: # 工具操作 result = perform_operation() return types.CallToolResult( content=[ types.TextContent( type="text", text=f"操作成功: {result}" ) ] ) except Exception as error: return types.CallToolResult( isError=True, content=[ types.TextContent( type="text", text=f"错误: {str(error)}" ) ] ) ```  

This approach allows the LLM to see that an error occurred and potentially take corrective action or request human intervention.
这种方法允许 LLM 看到发生了错误，并可能采取纠正措施或请求人工干预。

## Tool annotations  工具注释

Tool annotations provide additional metadata about a tool's behavior, helping clients understand how to present and manage tools. These annotations are hints that describe the nature and impact of a tool, but should not be relied upon for security decisions.
工具注释提供了关于工具行为的额外元数据，帮助客户端了解如何展示和管理工具。这些注释是描述工具性质和影响的提示，但不应用于安全决策。

### Purpose of tool annotations
### 工具注释的目的

Tool annotations serve several key purposes:
工具注释有几个关键用途：

1. Provide UX-specific information without affecting model context
2. Help clients categorize and present tools appropriately
3. Convey information about a tool's potential side effects
4. Assist in developing intuitive interfaces for tool approval
1. 提供不影响模型上下文的 UX 特定信息 2. 帮助客户适当地分类和展示工具 3. 传达关于工具潜在副作用的说明 4. 协助开发直观的工具审批界面

### Available tool annotations
### 可用工具注释

The MCP specification defines the following annotations for tools:
MCP 规范定义了以下工具注释：

| Annotation        | Type    | Default | Description                                                                                                                          |
| ----------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `title`           | string  | -       | A human-readable title for the tool, useful for UI display                                                                           |
| `readOnlyHint`    | boolean | false   | If true, indicates the tool does not modify its environment                                                                          |
| `destructiveHint` | boolean | true    | If true, the tool may perform destructive updates (only meaningful when `readOnlyHint` is false)                                     |
| `idempotentHint`  | boolean | false   | If true, calling the tool repeatedly with the same arguments has no additional effect (only meaningful when `readOnlyHint` is false) |
| `openWorldHint`   | boolean | true    | If true, the tool may interact with an "open world" of external entities                                                             |
| 注释 | 类型 | 默认值 | 描述 | | ----------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------ | | `title` | 字符串 | - | 供 UI 显示的易读标题 | | `readOnlyHint` | 布尔值 | false | 如果为 true，表示工具不修改其环境 | | `destructiveHint` | 布尔值 | true | 如果为 true，工具可能执行破坏性更新（仅在`readOnlyHint`为 false 时才有意义） | | `idempotentHint` | 布尔值 | false | 如果为 true，重复调用工具使用相同的参数没有额外效果（仅在`readOnlyHint`为 false 时才有意义） | | `openWorldHint` | 布尔值 | true | 如果为 true，工具可能与外部实体“开放世界”交互 |

### Example usage  示例用法

Here's how to define tools with annotations for different scenarios:
这里是如何定义不同场景下的工具及其注解：

```typescript
// A read-only search tool
{
  name: "web_search",
  description: "Search the web for information",
  inputSchema: {
    type: "object",
    properties: {
      query: { type: "string" }
    },
    required: ["query"]
  },
  annotations: {
    title: "Web Search",
    readOnlyHint: true,
    openWorldHint: true
  }
}
```typescript // 只读搜索工具 { name: "web_search", description: "在网络上搜索信息", inputSchema: { type: "object", properties: { query: { type: "string" } }, required: ["query"] }, annotations: { title: "网络搜索", readOnlyHint: true, openWorldHint: true } }

// A destructive file deletion tool
{
  name: "delete_file",
  description: "Delete a file from the filesystem",
  inputSchema: {
    type: "object",
    properties: {
      path: { type: "string" }
    },
    required: ["path"]
  },
  annotations: {
    title: "Delete File",
    readOnlyHint: false,
    destructiveHint: true,
    idempotentHint: true,
    openWorldHint: false
  }
}
// 一个破坏性文件删除工具 { name: "delete_file", description: "从文件系统中删除文件", inputSchema: { type: "object", properties: { path: { type: "string" } }, required: ["path"] }, annotations: { title: "删除文件", readOnlyHint: false, destructiveHint: true, idempotentHint: true, openWorldHint: false } }

// A non-destructive database record creation tool
{
  name: "create_record",
  description: "Create a new record in the database",
  inputSchema: {
    type: "object",
    properties: {
      table: { type: "string" },
      data: { type: "object" }
    },
    required: ["table", "data"]
  },
  annotations: {
    title: "Create Database Record",
    readOnlyHint: false,
    destructiveHint: false,
    idempotentHint: false,
    openWorldHint: false
  }
}
```
// 一个非破坏性数据库记录创建工具 { name: "create_record", description: "在数据库中创建新记录", inputSchema: { type: "object", properties: { table: { type: "string" }, data: { type: "object" } }, required: ["table", "data"] }, annotations: { title: "创建数据库记录", readOnlyHint: false, destructiveHint: false, idempotentHint: false, openWorldHint: false } }

### Integrating annotations in server implementation
### 在服务器实现中集成注释

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [{
          name: "calculate_sum",
          description: "Add two numbers together",
          inputSchema: {
            type: "object",
            properties: {
              a: { type: "number" },
              b: { type: "number" }
            },
            required: ["a", "b"]
          },
          annotations: {
            title: "Calculate Sum",
            readOnlyHint: true,
            openWorldHint: false
          }
        }]
      };
    });
    ```
  </Tab>
  ```typescript server.setRequestHandler(ListToolsRequestSchema, async () => { return { tools: [{ name: "calculate_sum", description: "将两个数字相加", inputSchema: { type: "object", properties: { a: { type: "number" }, b: { type: "number" } }, required: ["a", "b"] }, annotations: { title: "计算总和", readOnlyHint: true, openWorldHint: false } }] }; }); ``` 

  <Tab title="Python">
    ```python
    from mcp.server.fastmcp import FastMCP
 ```python from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("example-server")

    @mcp.tool(
        annotations={
            "title": "Calculate Sum",
            "readOnlyHint": True,
            "openWorldHint": False
        }
    )
    async def calculate_sum(a: float, b: float) -> str:
        """Add two numbers together.
@mcp.tool( annotations={ "title": "计算总和", "readOnlyHint": True, "openWorldHint": False } ) async def calculate_sum(a: float, b: float) -> str: """将两个数字相加。

        Args:
            a: First number to add
            b: Second number to add
        """
        result = a + b
        return str(result)
    ```
  </Tab>
</Tabs>
Args: a: 要相加的第一个数字 b: 要相加的第二个数字 """ result = a + b return str(result) ```  

### Best practices for tool annotations
### 工具注释的最佳实践

1. **Be accurate about side effects**: Clearly indicate whether a tool modifies its environment and whether those modifications are destructive.
1. **准确描述副作用**：明确指出工具是否修改其环境以及这些修改是否具有破坏性。

2. **Use descriptive titles**: Provide human-friendly titles that clearly describe the tool's purpose.
2. **使用描述性标题**：提供清晰描述工具用途的人性化标题。

3. **Indicate idempotency properly**: Mark tools as idempotent only if repeated calls with the same arguments truly have no additional effect.
3. **正确标识幂等性**：只有当具有相同参数的重复调用确实没有额外影响时，才将工具标记为幂等的。

4. **Set appropriate open/closed world hints**: Indicate whether a tool interacts with a closed system (like a database) or an open system (like the web).
4. **设置适当的开放/封闭世界提示**：指示工具是否与封闭系统（如数据库）或开放系统（如网络）交互。

5. **Remember annotations are hints**: All properties in ToolAnnotations are hints and not guaranteed to provide a faithful description of tool behavior. Clients should never make security-critical decisions based solely on annotations.
5. **记住，注释是提示**：ToolAnnotations 中的所有属性都是提示，并不保证能够忠实描述工具的行为。客户端不应仅基于注释做出安全关键的决定。

## Testing tools  ## 测试工具

A comprehensive testing strategy for MCP tools should cover:
MCP 工具的综合测试策略应包括：

* **Functional testing**: Verify tools execute correctly with valid inputs and handle invalid inputs appropriately
* **Integration testing**: Test tool interaction with external systems using both real and mocked dependencies
* **Security testing**: Validate authentication, authorization, input sanitization, and rate limiting
* **Performance testing**: Check behavior under load, timeout handling, and resource cleanup
* **Error handling**: Ensure tools properly report errors through the MCP protocol and clean up resources
* **功能测试**：验证工具在有效输入下正确执行，并适当处理无效输入 * **集成测试**：测试工具与外部系统的交互，使用真实和模拟的依赖项 * **安全测试**：验证身份验证、授权、输入清理和速率限制 * **性能测试**：检查负载下的行为、超时处理和资源清理 * **错误处理**：确保工具通过 MCP 协议正确报告错误并清理资源


# Transports
Source: https://modelcontextprotocol.io/docs/concepts/transports
# 传输来源: https://modelcontextprotocol.io/docs/concepts/transports

Learn about MCP's communication mechanisms
了解 MCP 的通信机制

Transports in the Model Context Protocol (MCP) provide the foundation for communication between clients and servers. A transport handles the underlying mechanics of how messages are sent and received.
模型上下文协议（MCP）的传输为客户端和服务器之间的通信提供基础。传输处理消息发送和接收的底层机制。

## Message Format  消息格式

MCP uses [JSON-RPC](https://www.jsonrpc.org/) 2.0 as its wire format. The transport layer is responsible for converting MCP protocol messages into JSON-RPC format for transmission and converting received JSON-RPC messages back into MCP protocol messages.
MCP 使用[JSON-RPC](https://www.jsonrpc.org/) 2.0 作为其传输格式。传输层负责将 MCP 协议消息转换为 JSON-RPC 格式进行传输，并将接收到的 JSON-RPC 消息转换回 MCP 协议消息。

There are three types of JSON-RPC messages used:
使用三种类型的 JSON-RPC 消息：

### Requests  ### 请求

```typescript
{
  jsonrpc: "2.0",
  id: number | string,
  method: string,
  params?: object
}
```

### Responses  ### 响应

```typescript
{
  jsonrpc: "2.0",
  id: number | string,
  result?: object,
  error?: {
    code: number,
    message: string,
    data?: unknown
  }
}
```

### Notifications  ### 通知

```typescript
{
  jsonrpc: "2.0",
  method: string,
  params?: object
}
```

## Built-in Transport Types
## 内置传输类型

MCP includes two standard transport implementations:
MCP 包含两种标准传输实现：

### Standard Input/Output (stdio)
### 标准输入/输出（stdio）

The stdio transport enables communication through standard input and output streams. This is particularly useful for local integrations and command-line tools.
stdio 传输允许通过标准输入和输出流进行通信。这对于本地集成和命令行工具特别有用。

Use stdio when:  在以下情况下使用 stdio：

* Building command-line tools
* Implementing local integrations
* Needing simple process communication
* Working with shell scripts
* 构建命令行工具 * 实现本地集成 * 需要简单的进程通信 * 与 shell 脚本一起工作

<Tabs>
  <Tab title="TypeScript (Server)">
    ```typescript
    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {}
    });
  ```typescript const server = new Server({ name: "example-server", version: "1.0.0" }, { capabilities: {} });

    const transport = new StdioServerTransport();
    await server.connect(transport);
    ```
  </Tab>
const transport = new StdioServerTransport(); await server.connect(transport); ```

  <Tab title="TypeScript (Client)">
    ```typescript
    const client = new Client({
      name: "example-client",
      version: "1.0.0"
    }, {
      capabilities: {}
    });

    const transport = new StdioClientTransport({
      command: "./server",
      args: ["--option", "value"]
    });
    await client.connect(transport);
    ```
  </Tab>
const transport = new StdioClientTransport({ command: "./server", args: ["--option", "value"] }); await client.connect(transport); ```

  <Tab title="Python (Server)">
    ```python
    app = Server("example-server")

    async with stdio_server() as streams:
        await app.run(
            streams[0],
            streams[1],
            app.create_initialization_options()
        )
    ```
  </Tab>
async with stdio_server() as streams: await app.run(streams[0], streams[1], app.create_initialization_options()) ``` 

  <Tab title="Python (Client)">
    ```python
    params = StdioServerParameters(
        command="./server",
        args=["--option", "value"]
    )
 ```python params = StdioServerParameters(command="./server", args=["--option", "value"]) 

    async with stdio_client(params) as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()
    ```
  </Tab>
</Tabs>

### Server-Sent Events (SSE)
### 服务器发送事件 (SSE)

SSE transport enables server-to-client streaming with HTTP POST requests for client-to-server communication.
SSE 传输通过 HTTP POST 请求实现服务器到客户端的流式传输，用于客户端到服务器的通信。

Use SSE when:  在以下情况下使用 SSE：

* Only server-to-client streaming is needed
* Working with restricted networks
* Implementing simple updates
* 仅需要服务器到客户端的流式传输 * 在受限网络中工作 * 实现简单更新

#### Security Warning: DNS Rebinding Attacks
#### 安全警告：DNS 重绑定攻击

SSE transports can be vulnerable to DNS rebinding attacks if not properly secured. To prevent this:
SSE 传输可能在不正确安全的情况下容易受到 DNS 重绑定攻击。为了防止这种情况：

1. **Always validate Origin headers** on incoming SSE connections to ensure they come from expected sources
2. **Avoid binding servers to all network interfaces** (0.0.0.0) when running locally - bind only to localhost (127.0.0.1) instead
3. **Implement proper authentication** for all SSE connections
1. **始终验证 Origin 头**，以确保传入的 SSE 连接来自预期的来源 2. **在本地运行时避免将服务器绑定到所有网络接口**（0.0.0.0）- 只绑定到 localhost（127.0.0.1） 3. **为所有 SSE 连接实施适当的身份验证**

Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites.
如果没有这些保护措施，攻击者可能会使用 DNS 重绑定从远程网站与本地 MCP 服务器交互。

<Tabs>
  <Tab title="TypeScript (Server)">
    ```typescript
    import express from "express";
  ```typescript import express from "express";

    const app = express();

    const server = new Server({
      name: "example-server",
      version: "1.0.0"
    }, {
      capabilities: {}
    });

    let transport: SSEServerTransport | null = null;

    app.get("/sse", (req, res) => {
      transport = new SSEServerTransport("/messages", res);
      server.connect(transport);
    });

    app.post("/messages", (req, res) => {
      if (transport) {
        transport.handlePostMessage(req, res);
      }
    });

    app.listen(3000);
    ```
  </Tab>
app.listen(3000);

  <Tab title="TypeScript (Client)">
    ```typescript
    const client = new Client({
      name: "example-client",
      version: "1.0.0"
    }, {
      capabilities: {}
    });

    const transport = new SSEClientTransport(
      new URL("http://localhost:3000/sse")
    );
    await client.connect(transport);
    ```
  </Tab>
const transport = new SSEClientTransport( new URL("http://localhost:3000/sse") ); await client.connect(transport);

  <Tab title="Python (Server)">
    ```python
    from mcp.server.sse import SseServerTransport
    from starlette.applications import Starlette
    from starlette.routing import Route
Python (服务器) ```python from mcp.server.sse import SseServerTransport from starlette.applications import Starlette from starlette.routing import Route

    app = Server("example-server")
    sse = SseServerTransport("/messages")
app = 服务器("example-server") sse = SseServerTransport("/messages")

    async def handle_sse(scope, receive, send):
        async with sse.connect_sse(scope, receive, send) as streams:
            await app.run(streams[0], streams[1], app.create_initialization_options())
异步处理服务器发送事件（SSE）的函数，使用`sse.connect_sse`连接 SSE 流，并在连接上下文中运行应用程序。

    async def handle_messages(scope, receive, send):
        await sse.handle_post_message(scope, receive, send)
异步处理消息（scope，receive，send）：等待 sse.handle_post_message（scope，receive，send）

    starlette_app = Starlette(
        routes=[
            Route("/sse", endpoint=handle_sse),
            Route("/messages", endpoint=handle_messages, methods=["POST"]),
        ]
    )
    ```
  </Tab>
starlette_app = Starlette(路由=[Route("/sse", 端点=handle_sse), Route("/messages", 端点=handle_messages, 方法=["POST"])]) ``` 

  <Tab title="Python (Client)">
    ```python
    async with sse_client("http://localhost:8000/sse") as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()
    ```
  </Tab>
</Tabs>
 ```python async with sse_client("http://localhost:8000/sse") as streams: async with ClientSession(streams[0], streams[1]) as session: await session.initialize() ```  

## Custom Transports  ## 自定义传输

MCP makes it easy to implement custom transports for specific needs. Any transport implementation just needs to conform to the Transport interface:
MCP 使得为特定需求实现自定义传输变得简单。任何传输实现只需符合传输接口：

You can implement custom transports for:
您可以实现自定义传输方式：

* Custom network protocols
* Specialized communication channels
* Integration with existing systems
* Performance optimization
* 自定义网络协议 * 专用通信通道 * 与现有系统集成 * 性能优化

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    interface Transport {
      // Start processing messages
      start(): Promise<void>;
  ```typescript interface Transport { // 开始处理消息 start(): Promise;

      // Send a JSON-RPC message
      send(message: JSONRPCMessage): Promise<void>;
// 发送 JSON-RPC 消息 send(message: JSONRPCMessage): Promise;

      // Close the connection
      close(): Promise<void>;
// 关闭连接 close(): Promise;

      // Callbacks
      onclose?: () => void;
      onerror?: (error: Error) => void;
      onmessage?: (message: JSONRPCMessage) => void;
    }
    ```
  </Tab>
// onclose?: () => void; onerror?: (error: Error) => void; onmessage?: (message: JSONRPCMessage) => void; } ``` 

  <Tab title="Python">
    Note that while MCP Servers are often implemented with asyncio, we recommend
    implementing low-level interfaces like transports with `anyio` for wider compatibility.
 注意虽然 MCP 服务器通常使用 asyncio 实现，但我们建议使用`anyio`实现低级接口，如 transports，以提高兼容性。

    ```python
    @contextmanager
    async def create_transport(
        read_stream: MemoryObjectReceiveStream[JSONRPCMessage | Exception],
        write_stream: MemoryObjectSendStream[JSONRPCMessage]
    ):
        """
        Transport interface for MCP.
```python @contextmanager async def create_transport( read_stream: MemoryObjectReceiveStream[JSONRPCMessage | Exception], write_stream: MemoryObjectSendStream[JSONRPCMessage] ): """ 传输接口用于 MCP。

        Args:
            read_stream: Stream to read incoming messages from
            write_stream: Stream to write outgoing messages to
        """
        async with anyio.create_task_group() as tg:
            try:
                # Start processing messages
                tg.start_soon(lambda: process_messages(read_stream))
Args: read_stream: 从该流读取传入消息 write_stream: 向该流写入传出消息 """ 使用 anyio.create_task_group() 创建任务组，并使用 async with 语句进行异步操作：try: # 启动消息处理过程 tg.start_soon(lambda: process_messages(read_stream))

                # Send messages
                async with write_stream:
                    yield write_stream
# 发送消息 async with write_stream: yield write_stream

            except Exception as exc:
                # Handle errors
                raise exc
            finally:
                # Clean up
                tg.cancel_scope.cancel()
                await write_stream.aclose()
                await read_stream.aclose()
    ```
  </Tab>
</Tabs>
except Exception as exc: # 处理异常 raise exc finally: # 清理资源 tg.cancel_scope.cancel() await write_stream.aclose() await read_stream.aclose() ```  

## Error Handling  ## 错误处理

Transport implementations should handle various error scenarios:
传输实现应处理各种错误场景：

1. Connection errors
2. Message parsing errors
3. Protocol errors
4. Network timeouts
5. Resource cleanup
1. 连接错误 2. 消息解析错误 3. 协议错误 4. 网络超时 5. 资源清理

Example error handling:  示例错误处理：

<Tabs>
  <Tab title="TypeScript">
    ```typescript
    class ExampleTransport implements Transport {
      async start() {
        try {
          // Connection logic
        } catch (error) {
          this.onerror?.(new Error(`Failed to connect: ${error}`));
          throw error;
        }
      }
  ```typescript class ExampleTransport implements Transport { async start() { try { // 连接逻辑 } catch (error) { this.onerror?.(new Error(`连接失败: ${error}`)); throw error; } }

      async send(message: JSONRPCMessage) {
        try {
          // Sending logic
        } catch (error) {
          this.onerror?.(new Error(`Failed to send message: ${error}`));
          throw error;
        }
      }
    }
    ```
  </Tab>
async send(message: JSONRPCMessage) { try { // 发送逻辑 } catch (error) { this.onerror?.(new Error(`Failed to send message: ${error}`)); throw error; } } }

  <Tab title="Python">
    Note that while MCP Servers are often implemented with asyncio, we recommend
    implementing low-level interfaces like transports with `anyio` for wider compatibility.
注意，虽然 MCP 服务器通常使用 asyncio 实现，但我们建议使用`anyio`实现低级接口，如 transports，以提高兼容性。

    ```python
    @contextmanager
    async def example_transport(scope: Scope, receive: Receive, send: Send):
        try:
            # Create streams for bidirectional communication
            read_stream_writer, read_stream = anyio.create_memory_object_stream(0)
            write_stream, write_stream_reader = anyio.create_memory_object_stream(0)
```python @contextmanager async def example_transport(scope: Scope, receive: Receive, send: Send): try: # 创建双向通信的流 read_stream_writer, read_stream = anyio.create_memory_object_stream(0) write_stream, write_stream_reader = anyio.create_memory_object_stream(0)

            async def message_handler():
                try:
                    async with read_stream_writer:
                        # Message handling logic
                        pass
                except Exception as exc:
                    logger.error(f"Failed to handle message: {exc}")
                    raise exc
async def message_handler(): try: async with read_stream_writer: # 消息处理逻辑 pass except Exception as exc: logger.error(f"Failed to handle message: {exc}") raise exc

            async with anyio.create_task_group() as tg:
                tg.start_soon(message_handler)
                try:
                    # Yield streams for communication
                    yield read_stream, write_stream
                except Exception as exc:
                    logger.error(f"Transport error: {exc}")
                    raise exc
                finally:
                    tg.cancel_scope.cancel()
                    await write_stream.aclose()
                    await read_stream.aclose()
        except Exception as exc:
            logger.error(f"Failed to initialize transport: {exc}")
            raise exc
    ```
  </Tab>
</Tabs>
async with anyio.create_task_group() as tg: tg.start_soon(message_handler) try: # Yield streams for communication yield read_stream, write_stream except Exception as exc: logger.error(f"Transport error: {exc}") raise exc finally: tg.cancel_scope.cancel() await write_stream.aclose() await read_stream.aclose() except Exception as exc: logger.error(f"Failed to initialize transport: {exc}") raise exc

## Best Practices  最佳实践

When implementing or using MCP transport:
当实现或使用 MCP 传输时：

1. Handle connection lifecycle properly
2. Implement proper error handling
3. Clean up resources on connection close
4. Use appropriate timeouts
5. Validate messages before sending
6. Log transport events for debugging
7. Implement reconnection logic when appropriate
8. Handle backpressure in message queues
9. Monitor connection health
10. Implement proper security measures
1. 正确处理连接生命周期 2. 实现适当的错误处理 3. 在连接关闭时清理资源 4. 使用适当的超时 5. 在发送消息前验证消息 6. 记录传输事件以供调试 7. 在适当的情况下实现重连逻辑 8. 处理消息队列的背压 9. 监控连接健康状态 10. 实现适当的安全措施

## Security Considerations
安全注意事项

When implementing transport:
实现传输时：

### Authentication and Authorization
### 认证与授权

* Implement proper authentication mechanisms
* Validate client credentials
* Use secure token handling
* Implement authorization checks
* 实现适当的认证机制 * 验证客户端凭证 * 使用安全的令牌处理 * 实现授权检查

### Data Security  ### 数据安全

* Use TLS for network transport
* Encrypt sensitive data
* Validate message integrity
* Implement message size limits
* Sanitize input data
* 使用 TLS 进行网络传输 * 加密敏感数据 * 验证消息完整性 * 实现消息大小限制 * 清洗输入数据

### Network Security  ### 网络安全

* Implement rate limiting
* Use appropriate timeouts
* Handle denial of service scenarios
* Monitor for unusual patterns
* Implement proper firewall rules
* For SSE transports, validate Origin headers to prevent DNS rebinding attacks
* For local SSE servers, bind only to localhost (127.0.0.1) instead of all interfaces (0.0.0.0)
* 实施速率限制 * 使用适当的超时 * 处理拒绝服务场景 * 监控异常模式 * 实施适当的防火墙规则 * 对于 SSE 传输，验证 Origin 头以防止 DNS 重绑定攻击 * 对于本地 SSE 服务器，仅绑定到 localhost（127.0.0.1）而不是所有接口（0.0.0.0）

## Debugging Transport  调试传输

Tips for debugging transport issues:
调试传输问题的技巧：

1. Enable debug logging
2. Monitor message flow
3. Check connection states
4. Validate message formats
5. Test error scenarios
6. Use network analysis tools
7. Implement health checks
8. Monitor resource usage
9. Test edge cases
10. Use proper error tracking
1. 启用调试日志 2. 监控消息流 3. 检查连接状态 4. 验证消息格式 5. 测试错误场景 6. 使用网络分析工具 7. 实施健康检查 8. 监控资源使用 9. 测试边缘情况 10. 使用适当的错误跟踪


# Debugging
Source: https://modelcontextprotocol.io/docs/tools/debugging
# 调试来源: https://modelcontextprotocol.io/docs/tools/debugging

A comprehensive guide to debugging Model Context Protocol (MCP) integrations
全面指南：调试模型上下文协议（MCP）集成

Effective debugging is essential when developing MCP servers or integrating them with applications. This guide covers the debugging tools and approaches available in the MCP ecosystem.
有效的调试对于开发 MCP 服务器或将其与应用程序集成至关重要。本指南涵盖了 MCP 生态系统中可用的调试工具和方法。

<Info>
  This guide is for macOS. Guides for other platforms are coming soon.
</Info>
<信息>本指南适用于 macOS。其他平台的指南即将推出。

## Debugging tools overview
调试工具概述

MCP provides several tools for debugging at different levels:
MCP 提供了不同级别的多个调试工具：

1. **MCP Inspector**
   * Interactive debugging interface
   * Direct server testing
   * See the [Inspector guide](/docs/tools/inspector) for details
1. **MCP Inspector** *交互式调试界面* 直接服务器测试 *查看[Inspector 指南](/docs/tools/inspector)获取详细信息

2. **Claude Desktop Developer Tools**
   * Integration testing
   * Log collection
   * Chrome DevTools integration
2. **Claude 桌面开发者工具** *集成测试* 日志收集 *Chrome DevTools 集成

3. **Server Logging**
   * Custom logging implementations
   * Error tracking
   * Performance monitoring
3. **服务器日志** *自定义日志实现* 错误跟踪 *性能监控

## Debugging in Claude Desktop
## Claude 桌面调试

### Checking server status
### 检查服务器状态

The Claude.app interface provides basic server status information:
Claude.app 界面提供基本的服务器状态信息：

1. Click the <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-plug-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} /> icon to view:
   * Connected servers
   * Available prompts and resources
1. 点击  图标查看：* 已连接的服务器 * 可用的提示和资源

2. Click the <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-hammer-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} /> icon to view:
   * Tools made available to the model
点击  图标查看：* 模型可用的工具

### Viewing logs  ### 查看日志

Review detailed MCP logs from Claude Desktop:
从 Claude 桌面查看详细的 MCP 日志：

```bash
# Follow logs in real-time
tail -n 20 -F ~/Library/Logs/Claude/mcp*.log
```
```bash # 实时跟踪日志 tail -n 20 -F ~/Library/Logs/Claude/mcp*.log ```

The logs capture:  日志捕获：

* Server connection events
* Configuration issues
* Runtime errors
* Message exchanges
* 服务器连接事件 * 配置问题 * 运行时错误 * 消息交换

### Using Chrome DevTools
### 使用 Chrome 开发者工具

Access Chrome's developer tools inside Claude Desktop to investigate client-side errors:
在 Claude 桌面访问 Chrome 开发者工具以调查客户端错误：

1. Create a `developer_settings.json` file with `allowDevTools` set to true:
创建一个将 `allowDevTools` 设置为 true 的 `developer_settings.json` 文件：

```bash
echo '{"allowDevTools": true}' > ~/Library/Application\ Support/Claude/developer_settings.json
```

2. Open DevTools: `Command-Option-Shift-i`
2. 打开开发者工具：`Command-Option-Shift-i`

Note: You'll see two DevTools windows:
注意：您将看到两个开发者工具窗口：

* Main content window
* App title bar window
* 主要内容窗口 * 应用程序标题栏窗口

Use the Console panel to inspect client-side errors.
使用控制台面板检查客户端错误。

Use the Network panel to inspect:
使用网络面板检查：

* Message payloads
* Connection timing
* 消息负载 * 连接时间

## Common issues  ## 常见问题

### Working directory  ### 工作目录

When using MCP servers with Claude Desktop:
当使用 Claude Desktop 与 MCP 服务器一起使用时：

* The working directory for servers launched via `claude_desktop_config.json` may be undefined (like `/` on macOS) since Claude Desktop could be started from anywhere
* Always use absolute paths in your configuration and `.env` files to ensure reliable operation
* For testing servers directly via command line, the working directory will be where you run the command
* 通过 `claude_desktop_config.json` 启动的服务器的工作目录可能未定义（例如 macOS 上的 `/`），因为 Claude Desktop 可以从任何位置启动 * 请始终在您的配置和 `.env` 文件中使用绝对路径以确保可靠运行 * 直接通过命令行测试服务器时，工作目录将是您运行命令的位置

For example in `claude_desktop_config.json`, use:
例如，在 `claude_desktop_config.json` 中，请使用：

```json
{
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username/data"]
}
```

Instead of relative paths like `./data`
而不是相对路径如 `./data`

### Environment variables
### 环境变量

MCP servers inherit only a subset of environment variables automatically, like `USER`, `HOME`, and `PATH`.
MCP 服务器自动继承的环境变量只有一部分，如 `USER`、`HOME` 和 `PATH`。

To override the default variables or provide your own, you can specify an `env` key in `claude_desktop_config.json`:
要覆盖默认变量或提供自己的，您可以在 `claude_desktop_config.json` 中指定一个 `env` 键：

```json
{
  "myserver": {
    "command": "mcp-server-myapp",
    "env": {
      "MYAPP_API_KEY": "some_key",
    }
  }
}
```

### Server initialization
### 服务器初始化

Common initialization problems:
常见初始化问题：

1. **Path Issues**
   * Incorrect server executable path
   * Missing required files
   * Permission problems
   * Try using an absolute path for `command`
1. **路径问题** * 服务器可执行文件路径错误 * 缺少必需文件 * 权限问题 * 尝试使用 `command` 的绝对路径

2. **Configuration Errors**
   * Invalid JSON syntax
   * Missing required fields
   * Type mismatches
2. **配置错误** * 无效的 JSON 语法 * 缺少必需字段 * 类型不匹配

3. **Environment Problems**
   * Missing environment variables
   * Incorrect variable values
   * Permission restrictions
3. **环境问题** * 缺少环境变量 * 变量值不正确 * 权限限制

### Connection problems  ### 连接问题

When servers fail to connect:
当服务器无法连接时：

1. Check Claude Desktop logs
2. Verify server process is running
3. Test standalone with [Inspector](/docs/tools/inspector)
4. Verify protocol compatibility
1. 检查 Claude 桌面日志 2. 验证服务器进程是否正在运行 3. 使用[Inspector](/docs/tools/inspector)进行独立测试 4. 验证协议兼容性

## Implementing logging  ## 实现日志记录

### Server-side logging  ### 服务器端日志记录

When building a server that uses the local stdio [transport](/docs/concepts/transports), all messages logged to stderr (standard error) will be captured by the host application (e.g., Claude Desktop) automatically.
当构建使用本地 stdio [传输](/docs/concepts/transports)的服务器时，所有记录到 stderr（标准错误）的消息将被主机应用程序（例如，Claude 桌面）自动捕获。

<Warning>
  Local MCP servers should not log messages to stdout (standard out), as this will interfere with protocol operation.
</Warning>
<警告>本地 MCP 服务器不应将消息记录到 stdout（标准输出），因为这会干扰协议操作。

For all [transports](/docs/concepts/transports), you can also provide logging to the client by sending a log message notification:
对于所有[传输](/docs/concepts/transports)，您还可以通过发送日志消息通知向客户端提供日志记录：

<Tabs>
  <Tab title="Python">
    ```python
    server.request_context.session.send_log_message(
      level="info",
      data="Server started successfully",
    )
    ```
  </Tab>
<标签> <标签标题="Python"> ```python server.request_context.session.send_log_message( level="info", data="服务器启动成功", ) ``` 

  <Tab title="TypeScript">
    ```typescript
    server.sendLoggingMessage({
      level: "info",
      data: "Server started successfully",
    });
    ```
  </Tab>
</Tabs>
 ```typescript server.sendLoggingMessage({ level: "info", data: "Server started successfully", }); ```  

Important events to log:  需要记录的重要事件：

* Initialization steps
* Resource access
* Tool execution
* Error conditions
* Performance metrics
* 初始化步骤 * 资源访问 * 工具执行 * 错误条件 * 性能指标

### Client-side logging  ### 客户端日志记录

In client applications:  在客户端应用程序中：

1. Enable debug logging
2. Monitor network traffic
3. Track message exchanges
4. Record error states
1. 启用调试日志 2. 监控网络流量 3. 跟踪消息交换 4. 记录错误状态

## Debugging workflow  ## 调试工作流程

### Development cycle  ### 开发周期

1. Initial Development
   * Use [Inspector](/docs/tools/inspector) for basic testing
   * Implement core functionality
   * Add logging points
1. 初始开发 * 使用 [检查器](/docs/tools/inspector) 进行基本测试 * 实现核心功能 * 添加日志点

2. Integration Testing
   * Test in Claude Desktop
   * Monitor logs
   * Check error handling
2. 集成测试 * 在 Claude 桌面测试 * 监控日志 * 检查错误处理

### Testing changes  ### 测试更改

To test changes efficiently:
要高效测试更改：

* **Configuration changes**: Restart Claude Desktop
* **Server code changes**: Use Command-R to reload
* **Quick iteration**: Use [Inspector](/docs/tools/inspector) during development
* **配置更改**: 重启 Claude 桌面 * **服务器代码更改**: 使用 Command-R 重新加载 * **快速迭代**: 在开发期间使用 [检查器](/docs/tools/inspector)

## Best practices  ## 最佳实践

### Logging strategy  ### 日志策略

1. **Structured Logging**
   * Use consistent formats
   * Include context
   * Add timestamps
   * Track request IDs
1. **结构化日志** * 使用一致的格式 * 包含上下文 * 添加时间戳 * 跟踪请求 ID

2. **Error Handling**
   * Log stack traces
   * Include error context
   * Track error patterns
   * Monitor recovery
2. **错误处理** * 记录堆栈跟踪 * 包含错误上下文 * 跟踪错误模式 * 监控恢复

3. **Performance Tracking**
   * Log operation timing
   * Monitor resource usage
   * Track message sizes
   * Measure latency
3. **性能跟踪** * 记录操作时间 * 监控资源使用 * 跟踪消息大小 * 测量延迟

### Security considerations
### 安全考虑

When debugging:  当调试时：

1. **Sensitive Data**
   * Sanitize logs
   * Protect credentials
   * Mask personal information
1. **敏感数据** * 清理日志 * 保护凭证 * 隐藏个人信息

2. **Access Control**
   * Verify permissions
   * Check authentication
   * Monitor access patterns
2. **访问控制** * 核实权限 * 检查身份验证 * 监控访问模式

## Getting help  ## 获取帮助

When encountering issues:
遇到问题时：

1. **First Steps**
   * Check server logs
   * Test with [Inspector](/docs/tools/inspector)
   * Review configuration
   * Verify environment
1. **第一步** * 检查服务器日志 * 使用 [Inspector](/docs/tools/inspector) 进行测试 * 审查配置 * 验证环境

2. **Support Channels**
   * GitHub issues
   * GitHub discussions
2. **支持渠道** * GitHub 问题 * GitHub 讨论

3. **Providing Information**
   * Log excerpts
   * Configuration files
   * Steps to reproduce
   * Environment details
3. **提供信息** * 日志摘录 * 配置文件 * 复现步骤 * 环境详情

## Next steps  ## 下一步

<CardGroup cols={2}>
  <Card title="MCP Inspector" icon="magnifying-glass" href="/docs/tools/inspector">
    Learn to use the MCP Inspector
  </Card>
</CardGroup>
 学习使用 MCP 检查器 


# Inspector
Source: https://modelcontextprotocol.io/docs/tools/inspector
# 检查器来源：https://modelcontextprotocol.io/docs/tools/inspector

In-depth guide to using the MCP Inspector for testing and debugging Model Context Protocol servers
使用 MCP 检查器进行测试和调试模型上下文协议服务器的深入指南

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is an interactive developer tool for testing and debugging MCP servers. While the [Debugging Guide](/docs/tools/debugging) covers the Inspector as part of the overall debugging toolkit, this document provides a detailed exploration of the Inspector's features and capabilities.
[MCP 检查器](https://github.com/modelcontextprotocol/inspector)是一个用于测试和调试 MCP 服务器的交互式开发者工具。虽然[调试指南](/docs/tools/debugging)将检查器作为整体调试工具集的一部分进行介绍，但本文件提供了对检查器功能和特性的详细探讨。

## Getting started  开始指南

### Installation and basic usage
安装与基本使用

The Inspector runs directly through `npx` without requiring installation:
检查器可以直接通过 `npx` 运行，无需安装：

```bash
npx @modelcontextprotocol/inspector <command>
```

```bash
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>
```

#### Inspecting servers from NPM or PyPi
#### 从 NPM 或 PyPi 检查服务器

A common way to start server packages from [NPM](https://npmjs.com) or [PyPi](https://pypi.com).
从 [NPM](https://npmjs.com) 或 [PyPi](https://pypi.com) 启动服务器包的常见方法。

<Tabs>
  <Tab title="NPM package">
    ```bash
    npx -y @modelcontextprotocol/inspector npx <package-name> <args>
    # For example
    npx -y @modelcontextprotocol/inspector npx server-postgres postgres://127.0.0.1/testdb
    ```
  </Tab>
  ```bash npx -y @modelcontextprotocol/inspector npx   # 例如 npx -y @modelcontextprotocol/inspector npx server-postgres postgres://127.0.0.1/testdb ``` 

  <Tab title="PyPi package">
    ```bash
    npx @modelcontextprotocol/inspector uvx <package-name> <args>
    # For example
    npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git
    ```
  </Tab>
</Tabs>
 ```bash npx @modelcontextprotocol/inspector uvx <包名> <参数> # 例如 npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git ```  

#### Inspecting locally developed servers
#### 本地开发服务器检查

To inspect servers locally developed or downloaded as a repository, the most common
way is:
要检查本地开发或作为仓库下载的服务器，最常见的方法是：

<Tabs>
  <Tab title="TypeScript">
    ```bash
    npx @modelcontextprotocol/inspector node path/to/server/index.js args...
    ```
  </Tab>
  ```bash npx @modelcontextprotocol/inspector node 路径/to/server/index.js 参数... ``` 

  <Tab title="Python">
    ```bash
    npx @modelcontextprotocol/inspector \
      uv \
      --directory path/to/server \
      run \
      package-name \
      args...
    ```
  </Tab>
</Tabs>
 ```bash npx @modelcontextprotocol/inspector \ uv \ --directory path/to/server \ run \ package-name \ args... ```  

Please carefully read any attached README for the most accurate instructions.
请仔细阅读任何附带的 README 文件，以获取最准确的说明。

## Feature overview  ## 功能概述

<Frame caption="The MCP Inspector interface">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/mcp-inspector.png" />
</Frame>
  

The Inspector provides several features for interacting with your MCP server:
检查员提供了与您的 MCP 服务器交互的多个功能：

### Server connection pane
### 服务器连接面板

* Allows selecting the [transport](/docs/concepts/transports) for connecting to the server
* For local servers, supports customizing the command-line arguments and environment
* 允许选择[传输方式](/docs/concepts/transports)以连接到服务器 * 对于本地服务器，支持自定义命令行参数和环境变量

### Resources tab  ### 资源标签页

* Lists all available resources
* Shows resource metadata (MIME types, descriptions)
* Allows resource content inspection
* Supports subscription testing
列出所有可用资源 显示资源元数据（MIME 类型、描述） 允许检查资源内容 支持订阅测试

### Prompts tab  ### 提示标签页

* Displays available prompt templates
* Shows prompt arguments and descriptions
* Enables prompt testing with custom arguments
* Previews generated messages
* 显示可用的提示模板 显示提示参数和描述 允许使用自定义参数进行提示测试 预览生成的消息

### Tools tab  ### 工具标签页

* Lists available tools
* Shows tool schemas and descriptions
* Enables tool testing with custom inputs
* Displays tool execution results
* 可用工具列表 * 显示工具模式和描述 * 允许使用自定义输入进行工具测试 * 显示工具执行结果

### Notifications pane  ### 通知面板

* Presents all logs recorded from the server
* Shows notifications received from the server
* 展示服务器记录的所有日志 * 显示从服务器接收到的通知

## Best practices  ## 最佳实践

### Development workflow  ### 开发工作流程

1. Start Development
   * Launch Inspector with your server
   * Verify basic connectivity
   * Check capability negotiation
1. 开始开发 * 启动服务器上的 Inspector * 验证基本连接性 * 检查能力协商

2. Iterative testing
   * Make server changes
   * Rebuild the server
   * Reconnect the Inspector
   * Test affected features
   * Monitor messages
2. 迭代测试 * 修改服务器 * 重新构建服务器 * 重新连接 Inspector * 测试受影响的功能 * 监控消息

3. Test edge cases
   * Invalid inputs
   * Missing prompt arguments
   * Concurrent operations
   * Verify error handling and error responses
3. 测试边缘情况 * 无效输入 * 缺少提示参数 * 并发操作 * 验证错误处理和错误响应

## Next steps  下一步

<CardGroup cols={2}>
  <Card title="Inspector Repository" icon="github" href="https://github.com/modelcontextprotocol/inspector">
    Check out the MCP Inspector source code
  </Card>
 查看 MCP 检查员源代码 

  <Card title="Debugging Guide" icon="bug" href="/docs/tools/debugging">
    Learn about broader debugging strategies
  </Card>
</CardGroup>
了解更广泛的调试策略 


# Example Servers
Source: https://modelcontextprotocol.io/examples
# 示例服务器来源：https://modelcontextprotocol.io/examples

A list of example servers and implementations
服务器和实现示例列表

This page showcases various Model Context Protocol (MCP) servers that demonstrate the protocol's capabilities and versatility. These servers enable Large Language Models (LLMs) to securely access tools and data sources.
本页面展示了各种模型上下文协议（MCP）服务器，这些服务器展示了协议的功能和多样性。这些服务器使大型语言模型（LLMs）能够安全地访问工具和数据源。

## Reference implementations
## 参考实现

These official reference servers demonstrate core MCP features and SDK usage:
这些官方参考服务器展示了 MCP 的核心功能和 SDK 的使用：

### Data and file systems
### 数据和文件系统

* **[Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** - Secure file operations with configurable access controls
* **[PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)** - Read-only database access with schema inspection capabilities
* **[SQLite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)** - Database interaction and business intelligence features
* **[Google Drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive)** - File access and search capabilities for Google Drive
* **[文件系统](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** - 可配置访问控制的加密文件操作 * **[PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)** - 具有模式检查功能的只读数据库访问 * **[SQLite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)** - 数据库交互和商业智能功能 * **[Google Drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive)** - Google Drive 的文件访问和搜索功能

### Development tools  ### 开发工具

* **[Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** - Tools to read, search, and manipulate Git repositories
* **[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/github)** - Repository management, file operations, and GitHub API integration
* **[GitLab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab)** - GitLab API integration enabling project management
* **[Sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry)** - Retrieving and analyzing issues from Sentry.io
* **[Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** - 用于读取、搜索和操作 Git 仓库的工具 * **[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/github)** - 仓库管理、文件操作和 GitHub API 集成 * **[GitLab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab)** - GitLab API 集成，实现项目管理 * **[Sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry)** - 从 Sentry.io 检索和分析问题

### Web and browser automation
### 网页和浏览器自动化

* **[Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)** - Web and local search using Brave's Search API
* **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** - Web content fetching and conversion optimized for LLM usage
* **[Puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)** - Browser automation and web scraping capabilities
* **[Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)** - 使用 Brave 的 Search API 进行网页和本地搜索 * **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** - 优化于LLM使用的网页内容获取和转换 * **[Puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)** - 浏览器自动化和网络爬虫功能

### Productivity and communication
### 生产力与沟通

* **[Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)** - Channel management and messaging capabilities
* **[Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps)** - Location services, directions, and place details
* **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** - Knowledge graph-based persistent memory system
* **[Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)** - 频道管理和消息功能 * **[Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps)** - 位置服务、路线和地点详情 * **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** - 基于知识图谱的持久内存系统

### AI and specialized tools
### 人工智能和专用工具

* **[EverArt](https://github.com/modelcontextprotocol/servers/tree/main/src/everart)** - AI image generation using various models
* **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** - Dynamic problem-solving through thought sequences
* **[AWS KB Retrieval](https://github.com/modelcontextprotocol/servers/tree/main/src/aws-kb-retrieval-server)** - Retrieval from AWS Knowledge Base using Bedrock Agent Runtime
* **[EverArt](https://github.com/modelcontextprotocol/servers/tree/main/src/everart)** - 使用各种模型进行 AI 图像生成 * **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** - 通过思维序列进行动态问题解决 * **[AWS KB Retrieval](https://github.com/modelcontextprotocol/servers/tree/main/src/aws-kb-retrieval-server)** - 使用 Bedrock Agent Runtime 从 AWS 知识库检索

## Official integrations  ## 官方集成

These MCP servers are maintained by companies for their platforms:
这些 MCP 服务器由公司为其平台维护：

* **[Axiom](https://github.com/axiomhq/mcp-server-axiom)** - Query and analyze logs, traces, and event data using natural language
* **[Browserbase](https://github.com/browserbase/mcp-server-browserbase)** - Automate browser interactions in the cloud
* **[Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - Deploy and manage resources on the Cloudflare developer platform
* **[E2B](https://github.com/e2b-dev/mcp-server)** - Execute code in secure cloud sandboxes
* **[Neon](https://github.com/neondatabase/mcp-server-neon)** - Interact with the Neon serverless Postgres platform
* **[Obsidian Markdown Notes](https://github.com/calclavia/mcp-obsidian)** - Read and search through Markdown notes in Obsidian vaults
* **[Qdrant](https://github.com/qdrant/mcp-server-qdrant/)** - Implement semantic memory using the Qdrant vector search engine
* **[Raygun](https://github.com/MindscapeHQ/mcp-server-raygun)** - Access crash reporting and monitoring data
* **[Search1API](https://github.com/fatwang2/search1api-mcp)** - Unified API for search, crawling, and sitemaps
* **[Stripe](https://github.com/stripe/agent-toolkit)** - Interact with the Stripe API
* **[Tinybird](https://github.com/tinybirdco/mcp-tinybird)** - Interface with the Tinybird serverless ClickHouse platform
* **[Weaviate](https://github.com/weaviate/mcp-server-weaviate)** - Enable Agentic RAG through your Weaviate collection(s)
* **[Axiom](https://github.com/axiomhq/mcp-server-axiom)** - 使用自然语言查询和分析日志、跟踪和事件数据 * **[Browserbase](https://github.com/browserbase/mcp-server-browserbase)** - 在云端自动化浏览器交互 * **[Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - 在 Cloudflare 开发者平台上部署和管理资源 * **[E2B](https://github.com/e2b-dev/mcp-server)** - 在安全的云沙箱中执行代码 * **[Neon](https://github.com/neondatabase/mcp-server-neon)** - 与 Neon 无服务器 Postgres 平台交互 * **[Obsidian Markdown Notes](https://github.com/calclavia/mcp-obsidian)** - 在 Obsidian 保险库中阅读和搜索 Markdown 笔记 * **[Qdrant](https://github.com/qdrant/mcp-server-qdrant/)** - 使用 Qdrant 向量搜索引擎实现语义记忆 * **[Raygun](https://github.com/MindscapeHQ/mcp-server-raygun)** - 访问崩溃报告和监控数据 * **[Search1API](https://github.com/fatwang2/search1api-mcp)** - 搜索、爬取和网站图的统一 API * **[Stripe](https://github.com/stripe/agent-toolkit)** - 与 Stripe API 交互 * **[Tinybird](https://github.com/tinybirdco/mcp-tinybird)** - 与 Tinybird 无服务器 ClickHouse 平台接口 * **[Weaviate](https://github.com/weaviate/mcp-server-weaviate)** - 通过您的 Weaviate 集合（们）启用 Agentic RAG

## Community highlights  ## 社区亮点

A growing ecosystem of community-developed servers extends MCP's capabilities:
一个不断增长的社区开发服务器生态系统扩展了 MCP 的功能：

* **[Docker](https://github.com/ckreiling/mcp-server-docker)** - Manage containers, images, volumes, and networks
* **[Kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - Manage pods, deployments, and services
* **[Linear](https://github.com/jerhadf/linear-mcp-server)** - Project management and issue tracking
* **[Snowflake](https://github.com/datawiz168/mcp-snowflake-service)** - Interact with Snowflake databases
* **[Spotify](https://github.com/varunneal/spotify-mcp)** - Control Spotify playback and manage playlists
* **[Todoist](https://github.com/abhiz123/todoist-mcp-server)** - Task management integration
* **[Docker](https://github.com/ckreiling/mcp-server-docker)** - 管理容器、镜像、卷和网络 * **[Kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - 管理 Pod、部署和服务 * **[Linear](https://github.com/jerhadf/linear-mcp-server)** - 项目管理和问题跟踪 * **[Snowflake](https://github.com/datawiz168/mcp-snowflake-service)** - 与 Snowflake 数据库交互 * **[Spotify](https://github.com/varunneal/spotify-mcp)** - 控制 Spotify 播放和管理播放列表 * **[Todoist](https://github.com/abhiz123/todoist-mcp-server)** - 任务管理集成

> **Note:** Community servers are untested and should be used at your own risk. They are not affiliated with or endorsed by Anthropic.
**注意：**社区服务器未经测试，请自行承担使用风险。它们与 Anthropic 无关，也不受其支持或认可。

For a complete list of community servers, visit the [MCP Servers Repository](https://github.com/modelcontextprotocol/servers).
欲获取社区服务器的完整列表，请访问[MCP 服务器仓库](https://github.com/modelcontextprotocol/servers)。

## Getting started  ## 开始使用

### Using reference servers
### 使用参考服务器

TypeScript-based servers can be used directly with `npx`:
基于 TypeScript 的服务器可以直接使用 `npx`:

```bash
npx -y @modelcontextprotocol/server-memory
```

Python-based servers can be used with `uvx` (recommended) or `pip`:
基于 Python 的服务器可以使用 `uvx`（推荐）或 `pip`:

```bash
# Using uvx
uvx mcp-server-git
```bash # 使用 uvx uvx mcp-server-git

# Using pip
pip install mcp-server-git
python -m mcp_server_git
```
使用 pip 安装 mcp-server-git

### Configuring with Claude
使用 Claude 进行配置

To use an MCP server with Claude, add it to your configuration:
要使用 Claude 的 MCP 服务器，请将其添加到您的配置中：

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
      }
    }
  }
}
```

## Additional resources  ## 其他资源

* [MCP Servers Repository](https://github.com/modelcontextprotocol/servers) - Complete collection of reference implementations and community servers
* [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - Curated list of MCP servers
* [MCP CLI](https://github.com/wong2/mcp-cli) - Command-line inspector for testing MCP servers
* [MCP Get](https://mcp-get.com) - Tool for installing and managing MCP servers
* [Supergateway](https://github.com/supercorp-ai/supergateway) - Run MCP stdio servers over SSE
* [Zapier MCP](https://zapier.com/mcp) - MCP Server with over 7,000+ apps and 30,000+ actions
* [MCP 服务器仓库](https://github.com/modelcontextprotocol/servers) - 完整的参考实现和社区服务器集合 * [优秀的 MCP 服务器](https://github.com/punkpeye/awesome-mcp-servers) - 精选的 MCP 服务器列表 * [MCP CLI](https://github.com/wong2/mcp-cli) - 用于测试 MCP 服务器的命令行检查器 * [MCP Get](https://mcp-get.com) - 用于安装和管理 MCP 服务器的工具 * [Supergateway](https://github.com/supercorp-ai/supergateway) - 通过 SSE 运行 MCP stdio 服务器 * [Zapier MCP](https://zapier.com/mcp) - 拥有超过 7,000+应用程序和 30,000+操作的 MCP 服务器

Visit our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to engage with the MCP community.
访问我们的[GitHub 讨论区](https://github.com/orgs/modelcontextprotocol/discussions)与 MCP 社区互动。


# FAQs
Source: https://modelcontextprotocol.io/faqs
# 常见问题解答来源：https://modelcontextprotocol.io/faqs

Explaining MCP and why it matters in simple terms
简单易懂地解释 MCP 及其重要性

## What is MCP?  ## 什么是 MCP？

MCP (Model Context Protocol) is a standard way for AI applications and agents to connect to and work with your data sources (e.g. local files, databases, or content repositories) and tools (e.g. GitHub, Google Maps, or Puppeteer).
MCP（模型上下文协议）是 AI 应用和代理连接到并处理您的数据源（例如本地文件、数据库或内容存储库）以及工具（例如 GitHub、Google Maps 或 Puppeteer）的标准方式。

Think of MCP as a universal adapter for AI applications, similar to what USB-C is for physical devices. USB-C acts as a universal adapter to connect devices to various peripherals and accessories. Similarly, MCP provides a standardized way to connect AI applications to different data and tools.
将 MCP 视为 AI 应用的通用适配器，类似于 USB-C 对物理设备的作用。USB-C 作为通用适配器，用于连接设备到各种外围设备和配件。同样，MCP 为 AI 应用连接不同的数据和工具提供了一种标准化方式。

Before USB-C, you needed different cables for different connections. Similarly, before MCP, developers had to build custom connections to each data source or tool they wanted their AI application to work with—a time-consuming process that often resulted in limited functionality. Now, with MCP, developers can easily add connections to their AI applications, making their applications much more powerful from day one.
在 USB-C 出现之前，您需要为不同的连接准备不同的线缆。同样，在 MCP 出现之前，开发者必须为每个他们希望 AI 应用程序与之交互的数据源或工具构建自定义连接——这是一个耗时且往往导致功能受限的过程。现在，有了 MCP，开发者可以轻松地为他们的 AI 应用程序添加连接，使他们的应用程序从第一天起就变得更加强大。

## Why does MCP matter?
## MCP 为何重要？

### For AI application users
### 对于 AI 应用程序用户

MCP means your AI applications can access the information and tools you work with every day, making them much more helpful. Rather than AI being limited to what it already knows about, it can now understand your specific documents, data, and work context.
MCP 意味着您的 AI 应用程序可以访问您每天使用的所有信息和工具，使它们变得更加有用。AI 不再局限于它已经知道的内容，现在它可以理解您特定的文档、数据和工作环境。

For example, by using MCP servers, applications can access your personal documents from Google Drive or data about your codebase from GitHub, providing more personalized and contextually relevant assistance.
例如，通过使用 MCP 服务器，应用程序可以访问您的 Google Drive 中的个人文档或 GitHub 中的代码库数据，从而提供更加个性化和上下文相关的帮助。

Imagine asking an AI assistant: "Summarize last week's team meeting notes and schedule follow-ups with everyone."
想象一下向人工智能助手提问：“总结上周团队会议的笔记并安排与每个人的跟进。”

By using connections to data sources powered by MCP, the AI assistant can:
通过使用由 MCP 提供动力的数据源连接，人工智能助手可以：

* Connect to your Google Drive through an MCP server to read meeting notes
* Understand who needs follow-ups based on the notes
* Connect to your calendar through another MCP server to schedule the meetings automatically
* 通过 MCP 服务器连接到您的 Google Drive 以读取会议笔记 * 根据笔记理解谁需要跟进 * 通过另一个 MCP 服务器连接到您的日历以自动安排会议

### For developers  为开发者

MCP reduces development time and complexity when building AI applications that need to access various data sources. With MCP, developers can focus on building great AI experiences rather than repeatedly creating custom connectors.
MCP 可以减少构建需要访问各种数据源的 AI 应用的开发时间和复杂性。使用 MCP，开发者可以专注于构建优秀的 AI 体验，而不是反复创建自定义连接器。

Traditionally, connecting applications with data sources required building custom, one-off connections for each data source and each application. This created significant duplicative work—every developer wanting to connect their AI application to Google Drive or Slack needed to build their own connection.
传统上，连接应用程序与数据源需要为每个数据源和每个应用程序构建自定义的、一次性的连接。这造成了大量的重复工作——每个希望将他们的 AI 应用程序连接到 Google Drive 或 Slack 的开发者都需要构建自己的连接。

MCP simplifies this by enabling developers to build MCP servers for data sources that are then reusable by various applications. For example, using the open source Google Drive MCP server, many different applications can access data from Google Drive without each developer needing to build a custom connection.
MCP 通过允许开发者为数据源构建 MCP 服务器来简化这一点，这些服务器可以被各种应用程序重用。例如，使用开源的 Google Drive MCP 服务器，许多不同的应用程序都可以访问 Google Drive 中的数据，而无需每个开发者都构建自定义连接。

This open source ecosystem of MCP servers means developers can leverage existing work rather than starting from scratch, making it easier to build powerful AI applications that seamlessly integrate with the tools and data sources their users already rely on.
这套开源的 MCP 服务器生态系统意味着开发者可以利用现有成果，而不是从头开始，从而更容易构建与用户现有工具和数据源无缝集成的强大 AI 应用。

## How does MCP work?
## MCP 是如何工作的？

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/mcp-simple-diagram.png" />
</Frame>

MCP creates a bridge between your AI applications and your data through a straightforward system:
MCP 通过一个简单的系统在您的 AI 应用和您的数据之间架起桥梁：

* **MCP servers** connect to your data sources and tools (like Google Drive or Slack)
* **MCP clients** are run by AI applications (like Claude Desktop) to connect them to these servers
* When you give permission, your AI application discovers available MCP servers
* The AI model can then use these connections to read information and take actions
* **MCP 服务器**连接到您的数据源和工具（如 Google Drive 或 Slack）* **MCP 客户端**由 AI 应用程序（如 Claude 桌面）运行，以连接到这些服务器*当您授权时，您的 AI 应用程序会发现可用的 MCP 服务器*AI 模型可以使用这些连接来读取信息和采取行动

This modular system means new capabilities can be added without changing AI applications themselves—just like adding new accessories to your computer without upgrading your entire system.
这种模块化系统意味着可以在不更改 AI 应用程序本身的情况下添加新功能——就像在不升级整个系统的情况下为您的计算机添加新配件一样。

## Who creates and maintains MCP servers?
## 谁创建和维护 MCP 服务器？

MCP servers are developed and maintained by:
MCP 服务器由以下组织开发和维护：

* Developers at Anthropic who build servers for common tools and data sources
* Open source contributors who create servers for tools they use
* Enterprise development teams building servers for their internal systems
* Software providers making their applications AI-ready
* Anthropic 的工程师们构建通用工具和数据源的服务器 * 为他们使用的工具创建服务器的开源贡献者 * 构建内部系统服务器的企业开发团队 * 使其应用程序 AI 就绪的软件提供商

Once an open source MCP server is created for a data source, it can be used by any MCP-compatible AI application, creating a growing ecosystem of connections. See our [list of example servers](https://modelcontextprotocol.io/examples), or [get started building your own server](https://modelcontextprotocol.io/quickstart/server).
一旦为数据源创建开源 MCP 服务器，它就可以被任何 MCP 兼容的 AI 应用程序使用，从而创建一个不断增长的连接生态系统。查看我们的[示例服务器列表](https://modelcontextprotocol.io/examples)，或[开始构建您自己的服务器](https://modelcontextprotocol.io/quickstart/server)。


# Introduction
Source: https://modelcontextprotocol.io/introduction
# 简介 来源：https://modelcontextprotocol.io/introduction

Get started with the Model Context Protocol (MCP)
开始使用模型上下文协议（MCP）

<Note>C# SDK released! Check out [what else is new.](/development/updates)</Note>
C# SDK 已发布！查看[其他新功能。](/development/updates)

MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.
MCP 是一种开放协议，它标准化了应用程序向LLMs提供上下文的方式。想象一下 MCP 就像 AI 应用的 USB-C 端口。就像 USB-C 为您的设备提供了一种标准化的方式来连接各种外围设备和配件一样，MCP 为 AI 模型连接不同的数据源和工具提供了一种标准化的方式。

## Why MCP?  ## 为什么选择 MCP？

MCP helps you build agents and complex workflows on top of LLMs. LLMs frequently need to integrate with data and tools, and MCP provides:
MCP 帮助您在LLMs上构建代理和复杂的流程。LLMs经常需要与数据和工具集成，MCP 提供：

* A growing list of pre-built integrations that your LLM can directly plug into
* The flexibility to switch between LLM providers and vendors
* Best practices for securing your data within your infrastructure
* 一份不断增长的预构建集成列表，您的 LLM 可以直接接入 * 之间切换 LLM 提供商和供应商的灵活性 * 在您的基础设施内保护数据的安全最佳实践

### General architecture  ### 通用架构

At its core, MCP follows a client-server architecture where a host application can connect to multiple servers:
MCP 的核心采用客户端-服务器架构，其中主机应用程序可以连接到多个服务器：

```mermaid
flowchart LR
    subgraph "Your Computer"
        Host["Host with MCP Client\n(Claude, IDEs, Tools)"]
        S1["MCP Server A"]
        S2["MCP Server B"]
        S3["MCP Server C"]
        Host <-->|"MCP Protocol"| S1
        Host <-->|"MCP Protocol"| S2
        Host <-->|"MCP Protocol"| S3
        S1 <--> D1[("Local\nData Source A")]
        S2 <--> D2[("Local\nData Source B")]
    end
    subgraph "Internet"
        S3 <-->|"Web APIs"| D3[("Remote\nService C")]
    end
```
```mermaid 流程图 LR 子图 "您的计算机" Host["带有 MCP 客户端的宿主\n(Claude, IDEs, 工具)"] S1["MCP 服务器 A"] S2["MCP 服务器 B"] S3["MCP 服务器 C"] Host -->|MCP 协议| S1 Host -->|MCP 协议| S2 Host -->|MCP 协议| S3 S1 --> D1[("本地\n 数据源 A")] S2 --> D2[("本地\n 数据源 B")] end 子图 "互联网" S3 -->|Web APIs| D3[("远程\n 服务 C")] end ```

* **MCP Hosts**: Programs like Claude Desktop, IDEs, or AI tools that want to access data through MCP
* **MCP Clients**: Protocol clients that maintain 1:1 connections with servers
* **MCP Servers**: Lightweight programs that each expose specific capabilities through the standardized Model Context Protocol
* **Local Data Sources**: Your computer's files, databases, and services that MCP servers can securely access
* **Remote Services**: External systems available over the internet (e.g., through APIs) that MCP servers can connect to
* **MCP 主机**: 想要通过 MCP 访问数据的 Claude Desktop、IDE 或 AI 工具 * **MCP 客户端**: 与服务器保持 1:1 连接的协议客户端 * **MCP 服务器**: 每个服务器通过标准化的模型上下文协议公开特定功能的轻量级程序 * **本地数据源**: MCP 服务器可以安全访问的您的计算机文件、数据库和服务 * **远程服务**: MCP 服务器可以连接的互联网上的外部系统（例如，通过 API）

## Get started  ## 开始使用

Choose the path that best fits your needs:
选择最适合您需求的路径：

#### Quick Starts  #### 快速入门

<CardGroup cols={2}>
  <Card title="For Server Developers" icon="bolt" href="/quickstart/server">
    Get started building your own server to use in Claude for Desktop and other clients
  </Card>
  开始构建您自己的服务器，用于 Claude for Desktop 和其他客户端 

  <Card title="For Client Developers" icon="bolt" href="/quickstart/client">
    Get started building your own client that can integrate with all MCP servers
  </Card>
 开始构建自己的客户端，可集成所有 MCP 服务器 

  <Card title="For Claude Desktop Users" icon="bolt" href="/quickstart/user">
    Get started using pre-built servers in Claude for Desktop
  </Card>
</CardGroup>
 开始使用 Claude for Desktop 中的预构建服务器  

#### Examples  #### 示例

<CardGroup cols={2}>
  <Card title="Example Servers" icon="grid" href="/examples">
    Check out our gallery of official MCP servers and implementations
  </Card>
 查看我们的官方 MCP 服务器和实现示例库 

  <Card title="Example Clients" icon="cubes" href="/clients">
    View the list of clients that support MCP integrations
  </Card>
</CardGroup>
查看支持 MCP 集成的客户端列表 

## Tutorials  ## 教程

<CardGroup cols={2}>
  <Card title="Building MCP with LLMs" icon="comments" href="/tutorials/building-mcp-with-llms">
    Learn how to use LLMs like Claude to speed up your MCP development
  </Card>
 学习如何像 Claude 一样使用 LLMs 加速您的 MCP 开发 

  <Card title="Debugging Guide" icon="bug" href="/docs/tools/debugging">
    Learn how to effectively debug MCP servers and integrations
  </Card>
学习如何有效地调试 MCP 服务器和集成

  <Card title="MCP Inspector" icon="magnifying-glass" href="/docs/tools/inspector">
    Test and inspect your MCP servers with our interactive debugging tool
  </Card>
使用我们的交互式调试工具测试和检查您的 MCP 服务器

  <Card title="MCP Workshop (Video, 2hr)" icon="person-chalkboard" href="https://www.youtube.com/watch?v=kQmXtrmQ5Zg">
    <iframe src="https://www.youtube.com/embed/kQmXtrmQ5Zg" />
  </Card>
</CardGroup>
 

## Explore MCP  ## 探索 MCP

Dive deeper into MCP's core concepts and capabilities:
深入了解 MCP 的核心概念和功能：

<CardGroup cols={2}>
  <Card title="Core architecture" icon="sitemap" href="/docs/concepts/architecture">
    Understand how MCP connects clients, servers, and LLMs
  </Card>
  理解 MCP 如何连接客户端、服务器和 LLMs 

  <Card title="Resources" icon="database" href="/docs/concepts/resources">
    Expose data and content from your servers to LLMs
  </Card>
 将您的服务器上的数据和内容公开给 LLMs 

  <Card title="Prompts" icon="message" href="/docs/concepts/prompts">
    Create reusable prompt templates and workflows
  </Card>
 创建可重用的提示模板和工作流程 

  <Card title="Tools" icon="wrench" href="/docs/concepts/tools">
    Enable LLMs to perform actions through your server
  </Card>
 启用 LLMs 通过您的服务器执行操作 

  <Card title="Sampling" icon="robot" href="/docs/concepts/sampling">
    Let your servers request completions from LLMs
  </Card>
 让您的服务器从 LLMs 请求完成 

  <Card title="Transports" icon="network-wired" href="/docs/concepts/transports">
    Learn about MCP's communication mechanism
  </Card>
</CardGroup>
 了解 MCP 的通信机制 

## Contributing  ## 贡献

Want to contribute? Check out our [Contributing Guide](/development/contributing) to learn how you can help improve MCP.
想要贡献？请查看我们的[贡献指南](/development/contributing)，了解如何帮助改进 MCP。

## Support and Feedback  ## 支持和反馈

Here's how to get help or provide feedback:
以下是获取帮助或提供反馈的方法：

* For bug reports and feature requests related to the MCP specification, SDKs, or documentation (open source), please [create a GitHub issue](https://github.com/modelcontextprotocol)
* For discussions or Q\&A about the MCP specification, use the [specification discussions](https://github.com/modelcontextprotocol/specification/discussions)
* For discussions or Q\&A about other MCP open source components, use the [organization discussions](https://github.com/orgs/modelcontextprotocol/discussions)
* For bug reports, feature requests, and questions related to Claude.app and claude.ai's MCP integration, please see Anthropic's guide on [How to Get Support](https://support.anthropic.com/en/articles/9015913-how-to-get-support)
* 对于与 MCP 规范、SDK 或文档（开源）相关的错误报告和功能请求，请[在 GitHub 创建问题](https://github.com/modelcontextprotocol) * 对于关于 MCP 规范的讨论或问答，请使用[规范讨论](https://github.com/modelcontextprotocol/specification/discussions) * 对于关于其他 MCP 开源组件的讨论或问答，请使用[组织讨论](https://github.com/orgs/modelcontextprotocol/discussions) * 对于与 Claude.app 和 claude.ai 的 MCP 集成相关的错误报告、功能请求和问题，请参阅 Anthropic 的[如何获取支持](https://support.anthropic.com/en/articles/9015913-how-to-get-support)指南


# For Client Developers
Source: https://modelcontextprotocol.io/quickstart/client
# For Client Developers 源：https://modelcontextprotocol.io/quickstart/client

Get started building your own client that can integrate with all MCP servers.
开始构建自己的客户端，使其能够与所有 MCP 服务器集成。

In this tutorial, you'll learn how to build a LLM-powered chatbot client that connects to MCP servers. It helps to have gone through the [Server quickstart](/quickstart/server) that guides you through the basic of building your first server.
在本教程中，您将学习如何构建一个由 LLM 驱动的聊天机器人客户端，该客户端可以连接到 MCP 服务器。如果您已经阅读了[服务器快速入门](/quickstart/server)，这将有助于您了解构建第一个服务器的基础知识。

<Tabs>
  <Tab title="Python">
    [You can find the complete code for this tutorial here.](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-python)
  [您可以在以下链接找到本教程的完整代码。](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-python)

    ## System Requirements  系统要求

    Before starting, ensure your system meets these requirements:
在开始之前，请确保您的系统满足以下要求：

    * Mac or Windows computer
    * Latest Python version installed
    * Latest version of `uv` installed
* Mac 或 Windows 计算机 * 已安装最新版本的 Python * 已安装 `uv` 的最新版本

    ## Setting Up Your Environment
设置您的环境

    First, create a new Python project with `uv`:
首先，使用 `uv` 创建一个新的 Python 项目：

    ```bash
    # Create project directory
    uv init mcp-client
    cd mcp-client
```bash # 创建项目目录 uv init mcp-client cd mcp-client

    # Create virtual environment
    uv venv
# 创建虚拟环境 uv venv

    # Activate virtual environment
    # On Windows:
    .venv\Scripts\activate
    # On Unix or MacOS:
    source .venv/bin/activate
# 激活虚拟环境 # 在 Windows 上：.venv\Scripts\activate # 在 Unix 或 MacOS 上：source .venv/bin/activate

    # Install required packages
    uv add mcp anthropic python-dotenv
# 安装所需包 uv add mcp anthropic python-dotenv

    # Remove boilerplate files
    rm main.py
# 删除样板文件 rm main.py

    # Create our main file
    touch client.py
    ```
# 创建我们的主文件 touch client.py

    ## Setting Up Your API Key
## 设置您的 API 密钥

    You'll need an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys).
您需要从[Anthropic 控制台](https://console.anthropic.com/settings/keys)获取一个 Anthropic API 密钥。

    Create a `.env` file to store it:
创建一个`.env`文件来存储它：

    ```bash
    # Create .env file
    touch .env
    ```
```bash # 创建 .env 文件 touch .env ```

    Add your key to the `.env` file:
将您的密钥添加到`.env`文件中：

    ```bash
    ANTHROPIC_API_KEY=<your key here>
    ```
```bash ANTHROPIC_API_KEY=<你的密钥在这里> ```

    Add `.env` to your `.gitignore`:
将 `.env` 添加到你的 `.gitignore` 文件中：

    ```bash
    echo ".env" >> .gitignore
    ```
```bash
echo ".env" >> .gitignore
``` 翻译为：```bash
echo ".env" >> .gitignore
```

    <Warning>
      Make sure you keep your `ANTHROPIC_API_KEY` secure!
    </Warning>
<警告> 确保您保护好您的 `ANTHROPIC_API_KEY`！

    ## Creating the Client
## 创建客户端

    ### Basic Client Structure
### 基本客户端结构

    First, let's set up our imports and create the basic client class:
首先，让我们设置导入并创建基本的客户端类：

    ```python
    import asyncio
    from typing import Optional
    from contextlib import AsyncExitStack
```python 导入 asyncio 模块 from typing import Optional from contextlib import AsyncExitStack

    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
from mcp 导入 ClientSession, StdioServerParameters from mcp.client.stdio 导入 stdio_client

    from anthropic import Anthropic
    from dotenv import load_dotenv
from anthropic 导入 Anthropic from dotenv 导入 load_dotenv

    load_dotenv()  # load environment variables from .env
load_dotenv() # 从 .env 文件中加载环境变量

    class MCPClient:
        def __init__(self):
            # Initialize session and client objects
            self.session: Optional[ClientSession] = None
            self.exit_stack = AsyncExitStack()
            self.anthropic = Anthropic()
        # methods will go here
    ```
class MCPClient: def __init__(self): # 初始化会话和客户端对象 self.session: Optional[ClientSession] = None self.exit_stack = AsyncExitStack() self.anthropic = Anthropic() # 方法将在这里

    ### Server Connection Management
### 服务器连接管理

    Next, we'll implement the method to connect to an MCP server:
接下来，我们将实现连接到 MCP 服务器的函数：

    ```python
    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server
```python async def connect_to_server(self, server_script_path: str): """连接到 MCP 服务器

        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")
Args: server_script_path: 服务器脚本路径（.py 或 .js） """ is_python = server_script_path.endswith('.py') is_js = server_script_path.endswith('.js') if not (is_python or is_js): raise ValueError("服务器脚本必须是 .py 或 .js 文件")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])
    ```
# 列出可用工具的响应 = await self.session.list_tools() tools = response.tools print("\n 连接到服务器，工具列表：", [tool.name for tool in tools]) ```

    ### Query Processing Logic
### 查询处理逻辑

    Now let's add the core functionality for processing queries and handling tool calls:
现在我们为处理查询和处理工具调用添加核心功能：

    ```python
    async def process_query(self, query: str) -> str:
        """Process a query using Claude and available tools"""
        messages = [
            {
                "role": "user",
                "content": query
            }
        ]
```python async def process_query(self, query: str) -> str: """使用 Claude 和可用工具处理查询""" messages = [ { "role": "user", "content": query } ]

        response = await self.session.list_tools()
        available_tools = [{
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        } for tool in response.tools]
response = await self.session.list_tools() 可用工具列表 = [{ "name": tool.name, "description": tool.description, "input_schema": tool.inputSchema } for tool in response.tools]

        # Initial Claude API call
        response = self.anthropic.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=messages,
            tools=available_tools
        )
# 初始 Claude API 调用 response = self.anthropic.messages.create( model="claude-3-5-sonnet-20241022", max_tokens=1000, messages=messages, tools=available_tools )

        # Process response and handle tool calls
        final_text = []
# 处理响应并处理工具调用 最终文本列表 = []

        assistant_message_content = []
        for content in response.content:
            if content.type == 'text':
                final_text.append(content.text)
                assistant_message_content.append(content)
            elif content.type == 'tool_use':
                tool_name = content.name
                tool_args = content.input
助手消息内容列表 = [] for content in response.content: if content.type == 'text': 最终文本列表.append(content.text) 助手消息内容列表.append(content) elif content.type == 'tool_use': 工具名称 = content.name 工具参数 = content.input

                # Execute tool call
                result = await self.session.call_tool(tool_name, tool_args)
                final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")
# 执行工具调用结果 = await self.session.call_tool(tool_name, tool_args) final_text.append(f"[调用工具 {tool_name}，参数 {tool_args}]")

                assistant_message_content.append(content)
                messages.append({
                    "role": "assistant",
                    "content": assistant_message_content
                })
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": content.id,
                            "content": result.content
                        }
                    ]
                })

                # Get next response from Claude
                response = self.anthropic.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1000,
                    messages=messages,
                    tools=available_tools
                )
# 从 Claude 获取下一个响应 response = self.anthropic.messages.create( model="claude-3-5-sonnet-20241022", max_tokens=1000, messages=messages, tools=available_tools )

                final_text.append(response.content[0].text)

        return "\n".join(final_text)
    ```

    ### Interactive Chat Interface
### 交互式聊天界面

    Now we'll add the chat loop and cleanup functionality:
现在我们将添加聊天循环和清理功能：

    ```python
    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")
```python async def chat_loop(self): """运行交互式聊天循环""" print("\nMCP 客户端启动！") print("输入您的查询或输入 'quit' 退出。")

        while True:
            try:
                query = input("\nQuery: ").strip()
while True: 尝试: query = input("\nQuery: ").strip()

                if query.lower() == 'quit':
                    break

                response = await self.process_query(query)
                print("\n" + response)

            except Exception as e:
                print(f"\nError: {str(e)}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()
    ```
async def cleanup(self): """清理资源""" await self.exit_stack.aclose()

    ### Main Entry Point
### 主入口点

    Finally, we'll add the main execution logic:
最后，我们将添加主要的执行逻辑：

    ```python
    async def main():
        if len(sys.argv) < 2:
            print("Usage: python client.py <path_to_server_script>")
            sys.exit(1)
```python async def main(): if len(sys.argv) < 2: print("用法：python client.py <服务器脚本路径>") sys.exit(1)

        client = MCPClient()
        try:
            await client.connect_to_server(sys.argv[1])
            await client.chat_loop()
        finally:
            await client.cleanup()
client = MCPClient() try: 等待 client.connect_to_server(sys.argv[1]) 等待 client.chat_loop() finally: 等待 client.cleanup()

    if __name__ == "__main__":
        import sys
        asyncio.run(main())
    ```
如果 __name__ == "__main__": 导入 sys 等待 asyncio.run(main())

    You can find the complete `client.py` file [here.](https://gist.github.com/zckly/f3f28ea731e096e53b39b47bf0a2d4b1)
您可以在[这里](https://gist.github.com/zckly/f3f28ea731e096e53b39b47bf0a2d4b1)找到完整的 `client.py` 文件。

    ## Key Components Explained
## 关键组件说明

    ### 1. Client Initialization
### 1. 客户端初始化

    * The `MCPClient` class initializes with session management and API clients
    * Uses `AsyncExitStack` for proper resource management
    * Configures the Anthropic client for Claude interactions
* `MCPClient` 类初始化时进行会话管理和 API 客户端配置 * 使用 `AsyncExitStack` 进行适当的资源管理 * 配置 Anthropic 客户端以进行 Claude 交互

    ### 2. Server Connection
### 2. 服务器连接

    * Supports both Python and Node.js servers
    * Validates server script type
    * Sets up proper communication channels
    * Initializes the session and lists available tools
* 支持 Python 和 Node.js 服务器 * 验证服务器脚本类型 * 设置适当的通信通道 * 初始化会话并列出可用工具

    ### 3. Query Processing
### 3. 查询处理

    * Maintains conversation context
    * Handles Claude's responses and tool calls
    * Manages the message flow between Claude and tools
    * Combines results into a coherent response
* 维护对话上下文 * 处理 Claude 的响应和工具调用 * 管理 Claude 与工具之间的消息流 * 将结果组合成连贯的响应

    ### 4. Interactive Interface
### 4. 交互式界面

    * Provides a simple command-line interface
    * Handles user input and displays responses
    * Includes basic error handling
    * Allows graceful exit
* 提供简单的命令行界面 * 处理用户输入并显示响应 * 包含基本的错误处理 * 允许优雅退出

    ### 5. Resource Management
### 5. 资源管理

    * Proper cleanup of resources
    * Error handling for connection issues
    * Graceful shutdown procedures
* 正确清理资源 * 处理连接问题错误 * 实施优雅的关闭程序

    ## Common Customization Points
## 常见自定义点

    1. **Tool Handling**
       * Modify `process_query()` to handle specific tool types
       * Add custom error handling for tool calls
       * Implement tool-specific response formatting
1. **工具处理** * 修改 `process_query()` 以处理特定工具类型 * 为工具调用添加自定义错误处理 * 实现特定工具的响应格式化

    2. **Response Processing**
       * Customize how tool results are formatted
       * Add response filtering or transformation
       * Implement custom logging
2. **响应处理** * 自定义工具结果的格式 * 添加响应过滤或转换 * 实现自定义日志

    3. **User Interface**
       * Add a GUI or web interface
       * Implement rich console output
       * Add command history or auto-completion
3. **用户界面** * 添加图形用户界面或 Web 界面 * 实现丰富的控制台输出 * 添加命令历史记录或自动完成

    ## Running the Client
## 运行客户端

    To run your client with any MCP server:
要运行您的客户端与任何 MCP 服务器：

    ```bash
    uv run client.py path/to/server.py # python server
    uv run client.py path/to/build/index.js # node server
    ```
```bash uv 运行 client.py path/to/server.py # python 服务器 uv 运行 client.py path/to/build/index.js # node 服务器 ```

    <Note>
      If you're continuing the weather tutorial from the server quickstart, your command might look something like this: `python client.py .../quickstart-resources/weather-server-python/weather.py`
    </Note>
<注意> 如果你正在从服务器快速入门教程继续天气教程，你的命令可能看起来像这样：`python client.py .../quickstart-resources/weather-server-python/weather.py` 

    The client will:  客户端将：

    1. Connect to the specified server
    2. List available tools
    3. Start an interactive chat session where you can:
       * Enter queries
       * See tool executions
       * Get responses from Claude
1. 连接到指定的服务器 2. 列出可用的工具 3. 开始一个交互式聊天会话，您可以在其中： * 输入查询 * 查看工具执行 * 从 Claude 获取响应

    Here's an example of what it should look like if connected to the weather server from the server quickstart:
这里是连接到服务器快速入门中的天气服务器应该看起来像什么的一个示例：

    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/client-claude-cli-python.png" />
    </Frame>

    ## How It Works
## 工作原理

    When you submit a query:
当你提交一个查询时：

    1. The client gets the list of available tools from the server
    2. Your query is sent to Claude along with tool descriptions
    3. Claude decides which tools (if any) to use
    4. The client executes any requested tool calls through the server
    5. Results are sent back to Claude
    6. Claude provides a natural language response
    7. The response is displayed to you
1. 客户从服务器获取可用工具列表 2. 您的查询连同工具描述一起发送给 Claude 3. Claude 决定使用哪些工具（如果有） 4. 客户通过服务器执行任何请求的工具调用 5. 结果发送回 Claude 6. Claude 提供自然语言响应 7. 响应显示给您

    ## Best practices  ## 最佳实践

    1. **Error Handling**
       * Always wrap tool calls in try-catch blocks
       * Provide meaningful error messages
       * Gracefully handle connection issues
1. **错误处理** * 总是使用 try-catch 块包装工具调用 * 提供有意义的错误消息 * 优雅地处理连接问题

    2. **Resource Management**
       * Use `AsyncExitStack` for proper cleanup
       * Close connections when done
       * Handle server disconnections
2. **资源管理** * 使用`AsyncExitStack`进行适当的清理 * 完成后关闭连接 * 处理服务器断开连接

    3. **Security**
       * Store API keys securely in `.env`
       * Validate server responses
       * Be cautious with tool permissions
3. **安全** * 在 `.env` 中安全存储 API 密钥 * 验证服务器响应 * 对工具权限保持谨慎

    ## Troubleshooting  ## 故障排除

    ### Server Path Issues
### 服务器路径问题

    * Double-check the path to your server script is correct
    * Use the absolute path if the relative path isn't working
    * For Windows users, make sure to use forward slashes (/) or escaped backslashes (\\) in the path
    * Verify the server file has the correct extension (.py for Python or .js for Node.js)
* 请再次确认您的服务器脚本路径是否正确 * 如果相对路径不起作用，请使用绝对路径 * 对于 Windows 用户，请确保使用正斜杠 (/) 或转义的反斜杠 (\\) 作为路径 * 请验证服务器文件是否具有正确的扩展名 (.py 用于 Python 或 .js 用于 Node.js)

    Example of correct path usage:
正确路径使用示例：

    ```bash
    # Relative path
    uv run client.py ./server/weather.py
```bash # 相对路径 uv run client.py ./server/weather.py

    # Absolute path
    uv run client.py /Users/username/projects/mcp-server/weather.py
# 绝对路径 uv run client.py /Users/username/projects/mcp-server/weather.py

    # Windows path (either format works)
    uv run client.py C:/projects/mcp-server/weather.py
    uv run client.py C:\\projects\\mcp-server\\weather.py
    ```
# Windows 路径（两种格式均可）uv run client.py C:/projects/mcp-server/weather.py uv run client.py C:\\projects\\mcp-server\\weather.py ```

    ### Response Timing  ### 响应时间

    * The first response might take up to 30 seconds to return
    * This is normal and happens while:
      * The server initializes
      * Claude processes the query
      * Tools are being executed
    * Subsequent responses are typically faster
    * Don't interrupt the process during this initial waiting period
* 首次响应可能需要 30 秒才能返回 * 这是正常的，发生在以下情况： * 服务器初始化 * Claude 处理查询 * 执行工具 * 后续响应通常更快 * 在这个初始等待期间请不要中断进程

    ### Common Error Messages
### 常见错误信息

    If you see:  如果您看到：

    * `FileNotFoundError`: Check your server path
    * `Connection refused`: Ensure the server is running and the path is correct
    * `Tool execution failed`: Verify the tool's required environment variables are set
    * `Timeout error`: Consider increasing the timeout in your client configuration
  </Tab>
* `文件未找到错误`：检查您的服务器路径 * `连接被拒绝`：确保服务器正在运行且路径正确 * `工具执行失败`：验证工具所需的环境变量是否已设置 * `超时错误`：考虑在客户端配置中增加超时时间

  <Tab title="Node">
    [You can find the complete code for this tutorial here.](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-typescript)
 [在此处可以找到本教程的完整代码。](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-typescript)

    ## System Requirements  ## 系统要求

    Before starting, ensure your system meets these requirements:
在开始之前，请确保您的系统满足以下要求：

    * Mac or Windows computer
    * Node.js 17 or higher installed
    * Latest version of `npm` installed
    * Anthropic API key (Claude)
* Mac 或 Windows 电脑 * 安装 Node.js 17 或更高版本 * 安装最新版本的`npm` * Anthropic API 密钥（Claude）

    ## Setting Up Your Environment
## 设置您的环境

    First, let's create and set up our project:
首先，让我们创建并设置我们的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # Create project directory
      mkdir mcp-client-typescript
      cd mcp-client-typescript
 ```bash MacOS/Linux # 创建项目目录 mkdir mcp-client-typescript cd mcp-client-typescript

      # Initialize npm project
      npm init -y
初始化 npm 项目 npm init -y

      # Install dependencies
      npm install @anthropic-ai/sdk @modelcontextprotocol/sdk dotenv
安装依赖 npm install @anthropic-ai/sdk @modelcontextprotocol/sdk dotenv

      # Install dev dependencies
      npm install -D @types/node typescript
安装开发依赖 npm install -D @types/node typescript

      # Create source file
      touch index.ts
      ```
创建源文件 touch index.ts

      ```powershell Windows
      # Create project directory
      md mcp-client-typescript
      cd mcp-client-typescript
```powershell Windows # 创建项目目录 md mcp-client-typescript cd mcp-client-typescript

      # Initialize npm project
      npm init -y
# 初始化 npm 项目 npm init -y

      # Install dependencies
      npm install @anthropic-ai/sdk @modelcontextprotocol/sdk dotenv
# 安装依赖 npm install @anthropic-ai/sdk @modelcontextprotocol/sdk dotenv

      # Install dev dependencies
      npm install -D @types/node typescript
# 安装开发依赖 npm install -D @types/node typescript

      # Create source file
      new-item index.ts
      ```
    </CodeGroup>
创建源文件 new-item index.ts ``` 

    Update your `package.json` to set `type: "module"` and a build script:
更新你的 `package.json` 以设置 `type: "module"` 并添加构建脚本：

    ```json package.json
    {
      "type": "module",
      "scripts": {
        "build": "tsc && chmod 755 build/index.js"
      }
    }
    ```

    Create a `tsconfig.json` in the root of your project:
在项目的根目录下创建 `tsconfig.json`：

    ```json tsconfig.json
    {
      "compilerOptions": {
        "target": "ES2022",
        "module": "Node16",
        "moduleResolution": "Node16",
        "outDir": "./build",
        "rootDir": "./",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
      },
      "include": ["index.ts"],
      "exclude": ["node_modules"]
    }
    ```

    ## Setting Up Your API Key
## 设置您的 API 密钥

    You'll need an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys).
您需要从[Anthropic 控制台](https://console.anthropic.com/settings/keys)获取 Anthropic API 密钥。

    Create a `.env` file to store it:
创建一个`.env`文件来存储它：

    ```bash
    echo "ANTHROPIC_API_KEY=<your key here>" > .env
    ```

    Add `.env` to your `.gitignore`:
将 `.env` 添加到你的 `.gitignore` 文件中：

    ```bash
    echo ".env" >> .gitignore
    ```
```bash
echo ".env" >> .gitignore
``` 翻译为：```bash
echo ".env" >> .gitignore
```

    <Warning>
      Make sure you keep your `ANTHROPIC_API_KEY` secure!
    </Warning>
<警告> 确保你的 `ANTHROPIC_API_KEY` 安全！

    ## Creating the Client
## 创建客户端

    ### Basic Client Structure
### 基本客户端结构

    First, let's set up our imports and create the basic client class in `index.ts`:
首先，让我们设置导入并创建基本的客户端类 `index.ts`：

    ```typescript
    import { Anthropic } from "@anthropic-ai/sdk";
    import {
      MessageParam,
      Tool,
    } from "@anthropic-ai/sdk/resources/messages/messages.mjs";
    import { Client } from "@modelcontextprotocol/sdk/client/index.js";
    import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
    import readline from "readline/promises";
    import dotenv from "dotenv";
```typescript
    import { Anthropic } from "@anthropic-ai/sdk";
    import { MessageParam, Tool, } from "@anthropic-ai/sdk/resources/messages/messages.mjs";
    import { Client } from "@modelcontextprotocol/sdk/client/index.js";
    import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
    import readline from "readline/promises";
    import dotenv from "dotenv";
  ```

    dotenv.config();

    const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
    if (!ANTHROPIC_API_KEY) {
      throw new Error("ANTHROPIC_API_KEY is not set");
    }

    class MCPClient {
      private mcp: Client;
      private anthropic: Anthropic;
      private transport: StdioClientTransport | null = null;
      private tools: Tool[] = [];
class MCPClient { private mcp: Client; private anthropic: Anthropic; private transport: StdioClientTransport | null = null; private tools: Tool[] = []; }

      constructor() {
        this.anthropic = new Anthropic({
          apiKey: ANTHROPIC_API_KEY,
        });
        this.mcp = new Client({ name: "mcp-client-cli", version: "1.0.0" });
      }
      // methods will go here
    }
    ```

    ### Server Connection Management
### 服务器连接管理

    Next, we'll implement the method to connect to an MCP server:
接下来，我们将实现连接到 MCP 服务器的功能：

    ```typescript
    async connectToServer(serverScriptPath: string) {
      try {
        const isJs = serverScriptPath.endsWith(".js");
        const isPy = serverScriptPath.endsWith(".py");
        if (!isJs && !isPy) {
          throw new Error("Server script must be a .js or .py file");
        }
        const command = isPy
          ? process.platform === "win32"
            ? "python"
            : "python3"
          : process.execPath;
```typescript async connectToServer(serverScriptPath: string) { try { const isJs = serverScriptPath.endsWith(".js"); const isPy = serverScriptPath.endsWith(".py"); if (!isJs && !isPy) { throw new Error("服务器脚本必须是.js 或.py 文件"); } const command = isPy ? process.platform === "win32" ? "python" : "python3" : process.execPath;

        this.transport = new StdioClientTransport({
          command,
          args: [serverScriptPath],
        });
        this.mcp.connect(this.transport);

        const toolsResult = await this.mcp.listTools();
        this.tools = toolsResult.tools.map((tool) => {
          return {
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
          };
        });
        console.log(
          "Connected to server with tools:",
          this.tools.map(({ name }) => name)
        );
      } catch (e) {
        console.log("Failed to connect to MCP server: ", e);
        throw e;
      }
    }
    ```
const toolsResult = await this.mcp.listTools(); this.tools = toolsResult.tools.map((tool) => { return { name: tool.name, description: tool.description, input_schema: tool.inputSchema, }; }); console.log( "已连接到服务器，工具列表如下:", this.tools.map(({ name }) => name) ); } catch (e) { console.log("连接 MCP 服务器失败: ", e); throw e; } } ```

    ### Query Processing Logic
查询处理逻辑

    Now let's add the core functionality for processing queries and handling tool calls:
现在让我们添加处理查询和处理工具调用的核心功能：

    ```typescript
    async processQuery(query: string) {
      const messages: MessageParam[] = [
        {
          role: "user",
          content: query,
        },
      ];

      const response = await this.anthropic.messages.create({
        model: "claude-3-5-sonnet-20241022",
        max_tokens: 1000,
        messages,
        tools: this.tools,
      });

      const finalText = [];
      const toolResults = [];

      for (const content of response.content) {
        if (content.type === "text") {
          finalText.push(content.text);
        } else if (content.type === "tool_use") {
          const toolName = content.name;
          const toolArgs = content.input as { [x: string]: unknown } | undefined;

          const result = await this.mcp.callTool({
            name: toolName,
            arguments: toolArgs,
          });
          toolResults.push(result);
          finalText.push(
            `[Calling tool ${toolName} with args ${JSON.stringify(toolArgs)}]`
          );
const result = await this.mcp.callTool({ name: toolName, arguments: toolArgs, }); toolResults.push(result); finalText.push( `[调用工具 ${toolName}，参数 ${JSON.stringify(toolArgs)}]` );

          messages.push({
            role: "user",
            content: result.content as string,
          });
messages.push({角色: "用户", 内容: result.content as string, });

          const response = await this.anthropic.messages.create({
            model: "claude-3-5-sonnet-20241022",
            max_tokens: 1000,
            messages,
          });

          finalText.push(
            response.content[0].type === "text" ? response.content[0].text : ""
          );
        }
      }
finalText.push(response.content[0].type === "text" ? response.content[0].text : ""); }

      return finalText.join("\n");
    }
    ```
return finalText.join("\n"); }

    ### Interactive Chat Interface
### 交互式聊天界面

    Now we'll add the chat loop and cleanup functionality:
现在我们将添加聊天循环和清理功能：

    ```typescript
    async chatLoop() {
      const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
      });

      try {
        console.log("\nMCP Client Started!");
        console.log("Type your queries or 'quit' to exit.");
try { console.log("\nMCP 客户端启动！"); console.log("输入您的查询或 '退出' 以退出。");

        while (true) {
          const message = await rl.question("\nQuery: ");
          if (message.toLowerCase() === "quit") {
            break;
          }
          const response = await this.processQuery(message);
          console.log("\n" + response);
        }
      } finally {
        rl.close();
      }
    }
while (true) { const message = await rl.question("\n 查询: "); if (message.toLowerCase() === "quit") { break; } const response = await this.processQuery(message); console.log("\n" + response); } } finally { rl.close(); } }

    async cleanup() {
      await this.mcp.close();
    }
    ```
async cleanup() { await this.mcp.close(); }

    ### Main Entry Point
### 主入口点

    Finally, we'll add the main execution logic:
最后，我们将添加主要的执行逻辑：

    ```typescript
    async function main() {
      if (process.argv.length < 3) {
        console.log("Usage: node index.ts <path_to_server_script>");
        return;
      }
      const mcpClient = new MCPClient();
      try {
        await mcpClient.connectToServer(process.argv[2]);
        await mcpClient.chatLoop();
      } finally {
        await mcpClient.cleanup();
        process.exit(0);
      }
    }

    main();
    ```  main()

    ## Running the Client
## 运行客户端

    To run your client with any MCP server:
要运行您的客户端与任何 MCP 服务器：

    ```bash
    # Build TypeScript
    npm run build
```bash # 构建 TypeScript npm run build

    # Run the client
    node build/index.js path/to/server.py # python server
    node build/index.js path/to/build/index.js # node server
    ```
运行客户端节点 build/index.js path/to/server.py # python server node build/index.js path/to/build/index.js # node server ```

    <Note>
      If you're continuing the weather tutorial from the server quickstart, your command might look something like this: `node build/index.js .../quickstart-resources/weather-server-typescript/build/index.js`
    </Note>
<注意> 如果你正在从服务器快速入门教程继续天气教程，你的命令可能看起来像这样：`node build/index.js .../quickstart-resources/weather-server-typescript/build/index.js` 

    **The client will:**  **客户端将：**

    1. Connect to the specified server
    2. List available tools
    3. Start an interactive chat session where you can:
       * Enter queries
       * See tool executions
       * Get responses from Claude
1. 连接到指定的服务器 2. 列出可用的工具 3. 开始一个交互式聊天会话，您可以在其中： * 输入查询 * 查看工具执行 * 从 Claude 获取响应

    ## How It Works
## 如何工作

    When you submit a query:
当您提交查询时：

    1. The client gets the list of available tools from the server
    2. Your query is sent to Claude along with tool descriptions
    3. Claude decides which tools (if any) to use
    4. The client executes any requested tool calls through the server
    5. Results are sent back to Claude
    6. Claude provides a natural language response
    7. The response is displayed to you
1. 客户从服务器获取可用工具列表 2. 您的查询连同工具描述一起发送给 Claude 3. Claude 决定使用哪些工具（如果有） 4. 客户通过服务器执行任何请求的工具调用 5. 结果发送回 Claude 6. Claude 提供自然语言响应 7. 响应显示给您

    ## Best practices  ## 最佳实践

    1. **Error Handling**
       * Use TypeScript's type system for better error detection
       * Wrap tool calls in try-catch blocks
       * Provide meaningful error messages
       * Gracefully handle connection issues
1. **错误处理** * 使用 TypeScript 的类型系统进行更好的错误检测 * 在工具调用中包裹 try-catch 块 * 提供有意义的错误信息 * 优雅地处理连接问题

    2. **Security**
       * Store API keys securely in `.env`
       * Validate server responses
       * Be cautious with tool permissions
2. **安全** * 在 `.env` 中安全存储 API 密钥 * 验证服务器响应 * 对工具权限保持谨慎

    ## Troubleshooting  ## 故障排除

    ### Server Path Issues
### 服务器路径问题

    * Double-check the path to your server script is correct
    * Use the absolute path if the relative path isn't working
    * For Windows users, make sure to use forward slashes (/) or escaped backslashes (\\) in the path
    * Verify the server file has the correct extension (.js for Node.js or .py for Python)
*请确保您的服务器脚本路径正确* 如果相对路径不起作用，请使用绝对路径 *对于 Windows 用户，请确保使用正斜杠(/)或转义的反斜杠(\\)作为路径* 请验证服务器文件具有正确的扩展名（Node.js 的.js 或 Python 的.py）

    Example of correct path usage:
正确路径使用示例：

    ```bash
    # Relative path
    node build/index.js ./server/build/index.js
```bash # 相对路径 node build/index.js ./server/build/index.js

    # Absolute path
    node build/index.js /Users/username/projects/mcp-server/build/index.js
# 绝对路径 node build/index.js /Users/username/projects/mcp-server/build/index.js

    # Windows path (either format works)
    node build/index.js C:/projects/mcp-server/build/index.js
    node build/index.js C:\\projects\\mcp-server\\build\\index.js
    ```
# Windows 路径（以下两种格式均可）node build/index.js C:/projects/mcp-server/build/index.js node build/index.js C:\projects\mcp-server\build\index.js ```

    ### Response Timing  ### 响应时间

    * The first response might take up to 30 seconds to return
    * This is normal and happens while:
      * The server initializes
      * Claude processes the query
      * Tools are being executed
    * Subsequent responses are typically faster
    * Don't interrupt the process during this initial waiting period
* 第一次响应可能需要 30 秒才能返回 * 这是正常的，发生在以下情况：* 服务器初始化 * Claude 处理查询 * 工具正在执行 * 后续响应通常更快 * 在这个初始等待期间不要中断进程

    ### Common Error Messages
### 常见错误信息

    If you see:  如果您看到：

    * `Error: Cannot find module`: Check your build folder and ensure TypeScript compilation succeeded
    * `Connection refused`: Ensure the server is running and the path is correct
    * `Tool execution failed`: Verify the tool's required environment variables are set
    * `ANTHROPIC_API_KEY is not set`: Check your .env file and environment variables
    * `TypeError`: Ensure you're using the correct types for tool arguments
  </Tab>
* `错误：找不到模块`：检查您的构建文件夹并确保 TypeScript 编译成功 * `连接被拒绝`：确保服务器正在运行且路径正确 * `工具执行失败`：验证工具所需的环境变量是否已设置 * `ANTHROPIC_API_KEY 未设置`：检查您的.env 文件和环境变量 * `TypeError`：确保您为工具参数使用正确的类型

  <Tab title="Java">
    <Note>
      This is a quickstart demo based on Spring AI MCP auto-configuration and boot starters.
      To learn how to create sync and async MCP Clients manually, consult the [Java SDK Client](/sdk/java/mcp-client) documentation
    </Note>
  这是一个基于 Spring AI MCP 自动配置和启动器的快速入门演示。要了解如何手动创建同步和异步 MCP 客户端，请参阅[Java SDK 客户端](/sdk/java/mcp-client)文档 

    This example demonstrates how to build an interactive chatbot that combines Spring AI's Model Context Protocol (MCP) with the [Brave Search MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search). The application creates a conversational interface powered by Anthropic's Claude AI model that can perform internet searches through Brave Search, enabling natural language interactions with real-time web data.
    [You can find the complete code for this tutorial here.](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/web-search/brave-chatbot)
本示例演示了如何构建一个结合 Spring AI 的模型上下文协议（MCP）和[Brave Search MCP 服务器](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)的交互式聊天机器人。该应用程序创建了一个由 Anthropic 的 Claude AI 模型驱动的对话界面，可以通过 Brave Search 执行网络搜索，实现与实时网络数据的自然语言交互。[您可以在本教程中找到完整的代码。](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/web-search/brave-chatbot)

    ## System Requirements  ## 系统要求

    Before starting, ensure your system meets these requirements:
在开始之前，请确保您的系统满足以下要求：

    * Java 17 or higher
    * Maven 3.6+
    * npx package manager
    * Anthropic API key (Claude)
    * Brave Search API key
* Java 17 或更高版本 * Maven 3.6+ * npx 包管理器 * Anthropic API 密钥（Claude） * Brave Search API 密钥

    ## Setting Up Your Environment
配置您的环境

    1. Install npx (Node Package eXecute):
       First, make sure to install [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
       and then run:
       ```bash
       npm install -g npx
       ```
1. 安装 npx (Node Package eXecute)：首先，请确保已安装 [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)，然后运行：```bash npm install -g npx ```

    2. Clone the repository:
       ```bash
       git clone https://github.com/spring-projects/spring-ai-examples.git
       cd model-context-protocol/brave-chatbot
       ```
2. 克隆仓库：```bash git clone https://github.com/spring-projects/spring-ai-examples.git cd model-context-protocol/brave-chatbot ```

    3. Set up your API keys:
       ```bash
       export ANTHROPIC_API_KEY='your-anthropic-api-key-here'
       export BRAVE_API_KEY='your-brave-api-key-here'
       ```
3. 设置您的 API 密钥：```bash export ANTHROPIC_API_KEY='your-anthropic-api-key-here' export BRAVE_API_KEY='your-brave-api-key-here' ```

    4. Build the application:
       ```bash
       ./mvnw clean install
       ```
4. 构建应用程序：```bash ./mvnw clean install ```

    5. Run the application using Maven:
       ```bash
       ./mvnw spring-boot:run
       ```
5. 使用 Maven 运行应用程序：```bash ./mvnw spring-boot:run ```

    <Warning>
      Make sure you keep your `ANTHROPIC_API_KEY` and `BRAVE_API_KEY` keys secure!
    </Warning>
<警告> 确保您保护好 `ANTHROPIC_API_KEY` 和 `BRAVE_API_KEY` 密钥！

    ## How it Works
## 工作原理

    The application integrates Spring AI with the Brave Search MCP server through several components:
该应用程序通过多个组件将 Spring AI 与 Brave Search MCP 服务器集成：

    ### MCP Client Configuration
### MCP 客户端配置

    1. Required dependencies in pom.xml:
1. 在 pom.xml 中必需的依赖项：

    ```xml
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-starter-mcp-client</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-starter-model-anthropic</artifactId>
    </dependency>
    ```

    2. Application properties (application.yml):
2. 应用程序属性（application.yml）

    ```yml
    spring:
      ai:
        mcp:
          client:
            enabled: true
            name: brave-search-client
            version: 1.0.0
            type: SYNC
            request-timeout: 20s
            stdio:
              root-change-notification: true
              servers-configuration: classpath:/mcp-servers-config.json
            toolcallback:
              enabled: true
        anthropic:
          api-key: ${ANTHROPIC_API_KEY}
    ```
spring: ai: mcp: client: 启用: 是 名称: brave-search-client 版本: 1.0.0 类型: 同步 请求超时: 20 秒 标准输入输出: 根目录变更通知: 是 服务器配置: classpath:/mcp-servers-config.json 工具回调: 启用: 是 anthropic: api-key: ${ANTHROPIC_API_KEY}

    This activates the `spring-ai-starter-mcp-client` to create one or more `McpClient`s based on the provided server configuration.
    The `spring.ai.mcp.client.toolcallback.enabled=true` property enables the tool callback mechanism, that automatically registers all MCP tool as spring ai tools.
    It is disabled by default.
此操作激活了`spring-ai-starter-mcp-client`，根据提供的服务器配置创建一个或多个`McpClient`。将`spring.ai.mcp.client.toolcallback.enabled=true`属性启用工具回调机制，该机制自动将所有 MCP 工具注册为 spring ai 工具。默认情况下是禁用的。

    3. MCP Server Configuration (`mcp-servers-config.json`):
3. MCP 服务器配置 (`mcp-servers-config.json`)：

    ```json
    {
      "mcpServers": {
        "brave-search": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-brave-search"
          ],
          "env": {
            "BRAVE_API_KEY": "<PUT YOUR BRAVE API KEY>"
          }
        }
      }
    }
    ```

    ### Chat Implementation  ### 聊天实现

    The chatbot is implemented using Spring AI's ChatClient with MCP tool integration:
聊天机器人采用 Spring AI 的 ChatClient 与 MCP 工具集成实现：

    ```java
    var chatClient = chatClientBuilder
        .defaultSystem("You are useful assistant, expert in AI and Java.")
        .defaultTools((Object[]) mcpToolAdapter.toolCallbacks())
        .defaultAdvisors(new MessageChatMemoryAdvisor(new InMemoryChatMemory()))
        .build();
    ```
```java var chatClient = chatClientBuilder .defaultSystem("您是有用的助手，AI 和 Java 领域的专家。") .defaultTools((Object[]) mcpToolAdapter.toolCallbacks()) .defaultAdvisors(new MessageChatMemoryAdvisor(new InMemoryChatMemory())) .build(); ```

    Key features:  关键特性：

    * Uses Claude AI model for natural language understanding
    * Integrates Brave Search through MCP for real-time web search capabilities
    * Maintains conversation memory using InMemoryChatMemory
    * Runs as an interactive command-line application
* 使用 Claude AI 模型进行自然语言理解 * 通过 MCP 集成 Brave Search 以实现实时网络搜索功能 * 使用 InMemoryChatMemory 保持对话记忆 * 作为交互式命令行应用程序运行

    ### Build and run
### 构建和运行

    ```bash
    ./mvnw clean install
    java -jar ./target/ai-mcp-brave-chatbot-0.0.1-SNAPSHOT.jar
    ```

    or  或者

    ```bash
    ./mvnw spring-boot:run
    ```

    The application will start an interactive chat session where you can ask questions. The chatbot will use Brave Search when it needs to find information from the internet to answer your queries.
应用程序将启动一个交互式聊天会话，您可以在此会话中提问。当聊天机器人需要从互联网上查找信息以回答您的问题时，它将使用 Brave Search。

    The chatbot can:  聊天机器人可以：

    * Answer questions using its built-in knowledge
    * Perform web searches when needed using Brave Search
    * Remember context from previous messages in the conversation
    * Combine information from multiple sources to provide comprehensive answers
使用内置知识回答问题 * 在需要时使用 Brave Search 进行网络搜索 * 记住对话中的上下文 * 从多个来源结合信息以提供全面答案

    ### Advanced Configuration
### 高级配置

    The MCP client supports additional configuration options:
MCP 客户端支持额外的配置选项：

    * Client customization through `McpSyncClientCustomizer` or `McpAsyncClientCustomizer`
    * Multiple clients with multiple transport types: `STDIO` and `SSE` (Server-Sent Events)
    * Integration with Spring AI's tool execution framework
    * Automatic client initialization and lifecycle management
* 通过`McpSyncClientCustomizer`或`McpAsyncClientCustomizer`进行客户端定制 * 支持多种传输类型的多个客户端：`STDIO`和`SSE`（服务器端事件） * 与 Spring AI 的工具执行框架集成 * 自动客户端初始化和生命周期管理

    For WebFlux-based applications, you can use the WebFlux starter instead:
对于基于 WebFlux 的应用程序，您可以使用 WebFlux 启动器：

    ```xml
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-mcp-client-webflux-spring-boot-starter</artifactId>
    </dependency>
    ```

    This provides similar functionality but uses a WebFlux-based SSE transport implementation, recommended for production deployments.
  </Tab>
这提供了类似的功能，但使用基于 WebFlux 的 SSE 传输实现，推荐用于生产部署。

  <Tab title="Kotlin">
    [You can find the complete code for this tutorial here.](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/kotlin-mcp-client)
 [您可以在以下链接找到本教程的完整代码。](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/kotlin-mcp-client)

    ## System Requirements  系统要求

    Before starting, ensure your system meets these requirements:
在开始之前，请确保您的系统满足以下要求：

    * Java 17 or higher
    * Anthropic API key (Claude)
* Java 17 或更高版本 * Anthropic API 密钥（Claude）

    ## Setting up your environment
设置您的环境

    First, let's install `java` and `gradle` if you haven't already.
    You can download `java` from [official Oracle JDK website](https://www.oracle.com/java/technologies/downloads/).
    Verify your `java` installation:
首先，如果您还没有安装，请安装 `java` 和 `gradle`。您可以从 [官方 Oracle JDK 网站](https://www.oracle.com/java/technologies/downloads/) 下载 `java`。验证您的 `java` 安装：

    ```bash
    java --version
    ```

    Now, let's create and set up your project:
现在，让我们创建并设置您的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # Create a new directory for our project
      mkdir kotlin-mcp-client
      cd kotlin-mcp-client
 ```bash MacOS/Linux # 为我们的项目创建一个新的目录 mkdir kotlin-mcp-client cd kotlin-mcp-client

      # Initialize a new kotlin project
      gradle init
      ```
初始化一个新的 Kotlin 项目 gradle init ```

      ```powershell Windows
      # Create a new directory for our project
      md kotlin-mcp-client
      cd kotlin-mcp-client
      # Initialize a new kotlin project
      gradle init
      ```
    </CodeGroup>
```powershell Windows # 为我们的项目创建一个新目录 md kotlin-mcp-client cd kotlin-mcp-client # 初始化一个新的 Kotlin 项目 gradle init ``` 

    After running `gradle init`, you will be presented with options for creating your project.
    Select **Application** as the project type, **Kotlin** as the programming language, and **Java 17** as the Java version.
运行 `gradle init` 后，您将看到创建项目的选项。选择 **应用程序** 作为项目类型，**Kotlin** 作为编程语言，以及 **Java 17** 作为 Java 版本。

    Alternatively, you can create a Kotlin application using the [IntelliJ IDEA project wizard](https://kotlinlang.org/docs/jvm-get-started.html).
或者，您可以使用 [IntelliJ IDEA 项目向导](https://kotlinlang.org/docs/jvm-get-started.html) 创建 Kotlin 应用程序。

    After creating the project, add the following dependencies:
创建项目后，添加以下依赖项：

    <CodeGroup>
      ```kotlin build.gradle.kts
      val mcpVersion = "0.4.0"
      val slf4jVersion = "2.0.9"
      val anthropicVersion = "0.8.0"

      dependencies {
          implementation("io.modelcontextprotocol:kotlin-sdk:$mcpVersion")
          implementation("org.slf4j:slf4j-nop:$slf4jVersion")
          implementation("com.anthropic:anthropic-java:$anthropicVersion")
      }
      ```

      ```groovy build.gradle
      def mcpVersion = '0.3.0'
      def slf4jVersion = '2.0.9'
      def anthropicVersion = '0.8.0'
      dependencies {
          implementation "io.modelcontextprotocol:kotlin-sdk:$mcpVersion"
          implementation "org.slf4j:slf4j-nop:$slf4jVersion"
          implementation "com.anthropic:anthropic-java:$anthropicVersion"
      }
      ```
    </CodeGroup>

    Also, add the following plugins to your build script:
还需要在构建脚本中添加以下插件：

    <CodeGroup>
      ```kotlin build.gradle.kts
      plugins {
          id("com.github.johnrengelman.shadow") version "8.1.1"
      }
      ```
 ```kotlin build.gradle.kts plugins { id("com.github.johnrengelman.shadow") version "8.1.1" } ``` 

      ```groovy build.gradle
      plugins {
          id 'com.github.johnrengelman.shadow' version '8.1.1'
      }
      ```
    </CodeGroup>

    ## Setting up your API key
## 设置你的 API 密钥

    You'll need an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys).
您需要从[Anthropic 控制台](https://console.anthropic.com/settings/keys)获取 Anthropic API 密钥。

    Set up your API key:
设置您的 API 密钥：

    ```bash
    export ANTHROPIC_API_KEY='your-anthropic-api-key-here'
    ```

    <Warning>
      Make sure your keep your `ANTHROPIC_API_KEY` secure!
    </Warning>
<警告>请确保您的`ANTHROPIC_API_KEY`安全！

    ## Creating the Client
创建客户端

    ### Basic Client Structure
### 基本客户端结构

    First, let's create the basic client class:
首先，让我们创建基本客户端类：

    ```kotlin
    class MCPClient : AutoCloseable {
        private val anthropic = AnthropicOkHttpClient.fromEnv()
        private val mcp: Client = Client(clientInfo = Implementation(name = "mcp-client-cli", version = "1.0.0"))
        private lateinit var tools: List<ToolUnion>

        // methods will go here
// 方法将在这里

        override fun close() {
            runBlocking {
                mcp.close()
                anthropic.close()
            }
        }
    ```

    ### Server connection management
### 服务器连接管理

    Next, we'll implement the method to connect to an MCP server:
接下来，我们将实现连接到 MCP 服务器的函数：

    ```kotlin
    suspend fun connectToServer(serverScriptPath: String) {
        try {
            val command = buildList {
                when (serverScriptPath.substringAfterLast(".")) {
                    "js" -> add("node")
                    "py" -> add(if (System.getProperty("os.name").lowercase().contains("win")) "python" else "python3")
                    "jar" -> addAll(listOf("java", "-jar"))
                    else -> throw IllegalArgumentException("Server script must be a .js, .py or .jar file")
                }
                add(serverScriptPath)
            }
```kotlin suspend fun connectToServer(serverScriptPath: String) { try { val command = buildList { when (serverScriptPath.substringAfterLast(".")) { "js" -> add("node") "py" -> add(if (System.getProperty("os.name").lowercase().contains("win")) "python" else "python3") "jar" -> addAll(listOf("java", "-jar")) else -> throw IllegalArgumentException("Server script must be a .js, .py or .jar file") } add(serverScriptPath) }}

            val process = ProcessBuilder(command).start()
            val transport = StdioClientTransport(
                input = process.inputStream.asSource().buffered(),
                output = process.outputStream.asSink().buffered()
            )

            mcp.connect(transport)

            val toolsResult = mcp.listTools()
            tools = toolsResult?.tools?.map { tool ->
                ToolUnion.ofTool(
                    Tool.builder()
                        .name(tool.name)
                        .description(tool.description ?: "")
                        .inputSchema(
                            Tool.InputSchema.builder()
                                .type(JsonValue.from(tool.inputSchema.type))
                                .properties(tool.inputSchema.properties.toJsonValue())
                                .putAdditionalProperty("required", JsonValue.from(tool.inputSchema.required))
                                .build()
                        )
                        .build()
                )
            } ?: emptyList()
            println("Connected to server with tools: ${tools.joinToString(", ") { it.tool().get().name() }}")
        } catch (e: Exception) {
            println("Failed to connect to MCP server: $e")
            throw e
        }
    }
    ```
val toolsResult = mcp.listTools() tools = toolsResult?.tools?.map { tool -> ToolUnion.ofTool( Tool.builder() .name(tool.name) .description(tool.description ?: "") .inputSchema( Tool.InputSchema.builder() .type(JsonValue.from(tool.inputSchema.type)) .properties(tool.inputSchema.properties.toJsonValue()) .putAdditionalProperty("required", JsonValue.from(tool.inputSchema.required)) .build() ) .build() ) } ?: emptyList() println("Connected to server with tools: ${tools.joinToString(", ") { it.tool().get().name() }}") } catch (e: Exception) { println("Failed to connect to MCP server: $e") throw e } }

    Also create a helper function to convert from `JsonObject` to `JsonValue` for Anthropic:
也创建一个辅助函数来将 `JsonObject` 转换为 `JsonValue` 用于 Anthropic:

    ```kotlin
    private fun JsonObject.toJsonValue(): JsonValue {
        val mapper = ObjectMapper()
        val node = mapper.readTree(this.toString())
        return JsonValue.fromJsonNode(node)
    }
    ```

    ### Query processing logic
### 查询处理逻辑

    Now let's add the core functionality for processing queries and handling tool calls:
现在让我们添加处理查询和处理工具调用的核心功能：

    ```kotlin
    private val messageParamsBuilder: MessageCreateParams.Builder = MessageCreateParams.builder()
        .model(Model.CLAUDE_3_5_SONNET_20241022)
        .maxTokens(1024)

    suspend fun processQuery(query: String): String {
        val messages = mutableListOf(
            MessageParam.builder()
                .role(MessageParam.Role.USER)
                .content(query)
                .build()
        )

        val response = anthropic.messages().create(
            messageParamsBuilder
                .messages(messages)
                .tools(tools)
                .build()
        )

        val finalText = mutableListOf<String>()
        response.content().forEach { content ->
            when {
                content.isText() -> finalText.add(content.text().getOrNull()?.text() ?: "")

                content.isToolUse() -> {
                    val toolName = content.toolUse().get().name()
                    val toolArgs =
                        content.toolUse().get()._input().convert(object : TypeReference<Map<String, JsonValue>>() {})

                    val result = mcp.callTool(
                        name = toolName,
                        arguments = toolArgs ?: emptyMap()
                    )
                    finalText.add("[Calling tool $toolName with args $toolArgs]")
val result = mcp.callTool( name = toolName, arguments = toolArgs ?: emptyMap() ) finalText.add("[调用工具 $toolName，参数 $toolArgs]")

                    messages.add(
                        MessageParam.builder()
                            .role(MessageParam.Role.USER)
                            .content(
                                """
                                    "type": "tool_result",
                                    "tool_name": $toolName,
                                    "result": ${result?.content?.joinToString("\n") { (it as TextContent).text ?: "" }}
                                """.trimIndent()
                            )
                            .build()
                    )

                    val aiResponse = anthropic.messages().create(
                        messageParamsBuilder
                            .messages(messages)
                            .build()
                    )

                    finalText.add(aiResponse.content().first().text().getOrNull()?.text() ?: "")
                }
            }
        }

        return finalText.joinToString("\n", prefix = "", postfix = "")
    }
    ```
返回 finalText.joinToString("\n",前缀="",后缀="") } ```

    ### Interactive chat  交互式聊天

    We'll add the chat loop:
我们将添加聊天循环：

    ```kotlin
    suspend fun chatLoop() {
        println("\nMCP Client Started!")
        println("Type your queries or 'quit' to exit.")
```kotlin 懒惰的 fun chatLoop() { println("\nMCP 客户端启动！") println("输入您的查询或输入 'quit' 退出。")

        while (true) {
            print("\nQuery: ")
            val message = readLine() ?: break
            if (message.lowercase() == "quit") break
            val response = processQuery(message)
            println("\n$response")
        }
    }
    ```
while (true) { print("\n 查询： ") val message = readLine() ?: break if (message.lowercase() == "quit") break val response = processQuery(message) println("\n$response") } } ```

    ### Main entry point
### 主入口点

    Finally, we'll add the main execution function:
最后，我们将添加主执行函数：

    ```kotlin
    fun main(args: Array<String>) = runBlocking {
        if (args.isEmpty()) throw IllegalArgumentException("Usage: java -jar <your_path>/build/libs/kotlin-mcp-client-0.1.0-all.jar <path_to_server_script>")
        val serverPath = args.first()
        val client = MCPClient()
        client.use {
            client.connectToServer(serverPath)
            client.chatLoop()
        }
    }
    ```

    ## Running the client
## 运行客户端

    To run your client with any MCP server:
运行您的客户端与任何 MCP 服务器：

    ```bash
    ./gradlew build

    # Run the client
    java -jar build/libs/<your-jar-name>.jar path/to/server.jar # jvm server
    java -jar build/libs/<your-jar-name>.jar path/to/server.py # python server
    java -jar build/libs/<your-jar-name>.jar path/to/build/index.js # node server
    ```
# 运行客户端 java -jar build/libs/.jar path/to/server.jar # JVM 服务器 java -jar build/libs/.jar path/to/server.py # Python 服务器 java -jar build/libs/.jar path/to/build/index.js # Node 服务器 ```

    <Note>
      If you're continuing the weather tutorial from the server quickstart, your command might look something like this: `java -jar build/libs/kotlin-mcp-client-0.1.0-all.jar .../samples/weather-stdio-server/build/libs/weather-stdio-server-0.1.0-all.jar`
    </Note>
<注意>如果您正在从服务器快速入门教程继续天气教程，您的命令可能看起来像这样：`java -jar build/libs/kotlin-mcp-client-0.1.0-all.jar .../samples/weather-stdio-server/build/libs/weather-stdio-server-0.1.0-all.jar` 

    **The client will:**  **客户将：**

    1. Connect to the specified server
    2. List available tools
    3. Start an interactive chat session where you can:
       * Enter queries
       * See tool executions
       * Get responses from Claude
1. 连接到指定的服务器 2. 列出可用工具 3. 开始一个交互式聊天会话，您可以在其中：* 输入查询 * 查看工具执行 * 从 Claude 那里获取响应

    ## How it works
## 工作原理

    Here's a high-level workflow schema:
这里是一个高级工作流程图：

    ```mermaid
    ---
    config:
        theme: neutral
    ---
    sequenceDiagram
        actor User
        participant Client
        participant Claude
        participant MCP_Server as MCP Server
        participant Tools
```mermaid --- config: theme: neutral --- sequenceDiagram actor 用户 participant 客户端 participant 克劳德 participant MCP 服务器 as MCP 服务器 participant 工具

        User->>Client: Send query
        Client<<->>MCP_Server: Get available tools
        Client->>Claude: Send query with tool descriptions
        Claude-->>Client: Decide tool execution
        Client->>MCP_Server: Request tool execution
        MCP_Server->>Tools: Execute chosen tools
        Tools-->>MCP_Server: Return results
        MCP_Server-->>Client: Send results
        Client->>Claude: Send tool results
        Claude-->>Client: Provide final response
        Client-->>User: Display response
    ```
用户->>客户端：发送查询 客户端<<->>MCP 服务器：获取可用工具 客户端->>克劳德：发送带工具描述的查询 克劳德-->>客户端：决定工具执行 客户端->>MCP 服务器：请求执行工具 MCP 服务器->>工具：执行所选工具 工具-->>MCP 服务器：返回结果 MCP 服务器-->>客户端：发送结果 客户端->>克劳德：发送工具结果 克劳德-->>客户端：提供最终响应 客户端->>用户：显示响应 ```

    When you submit a query:
当您提交查询时：

    1. The client gets the list of available tools from the server
    2. Your query is sent to Claude along with tool descriptions
    3. Claude decides which tools (if any) to use
    4. The client executes any requested tool calls through the server
    5. Results are sent back to Claude
    6. Claude provides a natural language response
    7. The response is displayed to you
1. 客户端从服务器获取可用工具列表 2. 您的查询被发送到克劳德，并附带工具描述 3. 克劳德决定使用哪些工具（如果有） 4. 客户端通过服务器执行任何请求的工具调用 5. 结果被发送回克劳德 6. 克劳德提供自然语言响应 7. 响应显示给您

    ## Best practices  最佳实践

    1. **Error Handling**
       * Leverage Kotlin's type system to model errors explicitly
       * Wrap external tool and API calls in `try-catch` blocks when exceptions are possible
       * Provide clear and meaningful error messages
       * Handle network timeouts and connection issues gracefully
1. **错误处理** * 利用 Kotlin 的类型系统显式建模错误 * 当可能抛出异常时，将外部工具和 API 调用包裹在 `try-catch` 块中 * 提供清晰且具有意义的错误信息 * 优雅地处理网络超时和连接问题

    2. **Security**
       * Store API keys and secrets securely in `local.properties`, environment variables, or secret managers
       * Validate all external responses to avoid unexpected or unsafe data usage
       * Be cautious with permissions and trust boundaries when using tools
2. **安全** * 在 `local.properties`、环境变量或密钥管理器中安全地存储 API 密钥和秘密 * 验证所有外部响应以避免意外或不安全的数据使用 * 使用工具时，谨慎处理权限和信任边界

    ## Troubleshooting  ## 故障排除

    ### Server Path Issues
服务器路径问题

    * Double-check the path to your server script is correct
    * Use the absolute path if the relative path isn't working
    * For Windows users, make sure to use forward slashes (/) or escaped backslashes (\\) in the path
    * Make sure that the required runtime is installed (java for Java, npm for Node.js, or uv for Python)
    * Verify the server file has the correct extension (.jar for Java, .js for Node.js or .py for Python)
* 请仔细检查您的服务器脚本路径是否正确 * 如果相对路径不起作用，请使用绝对路径 * 对于 Windows 用户，请确保使用正斜杠（/）或转义的反斜杠（\\）作为路径 * 确保已安装所需的运行时（Java 用于 Java，npm 用于 Node.js，或 uv 用于 Python） * 请验证服务器文件具有正确的扩展名（Java 为.jar，Node.js 为.js，Python 为.py）

    Example of correct path usage:
正确路径使用示例：

    ```bash
    # Relative path
    java -jar build/libs/client.jar ./server/build/libs/server.jar
```bash # 相对路径 java -jar build/libs/client.jar ./server/build/libs/server.jar

    # Absolute path
    java -jar build/libs/client.jar /Users/username/projects/mcp-server/build/libs/server.jar
# 绝对路径 java -jar build/libs/client.jar /Users/username/projects/mcp-server/build/libs/server.jar

    # Windows path (either format works)
    java -jar build/libs/client.jar C:/projects/mcp-server/build/libs/server.jar
    java -jar build/libs/client.jar C:\\projects\\mcp-server\\build\\libs\\server.jar
    ```
# Windows 路径（两种格式均可）java -jar build/libs/client.jar C:/projects/mcp-server/build/libs/server.jar java -jar build/libs/client.jar C:\\projects\\mcp-server\\build\\libs\\server.jar

    ### Response Timing  ### 响应时间

    * The first response might take up to 30 seconds to return
    * This is normal and happens while:
      * The server initializes
      * Claude processes the query
      * Tools are being executed
    * Subsequent responses are typically faster
    * Don't interrupt the process during this initial waiting period
* 第一次响应可能需要 30 秒才能返回 * 这是正常的，发生在以下情况： * 服务器初始化 * Claude 处理查询 * 执行工具 * 后续响应通常更快 * 在这个初始等待期间不要中断进程

    ### Common Error Messages
常见错误信息

    If you see:  如果您看到：

    * `Connection refused`: Ensure the server is running and the path is correct
    * `Tool execution failed`: Verify the tool's required environment variables are set
    * `ANTHROPIC_API_KEY is not set`: Check your environment variables
  </Tab>
* `连接被拒绝`：请确保服务器正在运行且路径正确 * `工具执行失败`：请验证工具所需的环境变量是否已设置 * `ANTHROPIC_API_KEY 未设置`：请检查您的环境变量

  <Tab title="C#">
    [You can find the complete code for this tutorial here.](https://github.io/modelcontextprotocol/csharp-sdk/tree/main/samples/QuickstartClient)
 [您可以在本教程中找到完整的代码。](https://github.io/modelcontextprotocol/csharp-sdk/tree/main/samples/QuickstartClient)

    ## System Requirements  系统要求

    Before starting, ensure your system meets these requirements:
在开始之前，请确保您的系统满足以下要求：

    * .NET 8.0 or higher
    * Anthropic API key (Claude)
    * Windows, Linux, or MacOS
* .NET 8.0 或更高版本 * Anthropic API 密钥（Claude）* Windows、Linux 或 MacOS

    ## Setting up your environment
## 设置您的环境

    First, create a new .NET project:
首先，创建一个新的.NET 项目：

    ```bash
    dotnet new console -n QuickstartClient
    cd QuickstartClient
    ```

    Then, add the required dependencies to your project:
然后，将所需依赖项添加到您的项目中：

    ```bash
    dotnet add package ModelContextProtocol --prerelease
    dotnet add package Anthropic.SDK
    dotnet add package Microsoft.Extensions.Hosting
    ```

    ## Setting up your API key
设置您的 API 密钥

    You'll need an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys).
您需要从[Anthropic 控制台](https://console.anthropic.com/settings/keys)获取 Anthropic API 密钥。

    ```bash
    dotnet user-secrets init
    dotnet user-secrets set "ANTHROPIC_API_KEY" "<your key here>"
    ```

    ## Creating the Client
## 创建客户端

    ### Basic Client Structure
### 基本客户端结构

    First, let's setup the basic client class:
首先，让我们设置基本的客户端类：

    ```csharp
    using Microsoft.Extensions.Configuration;
    using Microsoft.Extensions.Hosting;

    var builder = Host.CreateEmptyApplicationBuilder(settings: null);

    builder.Configuration
        .AddUserSecrets<Program>();
    ```
builder.Configuration.AddUserSecrets();

    This creates the beginnings of a .NET console application that can read the API key from user secrets.
这将创建一个可以读取 API 密钥的.NET 控制台应用程序的初始部分。

    Next, we'll setup the MCP Client:
接下来，我们将设置 MCP 客户端：

    ```csharp
    var (command, arguments) = args switch
    {
        [var script] when script.EndsWith(".py") => ("python", script),
        [var script] when script.EndsWith(".js") => ("node", script),
        [var script] when Directory.Exists(script) || (File.Exists(script) && script.EndsWith(".csproj")) => ("dotnet", $"run --project {script} --no-build"),
        _ => throw new NotSupportedException("An unsupported server script was provided. Supported scripts are .py, .js, or .csproj")
    };
var (command, arguments) = args switch { [var script] when script.EndsWith(".py") => ("python", script), [var script] when script.EndsWith(".js") => ("node", script), [var script] when Directory.Exists(script) || (File.Exists(script) && script.EndsWith(".csproj")) => ("dotnet", $"run --project {script} --no-build"), _ => throw new NotSupportedException("An unsupported server script was provided. Supported scripts are .py, .js, or .csproj") };

    await using var mcpClient = await McpClientFactory.CreateAsync(new()
    {
        Id = "demo-server",
        Name = "Demo Server",
        TransportType = TransportTypes.StdIo,
        TransportOptions = new()
        {
            ["command"] = command,
            ["arguments"] = arguments,
        }
    });
await 使用 var mcpClient = await McpClientFactory.CreateAsync(new() { Id = "demo-server", Name = "Demo Server", TransportType = TransportTypes.StdIo, TransportOptions = new() { ["command"] = command, ["arguments"] = arguments, } });

    var tools = await mcpClient.ListToolsAsync();
    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
    }
    ```

    <Note>
      Be sure to add the `using` statements for the namespaces:
 请确保添加命名空间的使用语句：

      ```csharp
      using ModelContextProtocol.Client;
      using ModelContextProtocol.Protocol.Transport;
      ```
    </Note>

    This configures a MCP client that will connect to a server that is provided as a command line argument. It then lists the available tools from the connected server.
这配置了一个 MCP 客户端，该客户端将连接到作为命令行参数提供的服务器。然后它会列出连接的服务器上的可用工具。

    ### Query processing logic
### 查询处理逻辑

    Now let's add the core functionality for processing queries and handling tool calls:
现在让我们添加处理查询和处理工具调用的核心功能：

    ```csharp
    using IChatClient anthropicClient = new AnthropicClient(new APIAuthentication(builder.Configuration["ANTHROPIC_API_KEY"]))
        .Messages
        .AsBuilder()
        .UseFunctionInvocation()
        .Build();

    var options = new ChatOptions
    {
        MaxOutputTokens = 1000,
        ModelId = "claude-3-5-sonnet-20241022",
        Tools = [.. tools]
    };

    while (true)
    {
        Console.WriteLine("MCP Client Started!");
        Console.WriteLine("Type your queries or 'quit' to exit.");

        string? query = Console.ReadLine();

        if (string.IsNullOrWhiteSpace(query))
        {
            continue;
        }
        if (string.Equals(query, "quit", StringComparison.OrdinalIgnoreCase))
        {
            break;
        }

        var response = anthropicClient.GetStreamingResponseAsync(query, options);

        await foreach (var message in response)
        {
            Console.Write(message.Text);
        }
        Console.WriteLine();
    }
    ```
await foreach (var message in response) { Console.Write(message.Text); } Console.WriteLine(); }

    ## Key Components Explained
## 关键组件说明

    ### 1. Client Initialization
### 1. 客户端初始化

    * The client is initialized using `McpClientFactory.CreateAsync()`, which sets up the transport type and command to run the server.
* 客户端使用 `McpClientFactory.CreateAsync()` 初始化，该函数设置传输类型和要运行的命令。

    ### 2. Server Connection
### 2. 服务器连接

    * Supports Python, Node.js, and .NET servers.
    * The server is started using the command specified in the arguments.
    * Configures to use stdio for communication with the server.
    * Initializes the session and available tools.
* 支持 Python、Node.js 和 .NET 服务器。* 使用参数中指定的命令启动服务器。* 配置使用 stdio 与服务器进行通信。* 初始化会话和可用工具。

    ### 3. Query Processing
### 3. 查询处理

    * Leverages [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/ai-extensions) for the chat client.
    * Configures the `IChatClient` to use automatic tool (function) invocation.
    * The client reads user input and sends it to the server.
    * The server processes the query and returns a response.
    * The response is displayed to the user.
利用 [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/ai-extensions) 为聊天客户端提供支持。* 配置 `IChatClient` 以使用自动工具（函数）调用。* 客户端读取用户输入并将其发送到服务器。* 服务器处理查询并返回响应。* 将响应显示给用户。

    ### Running the Client
### 运行客户端

    To run your client with any MCP server:
要运行您的客户端与任何 MCP 服务器：

    ```bash
    dotnet run -- path/to/server.csproj # dotnet server
    dotnet run -- path/to/server.py # python server
    dotnet run -- path/to/server.js # node server
    ```

    <Note>
      If you're continuing the weather tutorial from the server quickstart, your command might look something like this: `dotnet run -- path/to/QuickstartWeatherServer`.
    </Note>
如果您正在从服务器快速入门继续天气教程，您的命令可能看起来像这样：`dotnet run -- path/to/QuickstartWeatherServer`。

    The client will:  客户端将：

    1. Connect to the specified server
    2. List available tools
    3. Start an interactive chat session where you can:
       * Enter queries
       * See tool executions
       * Get responses from Claude
    4. Exit the session when done
1. 连接到指定的服务器 2. 列出可用的工具 3. 开始一个交互式聊天会话，您可以在其中：* 输入查询 * 查看工具执行 * 获取 Claude 的响应 4. 完成会话后退出

    Here's an example of what it should look like it connected to a weather server quickstart:
下面是一个连接到天气服务器快速入门示例的样子：

    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-dotnet-client.png" />
    </Frame>
  </Tab>
</Tabs>

## Next steps  下一步

<CardGroup cols={2}>
  <Card title="Example servers" icon="grid" href="/examples">
    Check out our gallery of official MCP servers and implementations
  </Card>
  查看我们的官方 MCP 服务器和实现示例库 

  <Card title="Clients" icon="cubes" href="/clients">
    View the list of clients that support MCP integrations
  </Card>
 查看支持 MCP 集成的客户端列表 

  <Card title="Building MCP with LLMs" icon="comments" href="/tutorials/building-mcp-with-llms">
    Learn how to use LLMs like Claude to speed up your MCP development
  </Card>
学习如何像 Claude 一样使用 LLMs 加速您的 MCP 开发

  <Card title="Core architecture" icon="sitemap" href="/docs/concepts/architecture">
    Understand how MCP connects clients, servers, and LLMs
  </Card>
</CardGroup>
了解 MCP 如何连接客户端、服务器和 LLMs


# For Server Developers
Source: https://modelcontextprotocol.io/quickstart/server
# 服务器开发者指南 来源：https://modelcontextprotocol.io/quickstart/server

Get started building your own server to use in Claude for Desktop and other clients.
开始构建您自己的服务器，以便在 Claude 桌面版和其他客户端中使用。

In this tutorial, we'll build a simple MCP weather server and connect it to a host, Claude for Desktop. We'll start with a basic setup, and then progress to more complex use cases.
在本教程中，我们将构建一个简单的 MCP 天气服务器并将其连接到主机，Claude for Desktop。我们将从基本设置开始，然后逐步过渡到更复杂的使用案例。

### What we'll be building
### 我们将构建的内容

Many LLMs do not currently have the ability to fetch the forecast and severe weather alerts. Let's use MCP to solve that!
许多LLMs目前还没有获取预报和恶劣天气警报的能力。让我们使用 MCP 来解决这个问题！

We'll build a server that exposes two tools: `get-alerts` and `get-forecast`. Then we'll connect the server to an MCP host (in this case, Claude for Desktop):
我们将构建一个服务器，该服务器公开了两个工具：`get-alerts`和`get-forecast`。然后我们将服务器连接到 MCP 主机（在这种情况下，Claude for Desktop）：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/weather-alerts.png" />
</Frame>

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/current-weather.png" />
</Frame>

<Note>
  Servers can connect to any client. We've chosen Claude for Desktop here for simplicity, but we also have guides on [building your own client](/quickstart/client) as well as a [list of other clients here](/clients).
</Note>
 服务器可以连接到任何客户端。在这里我们选择了 Claude for Desktop 以简化操作，但我们也有关于[构建自己的客户端](/quickstart/client)的指南，以及[其他客户端列表](/clients)。 

<Accordion title="Why Claude for Desktop and not Claude.ai?">
  Because servers are locally run, MCP currently only supports desktop hosts. Remote hosts are in active development.
</Accordion>
 因为服务器是本地运行的，MCP 目前仅支持桌面主机。远程主机正在积极开发中。 

### Core MCP Concepts  核心 MCP 概念

MCP servers can provide three main types of capabilities:
MCP 服务器可以提供三种主要功能：

1. **Resources**: File-like data that can be read by clients (like API responses or file contents)
2. **Tools**: Functions that can be called by the LLM (with user approval)
3. **Prompts**: Pre-written templates that help users accomplish specific tasks
1. **资源**：客户端可以读取的类似文件的数据（如 API 响应或文件内容）2. **工具**：可以由LLM（经用户同意）调用的函数 3. **提示**：帮助用户完成特定任务的预写模板

This tutorial will primarily focus on tools.
本教程将主要关注工具。

<Tabs>
  <Tab title="Python">
    Let's get started with building our weather server! [You can find the complete code for what we'll be building here.](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-python)
<制表符> <标签标题="Python"> 让我们从构建我们的天气服务器开始！[您可以在以下链接找到我们将要构建的完整代码。](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-python)

    ### Prerequisite knowledge
### 前置知识

    This quickstart assumes you have familiarity with:
本快速入门假设您熟悉：

    * Python
    * LLMs like Claude
* Python * LLMs 像克劳德一样

    ### System requirements  系统要求

    * Python 3.10 or higher installed.
    * You must use the Python MCP SDK 1.2.0 or higher.
* 安装 Python 3.10 或更高版本。* 您必须使用 Python MCP SDK 1.2.0 或更高版本。

    ### Set up your environment
设置您的环境

    First, let's install `uv` and set up our Python project and environment:
首先，让我们安装 `uv` 并设置我们的 Python 项目和环境：

    <CodeGroup>
      ```bash MacOS/Linux
      curl -LsSf https://astral.sh/uv/install.sh | sh
      ```
```bash MacOS/Linux 使用 curl 命令安装 Astral：curl -LsSf https://astral.sh/uv/install.sh | sh ```

      ```powershell Windows
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
      ```
    </CodeGroup>
```powershell Windows 使用 powershell 命令绕过执行策略安装 Astral：powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" ```

    Make sure to restart your terminal afterwards to ensure that the `uv` command gets picked up.
安装完成后，请重启终端以确保`uv`命令生效。

    Now, let's create and set up our project:
现在，让我们创建并设置我们的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # Create a new directory for our project
      uv init weather
      cd weather
```bash MacOS/Linux # 创建我们的项目目录 uv init weather cd weather

      # Create virtual environment and activate it
      uv venv
      source .venv/bin/activate
# 创建虚拟环境并激活它 uv venv source .venv/bin/activate

      # Install dependencies
      uv add "mcp[cli]" httpx
# 安装依赖项 uv add "mcp[cli]" httpx

      # Create our server file
      touch weather.py
      ```
# 创建我们的服务器文件 touch weather.py ```

      ```powershell Windows
      # Create a new directory for our project
      uv init weather
      cd weather
```powershell Windows # 创建我们的项目目录 uv init weather cd weather

      # Create virtual environment and activate it
      uv venv
      .venv\Scripts\activate
# 创建虚拟环境并激活它 uv venv .venv\Scripts\activate

      # Install dependencies
      uv add mcp[cli] httpx
# 安装依赖项 uv add mcp[cli] httpx

      # Create our server file
      new-item weather.py
      ```
    </CodeGroup>
# 创建我们的服务器文件 new-item weather.py ``` 

    Now let's dive into building your server.
现在让我们深入构建您的服务器。

    ## Building your server
## 构建您的服务器

    ### Importing packages and setting up the instance
### 导入包和设置实例

    Add these to the top of your `weather.py`:
在您的 `weather.py` 顶部添加这些：

    ```python
    from typing import Any
    import httpx
    from mcp.server.fastmcp import FastMCP
```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

    # Initialize FastMCP server
    mcp = FastMCP("weather")
# 初始化 FastMCP 服务器 mcp = FastMCP("weather")

    # Constants
    NWS_API_BASE = "https://api.weather.gov"
    USER_AGENT = "weather-app/1.0"
    ```
# 常量 NWS_API_BASE = "https://api.weather.gov" USER_AGENT = "weather-app/1.0" ```

    The FastMCP class uses Python type hints and docstrings to automatically generate tool definitions, making it easy to create and maintain MCP tools.
FastMCP 类使用 Python 类型提示和文档字符串自动生成工具定义，使得创建和维护 MCP 工具变得容易。

    ### Helper functions  辅助函数

    Next, let's add our helper functions for querying and formatting the data from the National Weather Service API:
接下来，让我们添加查询和格式化国家气象服务 API 数据的辅助函数：

    ```python
    async def make_nws_request(url: str) -> dict[str, Any] | None:
        """Make a request to the NWS API with proper error handling."""
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "application/geo+json"
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=headers, timeout=30.0)
                response.raise_for_status()
                return response.json()
            except Exception:
                return None
```python
async def make_nws_request(url: str) -> dict[str, Any] | None: 
    """向 NWS API 发起请求并正确处理错误。"""
    headers = { "User-Agent": USER_AGENT, "Accept": "application/geo+json" }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

    def format_alert(feature: dict) -> str:
        """Format an alert feature into a readable string."""
        props = feature["properties"]
        return f"""
    Event: {props.get('event', 'Unknown')}
    Area: {props.get('areaDesc', 'Unknown')}
    Severity: {props.get('severity', 'Unknown')}
    Description: {props.get('description', 'No description available')}
    Instructions: {props.get('instruction', 'No specific instructions provided')}
    """
    ```
def format_alert(feature: dict) -> str:
    """将警报功能格式化为可读字符串。"""
    props = feature["properties"]
    return f""" 事件: {props.get('event', 'Unknown')} 区域: {props.get('areaDesc', 'Unknown')} 级别: {props.get('severity', 'Unknown')} 描述: {props.get('description', 'No description available')} 指令: {props.get('instruction', 'No specific instructions provided')} """

    ### Implementing tool execution
实现工具执行

    The tool execution handler is responsible for actually executing the logic of each tool. Let's add it:
工具执行处理器负责实际执行每个工具的逻辑。让我们添加它：

    ```python
    @mcp.tool()
    async def get_alerts(state: str) -> str:
        """Get weather alerts for a US state.
```python @mcp.tool() async def get_alerts(state: str) -> str: """获取美国各州的天气警报。

        Args:
            state: Two-letter US state code (e.g. CA, NY)
        """
        url = f"{NWS_API_BASE}/alerts/active/area/{state}"
        data = await make_nws_request(url)
Args: state: 美国两字母州代码（例如：CA，NY） """ url = f"{NWS_API_BASE}/alerts/active/area/{state}" data = await make_nws_request(url)

        if not data or "features" not in data:
            return "Unable to fetch alerts or no alerts found."
如果没有数据或“features”不在数据中，则返回“无法获取警报或未找到警报。”

        if not data["features"]:
            return "No active alerts for this state."
如果没有数据中的“features”，则返回“此状态下没有活动警报。”

        alerts = [format_alert(feature) for feature in data["features"]]
        return "\n---\n".join(alerts)
alerts = [format_alert(feature) for feature in data["features"]] 返回 "\n---\n".join(alerts)

    @mcp.tool()
    async def get_forecast(latitude: float, longitude: float) -> str:
        """Get weather forecast for a location.
@mcp.tool() async def get_forecast(latitude: float, longitude: float) -> str: 获取位置的天气预报。

        Args:
            latitude: Latitude of the location
            longitude: Longitude of the location
        """
        # First get the forecast grid endpoint
        points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
        points_data = await make_nws_request(points_url)
Args: 纬度：位置的纬度 经度：位置的经度 """ # 首先获取预报网格端点 points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}" points_data = await make_nws_request(points_url)

        if not points_data:
            return "Unable to fetch forecast data for this location."

        # Get the forecast URL from the points response
        forecast_url = points_data["properties"]["forecast"]
        forecast_data = await make_nws_request(forecast_url)
# 从端点响应中获取预报 URL forecast_url = points_data["properties"]["forecast"] forecast_data = await make_nws_request(forecast_url)

        if not forecast_data:
            return "Unable to fetch detailed forecast."

        # Format the periods into a readable forecast
        periods = forecast_data["properties"]["periods"]
        forecasts = []
        for period in periods[:5]:  # Only show next 5 periods
            forecast = f"""
    {period['name']}:
    Temperature: {period['temperature']}°{period['temperatureUnit']}
    Wind: {period['windSpeed']} {period['windDirection']}
    Forecast: {period['detailedForecast']}
    """
            forecasts.append(forecast)
|
    # 格式化预报周期 = forecast_data["properties"]["periods"]
    # 预报列表 = []
    # 只显示前 5 个预报周期
    # 预报 = f""" {period['name']}: 温度: {period['temperature']}°{period['temperatureUnit']} 风速: {period['windSpeed']} {period['windDirection']} 预报: {period['detailedForecast']} """
    # 预报列表.append(预报)

        return "\n---\n".join(forecasts)
    ```
|
    return "\n---\n".join(预报列表) ```

    ### Running the server
|
    ### 运行服务器

    Finally, let's initialize and run the server:
|
    最后，让我们初始化并运行服务器：

    ```python
    if __name__ == "__main__":
        # Initialize and run the server
        mcp.run(transport='stdio')
    ```
```python if __name__ == "__main__": # 初始化并运行服务器 mcp.run(transport='stdio') ```

    Your server is complete! Run `uv run weather.py` to confirm that everything's working.
服务器已完成！运行 `uv run weather.py` 以确认一切正常工作。

    Let's now test your server from an existing MCP host, Claude for Desktop.
现在让我们从现有的 MCP 主机，Claude for Desktop，测试你的服务器。

    ## Testing your server with Claude for Desktop
## 使用 Claude for Desktop 测试你的服务器

    <Note>
      Claude for Desktop is not yet available on Linux. Linux users can proceed to the [Building a client](/quickstart/client) tutorial to build an MCP client that connects to the server we just built.
    </Note>
 Claude for Desktop 在 Linux 上尚未提供。Linux 用户可以前往 [构建客户端](/quickstart/client) 教程，以构建一个连接到我们刚刚构建的服务器的 MCP 客户端。

    First, make sure you have Claude for Desktop installed. [You can install the latest version
    here.](https://claude.ai/download) If you already have Claude for Desktop, **make sure it's updated to the latest version.**
首先，请确保您已安装 Claude for Desktop。[您可以从这里安装最新版本。](https://claude.ai/download) 如果您已经安装了 Claude for Desktop，**请确保它已更新到最新版本。**

    We'll need to configure Claude for Desktop for whichever MCP servers you want to use. To do this, open your Claude for Desktop App configuration at `~/Library/Application Support/Claude/claude_desktop_config.json` in a text editor. Make sure to create the file if it doesn't exist.
我们需要为要使用的任何 MCP 服务器配置 Claude for Desktop。为此，请在文本编辑器中打开 Claude for Desktop 应用配置文件 `~/Library/Application Support/Claude/claude_desktop_config.json`。如果文件不存在，请创建该文件。

    For example, if you have [VS Code](https://code.visualstudio.com/) installed:
例如，如果您已安装 [VS Code](https://code.visualstudio.com/)：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        code ~/Library/Application\ Support/Claude/claude_desktop_config.json
        ```
      </Tab>

      <Tab title="Windows">
        ```powershell
        code $env:AppData\Claude\claude_desktop_config.json
        ```
      </Tab>
    </Tabs>

    You'll then add your servers in the `mcpServers` key. The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.
然后您将在 `mcpServers` 键中添加您的服务器。只有当至少配置了一个服务器后，MCP UI 元素才会显示在 Claude for Desktop 中。

    In this case, we'll add our single weather server like so:
在此情况下，我们将这样添加我们的单个天气服务器：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```json Python
        {
            "mcpServers": {
                "weather": {
                    "command": "uv",
                    "args": [
                        "--directory",
                        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
                        "run",
                        "weather.py"
                    ]
                }
            }
        }
        ```
      </Tab>

      <Tab title="Windows">
        ```json Python
        {
            "mcpServers": {
                "weather": {
                    "command": "uv",
                    "args": [
                        "--directory",
                        "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\weather",
                        "run",
                        "weather.py"
                    ]
                }
            }
        }
        ```
      </Tab>
    </Tabs>

    <Warning>
      You may need to put the full path to the `uv` executable in the `command` field. You can get this by running `which uv` on MacOS/Linux or `where uv` on Windows.
    </Warning>
 您可能需要在“command”字段中输入“uv”可执行文件的完整路径。您可以在 MacOS/Linux 上运行`which uv`或在 Windows 上运行`where uv`来获取此路径。 

    <Note>
      Make sure you pass in the absolute path to your server.
    </Note>
 确保您传递的是服务器的绝对路径。 

    This tells Claude for Desktop:
这是指明 Claude for Desktop：

    1. There's an MCP server named "weather"
    2. To launch it by running `uv --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather run weather.py`
1. 有一个名为 "weather" 的 MCP 服务器 2. 通过运行 `uv --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather run weather.py` 来启动它

    Save the file, and restart **Claude for Desktop**.
  </Tab>
保存文件，并重新启动 **Claude for Desktop**。

  <Tab title="Node">
    Let's get started with building our weather server! [You can find the complete code for what we'll be building here.](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-typescript)
 让我们开始构建我们的天气服务器！[您可以在以下链接找到我们将要构建的完整代码。](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-typescript)

    ### Prerequisite knowledge
### 前置知识

    This quickstart assumes you have familiarity with:
本快速入门假定您熟悉以下内容：

    * TypeScript
    * LLMs like Claude
* TypeScript * LLMs 类似于 Claude

    ### System requirements  ### 系统要求

    For TypeScript, make sure you have the latest version of Node installed.
对于 TypeScript，请确保您已安装最新版本的 Node。

    ### Set up your environment
### 设置您的环境

    First, let's install Node.js and npm if you haven't already. You can download them from [nodejs.org](https://nodejs.org/).
    Verify your Node.js installation:
首先，让我们安装 Node.js 和 npm（如果您还没有安装的话）。您可以从[nodejs.org](https://nodejs.org/)下载它们。验证您的 Node.js 安装：

    ```bash
    node --version
    npm --version
    ```

    For this tutorial, you'll need Node.js version 16 or higher.
对于本教程，您需要 Node.js 版本 16 或更高版本。

    Now, let's create and set up our project:
现在，让我们创建并设置我们的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # Create a new directory for our project
      mkdir weather
      cd weather
 ```bash MacOS/Linux # 创建我们的项目目录 mkdir weather cd weather

      # Initialize a new npm project
      npm init -y
# 使用 npm 初始化一个新的项目 npm init -y

      # Install dependencies
      npm install @modelcontextprotocol/sdk zod
      npm install -D @types/node typescript
# 安装依赖 npm install @modelcontextprotocol/sdk zod npm install -D @types/node typescript

      # Create our files
      mkdir src
      touch src/index.ts
      ```
# 创建我们的文件 mkdir src touch src/index.ts

      ```powershell Windows
      # Create a new directory for our project
      md weather
      cd weather
# Windows # 为我们的项目创建一个新目录 md weather cd weather

      # Initialize a new npm project
      npm init -y
# 初始化一个新的 npm 项目 npm init -y

      # Install dependencies
      npm install @modelcontextprotocol/sdk zod
      npm install -D @types/node typescript
# 安装依赖 npm install @modelcontextprotocol/sdk zod npm install -D @types/node typescript

      # Create our files
      md src
      new-item src\index.ts
      ```
    </CodeGroup>
# 创建我们的文件 md src new-item src\index.ts ``` 

    Update your package.json to add type: "module" and a build script:
# 更新 package.json 文件以添加 type: "module" 和构建脚本：

    ```json package.json
    {
      "type": "module",
      "bin": {
        "weather": "./build/index.js"
      },
      "scripts": {
        "build": "tsc && chmod 755 build/index.js"
      },
      "files": [
        "build"
      ],
    }
    ```

    Create a `tsconfig.json` in the root of your project:
在项目的根目录下创建一个 `tsconfig.json` 文件：

    ```json tsconfig.json
    {
      "compilerOptions": {
        "target": "ES2022",
        "module": "Node16",
        "moduleResolution": "Node16",
        "outDir": "./build",
        "rootDir": "./src",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
      },
      "include": ["src/**/*"],
      "exclude": ["node_modules"]
    }
    ```

    Now let's dive into building your server.
现在让我们深入构建你的服务器。

    ## Building your server
## 构建你的服务器

    ### Importing packages and setting up the instance
### 导入包并设置实例

    Add these to the top of your `src/index.ts`:
将这些添加到您的 `src/index.ts` 顶部：

    ```typescript
    import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
    import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
    import { z } from "zod";
```typescript
从 "@modelcontextprotocol/sdk/server/mcp.js" 导入 { McpServer }; 从 "@modelcontextprotocol/sdk/server/stdio.js" 导入 { StdioServerTransport }; 从 "zod" 导入 { z };
```

    const NWS_API_BASE = "https://api.weather.gov";
    const USER_AGENT = "weather-app/1.0";
const NWS_API_BASE = "https://api.weather.gov"; const USER_AGENT = "weather-app/1.0"; 

NWS_API_BASE = "https://api.weather.gov"; USER_AGENT = "weather-app/1.0";

    // Create server instance
    const server = new McpServer({
      name: "weather",
      version: "1.0.0",
      capabilities: {
        resources: {},
        tools: {},
      },
    });
    ```
// 创建服务器实例 const server = new McpServer({ name: "weather", version: "1.0.0", capabilities: { resources: {}, tools: {}, }, }); ```

    ### Helper functions  ### 辅助函数

    Next, let's add our helper functions for querying and formatting the data from the National Weather Service API:
接下来，让我们添加查询和格式化国家气象服务 API 数据的辅助函数：

    ```typescript
    // Helper function for making NWS API requests
    async function makeNWSRequest<T>(url: string): Promise<T | null> {
      const headers = {
        "User-Agent": USER_AGENT,
        Accept: "application/geo+json",
      };
```typescript // 发送 NWS API 请求的辅助函数 async function makeNWSRequest(url: string): Promise { const headers = { "User-Agent": USER_AGENT, Accept: "application/geo+json", };

      try {
        const response = await fetch(url, { headers });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return (await response.json()) as T;
      } catch (error) {
        console.error("Error making NWS request:", error);
        return null;
      }
    }
try { const response = await fetch(url, { headers }); if (!response.ok) { throw new Error(`HTTP 错误！状态：${response.status}`); } return (await response.json()) as T; } catch (error) { console.error("错误：制作 NWS 请求", error); return null; } }

    interface AlertFeature {
      properties: {
        event?: string;
        areaDesc?: string;
        severity?: string;
        status?: string;
        headline?: string;
      };
    }

    // Format alert data
    function formatAlert(feature: AlertFeature): string {
      const props = feature.properties;
      return [
        `Event: ${props.event || "Unknown"}`,
        `Area: ${props.areaDesc || "Unknown"}`,
        `Severity: ${props.severity || "Unknown"}`,
        `Status: ${props.status || "Unknown"}`,
        `Headline: ${props.headline || "No headline"}`,
        "---",
      ].join("\n");
    }
// 格式化警报数据函数 formatAlert(feature: AlertFeature): string { const props = feature.properties; return [ `事件：${props.event || "未知"}`, `区域：${props.areaDesc || "未知"}`, `严重程度：${props.severity || "未知"}`, `状态：${props.status || "未知"}`, `标题：${props.headline || "无标题"}`, "---", ].join("\n"); }

    interface ForecastPeriod {
      name?: string;
      temperature?: number;
      temperatureUnit?: string;
      windSpeed?: string;
      windDirection?: string;
      shortForecast?: string;
    }

    interface AlertsResponse {
      features: AlertFeature[];
    }

    interface PointsResponse {
      properties: {
        forecast?: string;
      };
    }

    interface ForecastResponse {
      properties: {
        periods: ForecastPeriod[];
      };
    }
    ```
interface ForecastResponse { properties: { periods: ForecastPeriod[]; }; }

    ### Implementing tool execution
### 实现工具执行

    The tool execution handler is responsible for actually executing the logic of each tool. Let's add it:
工具执行处理器负责实际执行每个工具的逻辑。让我们添加它：

    ```typescript
    // Register weather tools
    server.tool(
      "get-alerts",
      "Get weather alerts for a state",
      {
        state: z.string().length(2).describe("Two-letter state code (e.g. CA, NY)"),
      },
      async ({ state }) => {
        const stateCode = state.toUpperCase();
        const alertsUrl = `${NWS_API_BASE}/alerts?area=${stateCode}`;
        const alertsData = await makeNWSRequest<AlertsResponse>(alertsUrl);
```typescript // 注册天气工具 server.tool( "get-alerts", "获取某个州的天气警报", { state: z.string().length(2).describe("两位字母州代码（例如 CA, NY）"), }, async ({ state }) => { const stateCode = state.toUpperCase(); const alertsUrl = `${NWS_API_BASE}/alerts?area=${stateCode}`; const alertsData = await makeNWSRequest(alertsUrl);

        if (!alertsData) {
          return {
            content: [
              {
                type: "text",
                text: "Failed to retrieve alerts data",
              },
            ],
          };
        }
if (!alertsData) { return { content: [ { type: "text", text: "无法检索警报数据", }, ], }; }

        const features = alertsData.features || [];
        if (features.length === 0) {
          return {
            content: [
              {
                type: "text",
                text: `No active alerts for ${stateCode}`,
              },
            ],
          };
        }
const features = alertsData.features || []; if (features.length === 0) { return { content: [ { type: "text", text: `没有针对 ${stateCode} 的活动警报`, }, ], }; }

        const formattedAlerts = features.map(formatAlert);
        const alertsText = `Active alerts for ${stateCode}:\n\n${formattedAlerts.join("\n")}`;

        return {
          content: [
            {
              type: "text",
              text: alertsText,
            },
          ],
        };
      },
    );

    server.tool(
      "get-forecast",
      "Get weather forecast for a location",
      {
        latitude: z.number().min(-90).max(90).describe("Latitude of the location"),
        longitude: z.number().min(-180).max(180).describe("Longitude of the location"),
      },
      async ({ latitude, longitude }) => {
        // Get grid point data
        const pointsUrl = `${NWS_API_BASE}/points/${latitude.toFixed(4)},${longitude.toFixed(4)}`;
        const pointsData = await makeNWSRequest<PointsResponse>(pointsUrl);

        if (!pointsData) {
          return {
            content: [
              {
                type: "text",
                text: `Failed to retrieve grid point data for coordinates: ${latitude}, ${longitude}. This location may not be supported by the NWS API (only US locations are supported).`,
              },
            ],
          };
        }

        const forecastUrl = pointsData.properties?.forecast;
        if (!forecastUrl) {
          return {
            content: [
              {
                type: "text",
                text: "Failed to get forecast URL from grid point data",
              },
            ],
          };
        }

        // Get forecast data
        const forecastData = await makeNWSRequest<ForecastResponse>(forecastUrl);
        if (!forecastData) {
          return {
            content: [
              {
                type: "text",
                text: "Failed to retrieve forecast data",
              },
            ],
          };
        }

        const periods = forecastData.properties?.periods || [];
        if (periods.length === 0) {
          return {
            content: [
              {
                type: "text",
                text: "No forecast periods available",
              },
            ],
          };
        }

        // Format forecast periods
        const formattedForecast = periods.map((period: ForecastPeriod) =>
          [
            `${period.name || "Unknown"}:`,
            `Temperature: ${period.temperature || "Unknown"}°${period.temperatureUnit || "F"}`,
            `Wind: ${period.windSpeed || "Unknown"} ${period.windDirection || ""}`,
            `${period.shortForecast || "No forecast available"}`,
            "---",
          ].join("\n"),
        );

        const forecastText = `Forecast for ${latitude}, ${longitude}:\n\n${formattedForecast.join("\n")}`;
const forecastText = `预报${latitude}，${longitude}的天气：\n\n${formattedForecast.join("\n")}`;

        return {
          content: [
            {
              type: "text",
              text: forecastText,
            },
          ],
        };
      },
    );
    ```
return { content: [{ type: "text", text: forecastText, }], }; }, );

    ### Running the server
### 运行服务器

    Finally, implement the main function to run the server:
最后，实现运行服务器的主函数：

    ```typescript
    async function main() {
      const transport = new StdioServerTransport();
      await server.connect(transport);
      console.error("Weather MCP Server running on stdio");
    }

    main().catch((error) => {
      console.error("Fatal error in main():", error);
      process.exit(1);
    });
    ```
main().catch((error) => { console.error("Fatal error in main():", error); process.exit(1); });

    Make sure to run `npm run build` to build your server! This is a very important step in getting your server to connect.
确保运行 `npm run build` 来构建你的服务器！这是连接服务器的一个非常重要的步骤。

    Let's now test your server from an existing MCP host, Claude for Desktop.
现在让我们从现有的 MCP 主机，Claude for Desktop，测试你的服务器。

    ## Testing your server with Claude for Desktop
测试 Claude for Desktop 服务器

    <Note>
      Claude for Desktop is not yet available on Linux. Linux users can proceed to the [Building a client](/quickstart/client) tutorial to build an MCP client that connects to the server we just built.
    </Note>
 Claude for Desktop 目前尚未在 Linux 上提供。Linux 用户可以前往 [构建客户端](/quickstart/client) 教程，构建一个连接到我们刚刚构建的服务器的 MCP 客户端。

    First, make sure you have Claude for Desktop installed. [You can install the latest version
    here.](https://claude.ai/download) If you already have Claude for Desktop, **make sure it's updated to the latest version.**
首先，请确保您已安装 Claude for Desktop。[您可以在此处安装最新版本。](https://claude.ai/download) 如果您已经安装了 Claude for Desktop，**请确保它已更新到最新版本。**

    We'll need to configure Claude for Desktop for whichever MCP servers you want to use. To do this, open your Claude for Desktop App configuration at `~/Library/Application Support/Claude/claude_desktop_config.json` in a text editor. Make sure to create the file if it doesn't exist.
我们需要配置 Claude for Desktop 以使用您想要的任何 MCP 服务器。为此，请打开 Claude for Desktop 应用配置文件 `~/Library/Application Support/Claude/claude_desktop_config.json`，使用文本编辑器进行操作。如果文件不存在，请确保创建该文件。

    For example, if you have [VS Code](https://code.visualstudio.com/) installed:
例如，如果您已安装 [VS Code](https://code.visualstudio.com/)：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        code ~/Library/Application\ Support/Claude/claude_desktop_config.json
        ```
      </Tab>

      <Tab title="Windows">
        ```powershell
        code $env:AppData\Claude\claude_desktop_config.json
        ```
      </Tab>
    </Tabs>

    You'll then add your servers in the `mcpServers` key. The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.
然后，您将在 `mcpServers` 键中添加您的服务器。只有当至少配置了一个服务器后，MCP UI 元素才会显示在 Claude for Desktop 中。

    In this case, we'll add our single weather server like so:
在这种情况下，我们将添加我们的单个天气服务器如下：

    <Tabs>
      <Tab title="MacOS/Linux">
        <CodeGroup>
          ```json Node
          {
              "mcpServers": {
                  "weather": {
                      "command": "node",
                      "args": [
                          "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/index.js"
                      ]
                  }
              }
          }
          ```
        </CodeGroup>
      </Tab>

      <Tab title="Windows">
        <CodeGroup>
          ```json Node
          {
              "mcpServers": {
                  "weather": {
                      "command": "node",
                      "args": [
                          "C:\\PATH\\TO\\PARENT\\FOLDER\\weather\\build\\index.js"
                      ]
                  }
              }
          }
          ```
        </CodeGroup>
      </Tab>
    </Tabs>

    This tells Claude for Desktop:
这告诉 Claude for Desktop：

    1. There's an MCP server named "weather"
    2. Launch it by running `node /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/index.js`
1. 有一个名为 "weather" 的 MCP 服务器 2. 通过运行 `node /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/index.js` 来启动它

    Save the file, and restart **Claude for Desktop**.
  </Tab>
保存文件，并重新启动 **Claude for Desktop**。

  <Tab title="Java">
    <Note>
      This is a quickstart demo based on Spring AI MCP auto-configuration and boot starters.
      To learn how to create sync and async MCP Servers, manually, consult the [Java SDK Server](/sdk/java/mcp-server) documentation.
    </Note>
  这是一个基于 Spring AI MCP 自动配置和启动器的快速入门演示。要了解如何手动创建同步和异步 MCP 服务器，请参阅 [Java SDK 服务器](/sdk/java/mcp-server) 文档。

    Let's get started with building our weather server!
    [You can find the complete code for what we'll be building here.](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/weather/starter-stdio-server)
让我们开始构建我们的天气服务器！[您可以在以下位置找到我们将要构建的完整代码。](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/weather/starter-stdio-server)

    For more information, see the [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) reference documentation.
    For manual MCP Server implementation, refer to the [MCP Server Java SDK documentation](/sdk/java/mcp-server).
更多信息，请参阅[MCP 服务器启动器](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html)参考文档。对于手动 MCP 服务器实现，请参考[MCP 服务器 Java SDK 文档](/sdk/java/mcp-server)。

    ### System requirements  ### 系统要求

    * Java 17 or higher installed.
    * [Spring Boot 3.3.x](https://docs.spring.io/spring-boot/installing.html) or higher
* 安装 Java 17 或更高版本。 * [Spring Boot 3.3.x](https://docs.spring.io/spring-boot/installing.html)或更高版本

    ### Set up your environment
### 设置您的环境

    Use the [Spring Initializer](https://start.spring.io/) to bootstrap the project.
使用 [Spring Initializer](https://start.spring.io/) 来引导项目。

    You will need to add the following dependencies:
您需要添加以下依赖项：

    <Tabs>
      <Tab title="Maven">
        ```xml
        <dependencies>
              <dependency>
                  <groupId>org.springframework.ai</groupId>
                  <artifactId>spring-ai-starter-mcp-server</artifactId>
              </dependency>

              <dependency>
                  <groupId>org.springframework</groupId>
                  <artifactId>spring-web</artifactId>
              </dependency>
        </dependencies>
        ```
      </Tab>

      <Tab title="Gradle">
        ```groovy
        dependencies {
          implementation platform("org.springframework.ai:spring-ai-starter-mcp-server")
          implementation platform("org.springframework:spring-web")   
        }
        ```
      </Tab>
    </Tabs>
 ```groovy dependencies { implementation platform("org.springframework.ai:spring-ai-starter-mcp-server") implementation platform("org.springframework:spring-web") } ```  

    Then configure your application by setting the application properties:
然后通过设置应用程序属性来配置您的应用程序：

    <CodeGroup>
      ```bash application.properties
      spring.main.bannerMode=off
      logging.pattern.console=
      ```

      ```yaml application.yml
      logging:
        pattern:
          console:
      spring:
        main:
          banner-mode: off
      ```
    </CodeGroup>

    The [Server Configuration Properties](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html#_configuration_properties) documents all available properties.
服务器配置属性文档列出了所有可用的属性。[服务器配置属性](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html#_configuration_properties)

    Now let's dive into building your server.
现在让我们深入到构建你的服务器。

    ## Building your server
## 构建你的服务器

    ### Weather Service  ### 天气服务

    Let's implement a [WeatherService.java](https://github.com/spring-projects/spring-ai-examples/blob/main/model-context-protocol/weather/starter-stdio-server/src/main/java/org/springframework/ai/mcp/sample/server/WeatherService.java) that uses a REST client to query the data from the National Weather Service API:
让我们实现一个使用 REST 客户端从国家气象服务 API 查询数据的[WeatherService.java](https://github.com/spring-projects/spring-ai-examples/blob/main/model-context-protocol/weather/starter-stdio-server/src/main/java/org/springframework/ai/mcp/sample/server/WeatherService.java)：

    ```java
    @Service
    public class WeatherService {

    	private final RestClient restClient;

    	public WeatherService() {
    		this.restClient = RestClient.builder()
    			.baseUrl("https://api.weather.gov")
    			.defaultHeader("Accept", "application/geo+json")
    			.defaultHeader("User-Agent", "WeatherApiClient/1.0 (your@email.com)")
    			.build();
    	}

      @Tool(description = "Get weather forecast for a specific latitude/longitude")
      public String getWeatherForecastByLocation(
          double latitude,   // Latitude coordinate
          double longitude   // Longitude coordinate
      ) {
          // Returns detailed forecast including:
          // - Temperature and unit
          // - Wind speed and direction
          // - Detailed forecast description
      }
    	
      @Tool(description = "Get weather alerts for a US state")
      public String getAlerts(
          @ToolParam(description = "Two-letter US state code (e.g. CA, NY)" String state
      ) {
          // Returns active alerts including:
          // - Event type
          // - Affected area
          // - Severity
          // - Description
          // - Safety instructions
      }
@工具（描述 = "获取特定经纬度的天气预报"）public String getWeatherForecastByLocation( double latitude, // 纬度坐标 double longitude // 经度坐标 ) { // 返回详细的预报，包括： // - 温度和单位 // - 风速和风向 // - 详细预报描述 } @工具（描述 = "获取美国州的天气警报"）public String getAlerts( @工具参数（描述 = "两位字母的美国州代码（例如：CA，NY）" String state ) { // 返回活跃警报，包括： // - 事件类型 // - 影响区域 // - 严重程度 // - 描述 // - 安全指南

      // ......
    }
    ```

    The `@Service` annotation with auto-register the service in your application context.
    The Spring AI `@Tool` annotation, making it easy to create and maintain MCP tools.
`@Service` 注解会自动将服务注册到您的应用程序上下文中。Spring AI 的 `@Tool` 注解，使创建和维护 MCP 工具变得简单。

    The auto-configuration will automatically register these tools with the MCP server.
自动配置会自动将这些工具注册到 MCP 服务器。

    ### Create your Boot Application
### 创建您的 Boot 应用程序

    ```java
    @SpringBootApplication
    public class McpServerApplication {

    	public static void main(String[] args) {
    		SpringApplication.run(McpServerApplication.class, args);
    	}

    	@Bean
    	public ToolCallbackProvider weatherTools(WeatherService weatherService) {
    		return  MethodToolCallbackProvider.builder().toolObjects(weatherService).build();
    	}
    }
    ```
@Bean public ToolCallbackProvider weatherTools(WeatherService weatherService) { return MethodToolCallbackProvider.builder().toolObjects(weatherService).build(); } }

    Uses the the `MethodToolCallbackProvider` utils to convert the `@Tools` into actionable callbacks used by the MCP server.
使用 `MethodToolCallbackProvider` 工具将 `@Tools` 转换为 MCP 服务器使用的可操作回调。

    ### Running the server
### 运行服务器

    Finally, let's build the server:
最后，让我们构建服务器：

    ```bash
    ./mvnw clean install
    ```

    This will generate a `mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar` file within the `target` folder.
这将在 `target` 文件夹内生成一个 `mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar` 文件。

    Let's now test your server from an existing MCP host, Claude for Desktop.
现在，让我们从现有的 MCP 主机，Claude for Desktop，测试你的服务器。

    ## Testing your server with Claude for Desktop
测试您的 Claude for Desktop 服务器

    <Note>
      Claude for Desktop is not yet available on Linux.
    </Note>
 Claude for Desktop 目前尚未在 Linux 上提供。

    First, make sure you have Claude for Desktop installed.
    [You can install the latest version here.](https://claude.ai/download) If you already have Claude for Desktop, **make sure it's updated to the latest version.**
首先，请确保您已安装 Claude for Desktop。[您可以从这里安装最新版本。](https://claude.ai/download) 如果您已经安装了 Claude for Desktop，**请确保它已更新到最新版本。**

    We'll need to configure Claude for Desktop for whichever MCP servers you want to use.
    To do this, open your Claude for Desktop App configuration at `~/Library/Application Support/Claude/claude_desktop_config.json` in a text editor.
    Make sure to create the file if it doesn't exist.
我们需要为要使用的任何 MCP 服务器配置 Claude for Desktop。为此，请打开您的 Claude for Desktop 应用配置文件 `~/Library/Application Support/Claude/claude_desktop_config.json`，并在文本编辑器中打开。如果文件不存在，请确保创建该文件。

    For example, if you have [VS Code](https://code.visualstudio.com/) installed:
例如，如果您已安装 [VS Code](https://code.visualstudio.com/)：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        code ~/Library/Application\ Support/Claude/claude_desktop_config.json
        ```
      </Tab>

      <Tab title="Windows">
        ```powershell
        code $env:AppData\Claude\claude_desktop_config.json
        ```
      </Tab>
    </Tabs>

    You'll then add your servers in the `mcpServers` key.
    The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.
然后，您将在 `mcpServers` 键中添加您的服务器。只有当至少配置了一个服务器后，MCP UI 元素才会显示在 Claude for Desktop 中。

    In this case, we'll add our single weather server like so:
在这种情况下，我们将这样添加我们的单个天气服务器：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```json java
        {
          "mcpServers": {
            "spring-ai-mcp-weather": {
              "command": "java",
              "args": [
                "-Dspring.ai.mcp.server.stdio=true",
                "-jar",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar"
              ]
            }
          }
        }
        ```
      </Tab>

      <Tab title="Windows">
        ```json java
        {
          "mcpServers": {
            "spring-ai-mcp-weather": {
              "command": "java",
              "args": [
                "-Dspring.ai.mcp.server.transport=STDIO",
                "-jar",
                "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\weather\\mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar"
              ]
            }
          }
        }
        ```
      </Tab>
    </Tabs>

    <Note>
      Make sure you pass in the absolute path to your server.
    </Note>
 确保您传入服务器的绝对路径。 

    This tells Claude for Desktop:
这是指明 Claude for Desktop：

    1. There's an MCP server named "my-weather-server"
    2. To launch it by running `java -jar /ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar`
1. 有一个名为 "my-weather-server" 的 MCP 服务器 2. 通过运行 `java -jar /ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar` 来启动它

    Save the file, and restart **Claude for Desktop**.
保存文件，并重新启动 **Claude for Desktop**

    ## Testing your server with Java client
## 使用 Java 客户端测试您的服务器

    ### Create a MCP Client manually
手动创建 MCP 客户端

    Use the `McpClient` to connect to the server:
使用 `McpClient` 连接到服务器：

    ```java
    var stdioParams = ServerParameters.builder("java")
      .args("-jar", "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-weather-stdio-server-0.0.1-SNAPSHOT.jar")
      .build();

    var stdioTransport = new StdioClientTransport(stdioParams);

    var mcpClient = McpClient.sync(stdioTransport).build();

    mcpClient.initialize();

    ListToolsResult toolsList = mcpClient.listTools();

    CallToolResult weather = mcpClient.callTool(
      new CallToolRequest("getWeatherForecastByLocation",
          Map.of("latitude", "47.6062", "longitude", "-122.3321")));

    CallToolResult alert = mcpClient.callTool(
      new CallToolRequest("getAlerts", Map.of("state", "NY")));

    mcpClient.closeGracefully();
    ```
mcpClient.closeGracefully();

    ### Use MCP Client Boot Starter
### 使用 MCP 客户端启动器

    Create a new boot starter application using the `spring-ai-starter-mcp-client` dependency:
使用`spring-ai-starter-mcp-client`依赖项创建一个新的启动器应用程序：

    ```xml
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-starter-mcp-client</artifactId>
    </dependency>
    ```

    and set the `spring.ai.mcp.client.stdio.servers-configuration` property to point to your `claude_desktop_config.json`.
    You can re-use the existing Anthropic Desktop configuration:
将`spring.ai.mcp.client.stdio.servers-configuration`属性设置为指向您的`claude_desktop_config.json`。您可以重复使用现有的 Anthropic 桌面配置：

    ```properties
    spring.ai.mcp.client.stdio.servers-configuration=file:PATH/TO/claude_desktop_config.json
    ```

    When you start your client application, the auto-configuration will create, automatically MCP clients from the claude\_desktop\_config.json.
当您启动客户端应用程序时，自动配置将自动从`claude_desktop_config.json`创建 MCP 客户端。

    For more information, see the [MCP Client Boot Starters](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-client-docs.html) reference documentation.
有关更多信息，请参阅[MCP 客户端启动器](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-client-docs.html)参考文档。

    ## More Java MCP Server examples
## 更多 Java MCP 服务器示例

    The [starter-webflux-server](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/weather/starter-webflux-server) demonstrates how to create a MCP server using SSE transport.
    It showcases how to define and register MCP Tools, Resources, and Prompts, using the Spring Boot's auto-configuration capabilities.
  </Tab>
The [starter-webflux-server](https://github.com/spring-projects/spring-ai-examples/tree/main/model-context-protocol/weather/starter-webflux-server) 展示了如何使用 SSE 传输创建 MCP 服务器。它展示了如何使用 Spring Boot 的自动配置功能定义和注册 MCP 工具、资源和提示。

  <Tab title="Kotlin">
    Let's get started with building our weather server! [You can find the complete code for what we'll be building here.](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/weather-stdio-server)
让我们开始构建我们的天气服务器！[您可以在以下链接找到我们将要构建的完整代码。](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/weather-stdio-server)

    ### Prerequisite knowledge
### 前置知识

    This quickstart assumes you have familiarity with:
本快速入门假设您熟悉：

    * Kotlin
    * LLMs like Claude
* Kotlin * LLMs 像克劳德

    ### System requirements  ### 系统要求

    * Java 17 or higher installed.
* 安装 Java 17 或更高版本。

    ### Set up your environment
### 设置您的环境

    First, let's install `java` and `gradle` if you haven't already.
    You can download `java` from [official Oracle JDK website](https://www.oracle.com/java/technologies/downloads/).
    Verify your `java` installation:
首先，如果您还没有安装，请安装 `java` 和 `gradle`。您可以从 [官方 Oracle JDK 网站](https://www.oracle.com/java/technologies/downloads/) 下载 `java`。验证您的 `java` 安装：

    ```bash
    java --version
    ```

    Now, let's create and set up your project:
现在，让我们创建并设置您的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # Create a new directory for our project
      mkdir weather
      cd weather
 ```bash MacOS/Linux # 创建我们的项目目录 mkdir weather cd weather

      # Initialize a new kotlin project
      gradle init
      ```
初始化一个新的 Kotlin 项目 gradle init ```

      ```powershell Windows
      # Create a new directory for our project
      md weather
      cd weather
```powershell Windows # 为我们的项目创建一个新目录 md weather cd weather

      # Initialize a new kotlin project
      gradle init
      ```
    </CodeGroup>
# 初始化一个新的 Kotlin 项目 gradle init ``` 

    After running `gradle init`, you will be presented with options for creating your project.
    Select **Application** as the project type, **Kotlin** as the programming language, and **Java 17** as the Java version.
运行 `gradle init` 后，您将看到创建项目的选项。选择 **应用程序** 作为项目类型，**Kotlin** 作为编程语言，以及 **Java 17** 作为 Java 版本。

    Alternatively, you can create a Kotlin application using the [IntelliJ IDEA project wizard](https://kotlinlang.org/docs/jvm-get-started.html).
或者，您可以使用 IntelliJ IDEA 项目向导创建 Kotlin 应用程序。[IntelliJ IDEA 项目向导](https://kotlinlang.org/docs/jvm-get-started.html)。

    After creating the project, add the following dependencies:
创建项目后，添加以下依赖项：

    <CodeGroup>
      ```kotlin build.gradle.kts
      val mcpVersion = "0.4.0"
      val slf4jVersion = "2.0.9"
      val ktorVersion = "3.1.1"

      dependencies {
          implementation("io.modelcontextprotocol:kotlin-sdk:$mcpVersion")
          implementation("org.slf4j:slf4j-nop:$slf4jVersion")
          implementation("io.ktor:ktor-client-content-negotiation:$ktorVersion")
          implementation("io.ktor:ktor-serialization-kotlinx-json:$ktorVersion")
      }
      ```

      ```groovy build.gradle
      def mcpVersion = '0.3.0'
      def slf4jVersion = '2.0.9'
      def ktorVersion = '3.1.1'

      dependencies {
          implementation "io.modelcontextprotocol:kotlin-sdk:$mcpVersion"
          implementation "org.slf4j:slf4j-nop:$slf4jVersion"
          implementation "io.ktor:ktor-client-content-negotiation:$ktorVersion"
          implementation "io.ktor:ktor-serialization-kotlinx-json:$ktorVersion"
      }
      ```
    </CodeGroup>

    Also, add the following plugins to your build script:
同时，将以下插件添加到您的构建脚本中：

    <CodeGroup>
      ```kotlin build.gradle.kts
      plugins {
          kotlin("plugin.serialization") version "your_version_of_kotlin"
          id("com.github.johnrengelman.shadow") version "8.1.1"
      }
      ```
 ```kotlin build.gradle.kts plugins { kotlin("plugin.serialization") version "your_version_of_kotlin" id("com.github.johnrengelman.shadow") version "8.1.1" } ``` 

      ```groovy build.gradle
      plugins {
          id 'org.jetbrains.kotlin.plugin.serialization' version 'your_version_of_kotlin'
          id 'com.github.johnrengelman.shadow' version '8.1.1'
      }
      ```
    </CodeGroup>

    Now let’s dive into building your server.
现在让我们深入构建你的服务器。

    ## Building your server
## 构建你的服务器

    ### Setting up the instance
### 设置实例

    Add a server initialization function:
添加服务器初始化函数：

    ```kotlin
    // Main function to run the MCP server
    fun `run mcp server`() {
        // Create the MCP Server instance with a basic implementation
        val server = Server(
            Implementation(
                name = "weather", // Tool name is "weather"
                version = "1.0.0" // Version of the implementation
            ),
            ServerOptions(
                capabilities = ServerCapabilities(tools = ServerCapabilities.Tools(listChanged = true))
            )
        )
```kotlin // 运行 MCP 服务器的主函数 fun `run mcp server`() { // 使用基本实现创建 MCP 服务器实例 val server = Server( Implementation( name = "weather", // 工具名称为"weather" version = "1.0.0" // 实现的版本 ), ServerOptions( capabilities = ServerCapabilities(tools = ServerCapabilities.Tools(listChanged = true)) ) )

        // Create a transport using standard IO for server communication
        val transport = StdioServerTransport(
            System.`in`.asInput(),
            System.out.asSink().buffered()
        )
// 使用标准 IO 创建用于服务器通信的传输 val transport = StdioServerTransport( System.`in`.asInput(), System.out.asSink().buffered() )

        runBlocking {
            server.connect(transport)
            val done = Job()
            server.onClose {
                done.complete()
            }
            done.join()
        }
    }
    ```
runBlocking { server.connect(transport) val done = Job() server.onClose { done.complete() } done.join() } ```

    ### Weather API helper functions
天气 API 辅助函数

    Next, let's add functions and data classes for querying and converting responses from the National Weather Service API:
接下来，让我们添加查询和转换国家气象服务 API 响应的函数和数据类：

    ```kotlin
    // Extension function to fetch forecast information for given latitude and longitude
    suspend fun HttpClient.getForecast(latitude: Double, longitude: Double): List<String> {
        val points = this.get("/points/$latitude,$longitude").body<Points>()
        val forecast = this.get(points.properties.forecast).body<Forecast>()
        return forecast.properties.periods.map { period ->
            """
                ${period.name}:
                Temperature: ${period.temperature} ${period.temperatureUnit}
                Wind: ${period.windSpeed} ${period.windDirection}
                Forecast: ${period.detailedForecast}
            """.trimIndent()
        }
    }
```kotlin // 扩展函数，用于获取给定纬度和经度的天气预报信息 suspend fun HttpClient.getForecast(latitude: Double, longitude: Double): List { val points = this.get("/points/$latitude,$longitude").body() val forecast = this.get(points.properties.forecast).body() return forecast.properties.periods.map { period -> """ ${period.name}: 温度: ${period.temperature} ${period.temperatureUnit} 风速: ${period.windSpeed} ${period.windDirection} 预报: ${period.detailedForecast} """.trimIndent() } }

    // Extension function to fetch weather alerts for a given state
    suspend fun HttpClient.getAlerts(state: String): List<String> {
        val alerts = this.get("/alerts/active/area/$state").body<Alert>()
        return alerts.features.map { feature ->
            """
                Event: ${feature.properties.event}
                Area: ${feature.properties.areaDesc}
                Severity: ${feature.properties.severity}
                Description: ${feature.properties.description}
                Instruction: ${feature.properties.instruction}
            """.trimIndent()
        }
    }
// 扩展函数，用于获取给定州的天气警报 suspend fun HttpClient.getAlerts(state: String): List { val alerts = this.get("/alerts/active/area/$state").body() return alerts.features.map { feature -> """ 事件: ${feature.properties.event} 区域: ${feature.properties.areaDesc} 级别: ${feature.properties.severity} 描述: ${feature.properties.description} 指示: ${feature.properties.instruction} """.trimIndent() } }

    @Serializable
    data class Points(
        val properties: Properties
    ) {
        @Serializable
        data class Properties(val forecast: String)
    }
@Serializable 数据类 Points( val properties: Properties ) { @Serializable 数据类 Properties(val forecast: String) }

    @Serializable
    data class Forecast(
        val properties: Properties
    ) {
        @Serializable
        data class Properties(val periods: List<Period>)
@Serializable 数据类 Forecast( val properties: Properties ) { @Serializable 数据类 Properties(val periods: List) }

        @Serializable
        data class Period(
            val number: Int, val name: String, val startTime: String, val endTime: String,
            val isDaytime: Boolean, val temperature: Int, val temperatureUnit: String,
            val temperatureTrend: String, val probabilityOfPrecipitation: JsonObject,
            val windSpeed: String, val windDirection: String,
            val shortForecast: String, val detailedForecast: String,
        )
    }
@Serializable 数据类 Period( val number: Int, val name: String, val startTime: String, val endTime: String, val isDaytime: Boolean, val temperature: Int, val temperatureUnit: String, val temperatureTrend: String, val probabilityOfPrecipitation: JsonObject, val windSpeed: String, val windDirection: String, val shortForecast: String, val detailedForecast: String, ) }

    @Serializable
    data class Alert(
        val features: List<Feature>
    ) {
        @Serializable
        data class Feature(
            val properties: Properties
        )
@Serializable 数据类 Alert( val features: List ) { @Serializable 数据类 Feature( val properties: Properties ) }

        @Serializable
        data class Properties(
            val event: String, val areaDesc: String, val severity: String,
            val description: String, val instruction: String?,
        )
    }
    ```
`@Serializable data class Properties( val event: String, val areaDesc: String, val severity: String, val description: String, val instruction: String?, ) } ```

    ### Implementing tool execution
### 实现工具执行

    The tool execution handler is responsible for actually executing the logic of each tool. Let's add it:
工具执行处理器负责实际执行每个工具的逻辑。让我们添加它：

    ```kotlin
    // Create an HTTP client with a default request configuration and JSON content negotiation
    val httpClient = HttpClient {
        defaultRequest {
            url("https://api.weather.gov")
            headers {
                append("Accept", "application/geo+json")
                append("User-Agent", "WeatherApiClient/1.0")
            }
            contentType(ContentType.Application.Json)
        }
        // Install content negotiation plugin for JSON serialization/deserialization
        install(ContentNegotiation) { json(Json { ignoreUnknownKeys = true }) }
    }
```kotlin // 创建一个具有默认请求配置和 JSON 内容协商的 HTTP 客户端 val httpClient = HttpClient { defaultRequest { url("https://api.weather.gov") headers { append("Accept", "application/geo+json") append("User-Agent", "WeatherApiClient/1.0") } contentType(ContentType.Application.Json) } // 安装内容协商插件以进行 JSON 序列化和反序列化 install(ContentNegotiation) { json(Json { ignoreUnknownKeys = true }) } } ```

    // Register a tool to fetch weather alerts by state
    server.addTool(
        name = "get_alerts",
        description = """
            Get weather alerts for a US state. Input is Two-letter US state code (e.g. CA, NY)
        """.trimIndent(),
        inputSchema = Tool.Input(
            properties = buildJsonObject {
                putJsonObject("state") {
                    put("type", "string")
                    put("description", "Two-letter US state code (e.g. CA, NY)")
                }
            },
            required = listOf("state")
        )
    ) { request ->
        val state = request.arguments["state"]?.jsonPrimitive?.content
        if (state == null) {
            return@addTool CallToolResult(
                content = listOf(TextContent("The 'state' parameter is required."))
            )
        }
注册一个通过州服务器获取天气警报的工具 server.addTool(name = "get_alerts", description = """获取美国各州的天气警报。输入为两位字母的美国州代码（例如：CA，NY）""".trimIndent(), inputSchema = Tool.Input(properties = buildJsonObject { putJsonObject("state") { put("type", "string") put("description", "两位字母的美国州代码（例如：CA，NY）") } }, required = listOf("state")) { request -> val state = request.arguments["state"]?.jsonPrimitive?.content if (state == null) { return@addTool CallToolResult(content = listOf(TextContent("必需的 'state' 参数。"))) } })

        val alerts = httpClient.getAlerts(state)

        CallToolResult(content = alerts.map { TextContent(it) })
    }
CallToolResult(content = alerts.map { TextContent(it) })

    // Register a tool to fetch weather forecast by latitude and longitude
    server.addTool(
        name = "get_forecast",
        description = """
            Get weather forecast for a specific latitude/longitude
        """.trimIndent(),
        inputSchema = Tool.Input(
            properties = buildJsonObject {
                putJsonObject("latitude") { put("type", "number") }
                putJsonObject("longitude") { put("type", "number") }
            },
            required = listOf("latitude", "longitude")
        )
    ) { request ->
        val latitude = request.arguments["latitude"]?.jsonPrimitive?.doubleOrNull
        val longitude = request.arguments["longitude"]?.jsonPrimitive?.doubleOrNull
        if (latitude == null || longitude == null) {
            return@addTool CallToolResult(
                content = listOf(TextContent("The 'latitude' and 'longitude' parameters are required."))
            )
        }
注册一个通过经纬度获取天气预报的工具 server.addTool(名称 = "get_forecast"，描述 = """ 获取特定经纬度的天气预报 """.trimIndent()，输入模式 = Tool.Input(属性 = buildJsonObject { putJsonObject("latitude") { put("type", "number") } putJsonObject("longitude") { put("type", "number") } }，必需 = listOf("latitude", "longitude") ) ) { request -> val latitude = request.arguments["latitude"]?.jsonPrimitive?.doubleOrNull val longitude = request.arguments["longitude"]?.jsonPrimitive?.doubleOrNull if (latitude == null || longitude == null) { return@addTool CallToolResult(内容 = listOf(TextContent("The 'latitude' and 'longitude' parameters are required."))) }

        val forecast = httpClient.getForecast(latitude, longitude)

        CallToolResult(content = forecast.map { TextContent(it) })
    }
    ```
CallToolResult(内容 = forecast.map { TextContent(it) })

    ### Running the server
### 运行服务器

    Finally, implement the main function to run the server:
最后，实现运行服务器的 main 函数：

    ```kotlin
    fun main() = `run mcp server`()
    ```

    Make sure to run `./gradlew build` to build your server. This is a very important step in getting your server to connect.
确保运行 `./gradlew build` 来构建你的服务器。这是连接服务器的一个非常重要的步骤。

    Let's now test your server from an existing MCP host, Claude for Desktop.
现在，让我们从现有的 MCP 主机，Claude for Desktop，测试你的服务器。

    ## Testing your server with Claude for Desktop
测试 Claude for Desktop 服务器

    <Note>
      Claude for Desktop is not yet available on Linux. Linux users can proceed to the [Building a client](/quickstart/client) tutorial to build an MCP client that connects to the server we just built.
    </Note>
 Claude for Desktop 目前尚未在 Linux 上提供。Linux 用户可以前往 [构建客户端](/quickstart/client) 教程，构建一个连接到我们刚刚构建的服务器的 MCP 客户端。

    First, make sure you have Claude for Desktop installed. [You can install the latest version
    here.](https://claude.ai/download) If you already have Claude for Desktop, **make sure it's updated to the latest version.**
首先，请确保您已安装 Claude for Desktop。[您可以在此处安装最新版本。](https://claude.ai/download) 如果您已经安装了 Claude for Desktop，**请确保它已更新到最新版本。**

    We'll need to configure Claude for Desktop for whichever MCP servers you want to use.
    To do this, open your Claude for Desktop App configuration at `~/Library/Application Support/Claude/claude_desktop_config.json` in a text editor.
    Make sure to create the file if it doesn't exist.
我们需要配置 Claude for Desktop 以使用您想要的任何 MCP 服务器。为此，请打开 Claude for Desktop 应用配置文件 `~/Library/Application Support/Claude/claude_desktop_config.json`，使用文本编辑器进行操作。如果文件不存在，请确保创建该文件。

    For example, if you have [VS Code](https://code.visualstudio.com/) installed:
例如，如果您已安装 [VS Code](https://code.visualstudio.com/)：

    <CodeGroup>
      ```bash MacOS/Linux
      code ~/Library/Application\ Support/Claude/claude_desktop_config.json
      ```
 ```bash MacOS/Linux 代码 ~/Library/Application\ Support/Claude/claude_desktop_config.json ``` 

      ```powershell Windows
      code $env:AppData\Claude\claude_desktop_config.json
      ```
    </CodeGroup>
```powershell Windows 代码 $env:AppData\Claude\claude_desktop_config.json ``` 

    You'll then add your servers in the `mcpServers` key.
    The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.
然后，您将在 `mcpServers` 键中添加您的服务器。只有当至少配置了一个服务器后，MCP UI 元素才会显示在 Claude for Desktop 中。

    In this case, we'll add our single weather server like so:
在这种情况下，我们将像这样添加我们的单个天气服务器：

    <CodeGroup>
      ```json MacOS/Linux
      {
          "mcpServers": {
              "weather": {
                  "command": "java",
                  "args": [
                      "-jar",
                      "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/libs/weather-0.1.0-all.jar"
                  ]
              }
          }
      }
      ```
 ```json MacOS/Linux { "mcpServers": { "weather": { "command": "java", "args": [ "-jar", "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/libs/weather-0.1.0-all.jar" ] } } } ``` 

      ```json Windows
      {
          "mcpServers": {
              "weather": {
                  "command": "java",
                  "args": [
                      "-jar",
                      "C:\\PATH\\TO\\PARENT\\FOLDER\\weather\\build\\libs\\weather-0.1.0-all.jar"
                  ]
              }
          }
      }
      ```
    </CodeGroup>

    This tells Claude for Desktop:
这告诉 Claude 桌面：

    1. There's an MCP server named "weather"
    2. Launch it by running `java -jar /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/libs/weather-0.1.0-all.jar`
1. 有一个名为 "weather" 的 MCP 服务器 2. 通过运行 `java -jar /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather/build/libs/weather-0.1.0-all.jar` 来启动它

    Save the file, and restart **Claude for Desktop**.
  </Tab>
保存文件，并重新启动 **Claude for Desktop**。

  <Tab title="C#">
    Let's get started with building our weather server! [You can find the complete code for what we'll be building here.](https://github.com/modelcontextprotocol/csharp-sdk/tree/main/samples/QuickstartWeatherServer)
 让我们开始构建我们的天气服务器！[您可以在以下链接找到我们将要构建的完整代码。](https://github.com/modelcontextprotocol/csharp-sdk/tree/main/samples/QuickstartWeatherServer)

    ### Prerequisite knowledge
### 前置知识

    This quickstart assumes you have familiarity with:
本快速入门假设您熟悉以下内容：

    * C#
    * LLMs like Claude
    * .NET 8 or higher
* C# * LLMs 类似于 Claude * .NET 8 或更高版本

    ### System requirements  ### 系统要求

    * [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or higher installed.
* 已安装 [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) 或更高版本。

    ### Set up your environment
设置你的环境

    First, let's install `dotnet` if you haven't already. You can download `dotnet` from [official Microsoft .NET website](https://dotnet.microsoft.com/download/). Verify your `dotnet` installation:
首先，如果你还没有安装，请安装 `dotnet`。你可以从[官方 Microsoft .NET 网站](https://dotnet.microsoft.com/download/)下载 `dotnet`。验证你的 `dotnet` 安装：

    ```bash
    dotnet --version
    ```

    Now, let's create and set up your project:
现在，让我们创建并设置你的项目：

    <CodeGroup>
      ```bash MacOS/Linux
      # Create a new directory for our project
      mkdir weather
      cd weather
      # Initialize a new C# project
      dotnet new console
      ```
```bash MacOS/Linux # 创建项目目录 mkdir weather cd weather # 初始化新的 C# 项目 dotnet new console ```

      ```powershell Windows
      # Create a new directory for our project
      mkdir weather
      cd weather
      # Initialize a new C# project
      dotnet new console
      ```
    </CodeGroup>
```powershell Windows # 创建项目目录 mkdir weather cd weather # 初始化新的 C# 项目 dotnet new console ``` 

    After running `dotnet new console`, you will be presented with a new C# project.
    You can open the project in your favorite IDE, such as [Visual Studio](https://visualstudio.microsoft.com/) or [Rider](https://www.jetbrains.com/rider/).
    Alternatively, you can create a C# application using the [Visual Studio project wizard](https://learn.microsoft.com/en-us/visualstudio/get-started/csharp/tutorial-console?view=vs-2022).
    After creating the project, add NuGet package for the Model Context Protocol SDK and hosting:
运行 `dotnet new console` 后，您将看到一个新 C# 项目。您可以在您喜欢的 IDE 中打开该项目，例如 [Visual Studio](https://visualstudio.microsoft.com/) 或 [Rider](https://www.jetbrains.com/rider/)。或者，您可以使用 [Visual Studio 项目向导](https://learn.microsoft.com/en-us/visualstudio/get-started/csharp/tutorial-console?view=vs-2022)创建 C# 应用程序。创建项目后，添加 Model Context Protocol SDK 和托管 NuGet 包：

    ```bash
    # Add the Model Context Protocol SDK NuGet package
    dotnet add package ModelContextProtocol --prerelease
    # Add the .NET Hosting NuGet package
    dotnet add package Microsoft.Extensions.Hosting
    ```
```bash # 添加 Model Context Protocol SDK NuGet 包 dotnet add package ModelContextProtocol --prerelease # 添加 .NET 托管 NuGet 包 dotnet add package Microsoft.Extensions.Hosting ```

    Now let’s dive into building your server.
现在让我们深入到构建你的服务器。

    ## Building your server
## 构建你的服务器

    Open the `Program.cs` file in your project and replace its contents with the following code:
在你的项目中打开 `Program.cs` 文件，并用以下代码替换其内容：

    ```csharp
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.Extensions.Hosting;
    using ModelContextProtocol;
    using System.Net.Http.Headers;

    var builder = Host.CreateEmptyApplicationBuilder(settings: null);

    builder.Services.AddMcpServer()
        .WithStdioServerTransport()
        .WithToolsFromAssembly();

    builder.Services.AddSingleton(_ =>
    {
        var client = new HttpClient() { BaseAddress = new Uri("https://api.weather.gov") };
        client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("weather-tool", "1.0"));
        return client;
    });

    var app = builder.Build();

    await app.RunAsync();
    ```
await app.RunAsync();

    <Note>
      When creating the `ApplicationHostBuilder`, ensure you use `CreateEmptyApplicationBuilder` instead of `CreateDefaultBuilder`. This ensures that the server does not write any additional messages to the console. This is only neccessary for servers using STDIO transport.
    </Note>
在创建`ApplicationHostBuilder`时，请确保使用`CreateEmptyApplicationBuilder`而不是`CreateDefaultBuilder`。这确保服务器不会向控制台写入任何额外的消息。这仅适用于使用 STDIO 传输的服务器。

    This code sets up a basic console application that uses the Model Context Protocol SDK to create an MCP server with standard I/O transport.
此代码设置了一个基本的控制台应用程序，该应用程序使用模型上下文协议（MCP）SDK 创建一个带有标准 I/O 传输的 MCP 服务器。

    ### Weather API helper functions
### 天气 API 辅助函数

    Next, define a class with the tool execution handlers for querying and converting responses from the National Weather Service API:
接下来，定义一个类，用于处理查询和转换国家气象服务 API 的响应：

    ```csharp
    using ModelContextProtocol.Server;
    using System.ComponentModel;
    using System.Net.Http.Json;
    using System.Text.Json;
```csharp 使用 ModelContextProtocol.Server; 使用 System.ComponentModel; 使用 System.Net.Http.Json; 使用 System.Text.Json;

    namespace QuickstartWeatherServer.Tools;

    [McpServerToolType]
    public static class WeatherTools
    {
        [McpServerTool, Description("Get weather alerts for a US state.")]
        public static async Task<string> GetAlerts(
            HttpClient client,
            [Description("The US state to get alerts for.")] string state)
        {
            var jsonElement = await client.GetFromJsonAsync<JsonElement>($"/alerts/active/area/{state}");
            var alerts = jsonElement.GetProperty("features").EnumerateArray();
[McpServerToolType] public static class WeatherTools { [McpServerTool, Description("获取美国州的天气警报。")] public static async Task GetAlerts( HttpClient client, [Description("要获取警报的美国州。")] string state) { var jsonElement = await client.GetFromJsonAsync($"/alerts/active/area/{state}"); var alerts = jsonElement.GetProperty("features").EnumerateArray();

            if (!alerts.Any())
            {
                return "No active alerts for this state.";
            }
如果(!alerts.Any()) { 返回 "此状态无活动警报。"; }

            return string.Join("\n--\n", alerts.Select(alert =>
            {
                JsonElement properties = alert.GetProperty("properties");
                return $"""
                        Event: {properties.GetProperty("event").GetString()}
                        Area: {properties.GetProperty("areaDesc").GetString()}
                        Severity: {properties.GetProperty("severity").GetString()}
                        Description: {properties.GetProperty("description").GetString()}
                        Instruction: {properties.GetProperty("instruction").GetString()}
                        """;
            }));
        }
返回 string.Join("\n--\n", alerts.Select(alert => { JsonElement properties = alert.GetProperty("properties"); 返回 $""" 事件: {properties.GetProperty("event").GetString()} 区域: {properties.GetProperty("areaDesc").GetString()} 严重程度: {properties.GetProperty("severity").GetString()} 描述: {properties.GetProperty("description").GetString()} 指示: {properties.GetProperty("instruction").GetString()} """; })); }

        [McpServerTool, Description("Get weather forecast for a location.")]
        public static async Task<string> GetForecast(
            HttpClient client,
            [Description("Latitude of the location.")] double latitude,
            [Description("Longitude of the location.")] double longitude)
        {
            var jsonElement = await client.GetFromJsonAsync<JsonElement>($"/points/{latitude},{longitude}");
            var periods = jsonElement.GetProperty("properties").GetProperty("periods").EnumerateArray();
[McpServerTool, 描述("获取位置的天气预报。")] public static async Task GetForecast(HttpClient client, [描述("位置的纬度。")] double latitude, [描述("位置的经度。")] double longitude) { var jsonElement = await client.GetFromJsonAsync($"/points/{latitude},{longitude}"); var periods = jsonElement.GetProperty("properties").GetProperty("periods").EnumerateArray();

            return string.Join("\n---\n", periods.Select(period => $"""
                    {period.GetProperty("name").GetString()}
                    Temperature: {period.GetProperty("temperature").GetInt32()}°F
                    Wind: {period.GetProperty("windSpeed").GetString()} {period.GetProperty("windDirection").GetString()}
                    Forecast: {period.GetProperty("detailedForecast").GetString()}
                    """));
        }
    }
    ```
return string.Join("\n---\n", periods.Select(period => $""" {period.GetProperty("name").GetString()} 温度: {period.GetProperty("temperature").GetInt32()}°F 风速: {period.GetProperty("windSpeed").GetString()} {period.GetProperty("windDirection").GetString()} 预报: {period.GetProperty("detailedForecast").GetString()} """)); } }

    ### Running the server
### 运行服务器

    Finally, run the server using the following command:
最后，使用以下命令运行服务器：

    ```bash
    dotnet run
    ```

    This will start the server and listen for incoming requests on standard input/output.
这将启动服务器并监听标准输入/输出上的传入请求。

    ## Testing your server with Claude for Desktop
## 使用 Claude for Desktop 测试您的服务器

    <Note>
      Claude for Desktop is not yet available on Linux. Linux users can proceed to the [Building a client](/quickstart/client) tutorial to build an MCP client that connects to the server we just built.
    </Note>
<注意> Claude for Desktop 目前尚未在 Linux 上提供。Linux 用户可以前往 [构建客户端](/quickstart/client) 教程，构建一个连接到我们刚刚构建的服务器的 MCP 客户端。

    First, make sure you have Claude for Desktop installed. [You can install the latest version
    here.](https://claude.ai/download) If you already have Claude for Desktop, **make sure it's updated to the latest version.**
    We'll need to configure Claude for Desktop for whichever MCP servers you want to use. To do this, open your Claude for Desktop App configuration at `~/Library/Application Support/Claude/claude_desktop_config.json` in a text editor. Make sure to create the file if it doesn't exist.
    For example, if you have [VS Code](https://code.visualstudio.com/) installed:
首先，请确保您已安装 Claude for Desktop。[您可以从这里安装最新版本。](https://claude.ai/download) 如果您已经安装了 Claude for Desktop，**请确保它已更新到最新版本。** 我们需要配置 Claude for Desktop 以使用您想要的任何 MCP 服务器。为此，请打开您的 Claude for Desktop 应用程序配置文件 `~/Library/Application Support/Claude/claude_desktop_config.json`，在文本编辑器中打开。如果文件不存在，请创建它。例如，如果您已安装 [VS Code](https://code.visualstudio.com/)：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        code ~/Library/Application\ Support/Claude/claude_desktop_config.json
        ```
      </Tab>

      <Tab title="Windows">
        ```powershell
        code $env:AppData\Claude\claude_desktop_config.json
        ```
      </Tab>
    </Tabs>

    You'll then add your servers in the `mcpServers` key. The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.
    In this case, we'll add our single weather server like so:
您接下来需要在 `mcpServers` 键中添加您的服务器。只有当至少配置了一个服务器后，MCP UI 元素才会显示在 Claude for Desktop 中。在本例中，我们将添加我们的单个天气服务器，如下所示：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```json
        {
            "mcpServers": {
                "weather": {
                    "command": "dotnet",
                    "args": [
                        "run",
                        "--project",
                        "/ABSOLUTE/PATH/TO/PROJECT",
                        "--no-build"
                    ]
                }
            }
        }
        ```
      </Tab>

      <Tab title="Windows">
        ```json
        {
            "mcpServers": {
                "weather": {
                    "command": "dotnet",
                    "args": [
                        "run",
                        "--project",
                        "C:\\ABSOLUTE\\PATH\\TO\\PROJECT",
                        "--no-build"
                    ]
                }
            }
        }
        ```
      </Tab>
    </Tabs>
 ```json { "mcpServers": { "weather": { "command": "dotnet", "args": [ "run", "--project", "C:\\ABSOLUTE\\PATH\\TO\\PROJECT", "--no-build" ] } } } ```  

    This tells Claude for Desktop:
这告诉 Claude for Desktop：

    1. There's an MCP server named "weather"
    2. Launch it by running `dotnet run /ABSOLUTE/PATH/TO/PROJECT`
       Save the file, and restart **Claude for Desktop**.
  </Tab>
</Tabs>
1. 有一个名为 "weather" 的 MCP 服务器 2. 通过运行 `dotnet run /ABSOLUTE/PATH/TO/PROJECT` 启动它。保存文件，并重新启动 **Claude for Desktop**。  

### Test with commands  ### 使用命令进行测试

Let's make sure Claude for Desktop is picking up the two tools we've exposed in our `weather` server. You can do this by looking for the hammer <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-hammer-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} /> icon:
确保 Claude for Desktop 能够识别我们在`weather`服务器中暴露的两个工具。你可以通过查找锤子图标  来完成此操作：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/visual-indicator-mcp-tools.png" />
</Frame>

After clicking on the hammer icon, you should see two tools listed:
点击锤子图标后，你应该能看到列出的两个工具：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/available-mcp-tools.png" />
</Frame>

If your server isn't being picked up by Claude for Desktop, proceed to the [Troubleshooting](#troubleshooting) section for debugging tips.
如果您的服务器没有被 Claude for Desktop 识别，请转到[故障排除](#troubleshooting)部分以获取调试技巧。

If the hammer icon has shown up, you can now test your server by running the following commands in Claude for Desktop:
如果锤子图标已经出现，您现在可以在 Claude for Desktop 中运行以下命令来测试您的服务器：

* What's the weather in Sacramento?
* What are the active weather alerts in Texas?
* 萨克拉门托的天气怎么样？ * 德克萨斯州有哪些活跃的天气警报？

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/current-weather.png" />
</Frame>

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/weather-alerts.png" />
</Frame>

<Note>
  Since this is the US National Weather service, the queries will only work for US locations.
</Note>
 由于这是美国国家气象服务，查询将仅适用于美国地区。 

## What's happening under the hood
## 发生在引擎盖下的事情

When you ask a question:
当你提出问题时：

1. The client sends your question to Claude
2. Claude analyzes the available tools and decides which one(s) to use
3. The client executes the chosen tool(s) through the MCP server
4. The results are sent back to Claude
5. Claude formulates a natural language response
6. The response is displayed to you!
1. 客户将问题发送给 Claude 2. Claude 分析可用工具并决定使用哪个（些）工具 3. 客户通过 MCP 服务器执行所选工具（们） 4. 结果发送回 Claude 5. Claude 构建自然语言响应 6. 响应显示给您！

## Troubleshooting  ## 故障排除

<AccordionGroup>
  <Accordion title="Claude for Desktop Integration Issues">
    **Getting logs from Claude for Desktop**
  **从 Claude 桌面获取日志**

    Claude.app logging related to MCP is written to log files in `~/Library/Logs/Claude`:
Claude.app 与 MCP 相关的日志记录在`~/Library/Logs/Claude`的日志文件中：

    * `mcp.log` will contain general logging about MCP connections and connection failures.
    * Files named `mcp-server-SERVERNAME.log` will contain error (stderr) logging from the named server.
*mcp.log 将包含有关 MCP 连接和连接失败的常规日志。* 命名为`mcp-server-SERVERNAME.log`的文件将包含指定服务器的错误（stderr）日志。

    You can run the following command to list recent logs and follow along with any new ones:
您可以使用以下命令列出最近的日志并跟踪任何新的日志：

    ```bash
    # Check Claude's logs for errors
    tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
    ```
```bash # 检查 Claude 的日志错误 tail -n 20 -f ~/Library/Logs/Claude/mcp*.log ```

    **Server not showing up in Claude**
**服务器在 Claude 中未显示**

    1. Check your `claude_desktop_config.json` file syntax
    2. Make sure the path to your project is absolute and not relative
    3. Restart Claude for Desktop completely
1. 检查您的`claude_desktop_config.json`文件语法 2. 确保您的项目路径是绝对路径而不是相对路径 3. 完全重启 Claude 桌面版

    **Tool calls failing silently**
**工具调用静默失败**

    If Claude attempts to use the tools but they fail:
如果 Claude 尝试使用工具但它们失败了：

    1. Check Claude's logs for errors
    2. Verify your server builds and runs without errors
    3. Try restarting Claude for Desktop
1. 检查 Claude 的日志以查找错误 2. 验证您的服务器构建和运行没有错误 3. 尝试重新启动 Claude 桌面版

    **None of this is working. What do I do?**
**以上方法都不起作用。我该怎么办？**

    Please refer to our [debugging guide](/docs/tools/debugging) for better debugging tools and more detailed guidance.
  </Accordion>
请参阅我们的[调试指南](/docs/tools/debugging)，以获取更好的调试工具和更详细的指导。

  <Accordion title="Weather API Issues">
    **Error: Failed to retrieve grid point data**
折叠面板标题：“天气 API 问题”**错误：无法检索网格点数据**

    This usually means either:
这通常意味着：

    1. The coordinates are outside the US
    2. The NWS API is having issues
    3. You're being rate limited
1. 坐标在美国之外 2. NWS API 存在问题 3. 您正在被限制访问速率

    Fix:  修复：

    * Verify you're using US coordinates
    * Add a small delay between requests
    * Check the NWS API status page
* 确认您正在使用美国坐标 * 在请求之间添加一个小的延迟 * 检查 NWS API 状态页面

    **Error: No active alerts for \[STATE]**
**错误：[州] 没有活跃警报**

    This isn't an error - it just means there are no current weather alerts for that state. Try a different state or check during severe weather.
  </Accordion>
</AccordionGroup>
这不是错误 - 这只是意味着该州目前没有当前的天气警报。尝试另一个州或在恶劣天气期间检查。 

<Note>
  For more advanced troubleshooting, check out our guide on [Debugging MCP](/docs/tools/debugging)
</Note>
为了更高级的故障排除，请查看我们的[调试 MCP](/docs/tools/debugging)指南

## Next steps  下一步

<CardGroup cols={2}>
  <Card title="Building a client" icon="outlet" href="/quickstart/client">
    Learn how to build your own MCP client that can connect to your server
  </Card>
 学习如何构建自己的 MCP 客户端，使其能够连接到您的服务器 

  <Card title="Example servers" icon="grid" href="/examples">
    Check out our gallery of official MCP servers and implementations
  </Card>
查看我们的官方 MCP 服务器和实现示例画廊

  <Card title="Debugging Guide" icon="bug" href="/docs/tools/debugging">
    Learn how to effectively debug MCP servers and integrations
  </Card>
学习如何有效地调试 MCP 服务器和集成

  <Card title="Building MCP with LLMs" icon="comments" href="/tutorials/building-mcp-with-llms">
    Learn how to use LLMs like Claude to speed up your MCP development
  </Card>
</CardGroup>
学习如何像 Claude 一样使用LLMs来加速您的 MCP 开发 


# For Claude Desktop Users
Source: https://modelcontextprotocol.io/quickstart/user
# 为 Claude 桌面用户来源：https://modelcontextprotocol.io/quickstart/user

Get started using pre-built servers in Claude for Desktop.
在 Claude 桌面中开始使用预构建的服务器。

In this tutorial, you will extend [Claude for Desktop](https://claude.ai/download) so that it can read from your computer's file system, write new files, move files, and even search files.
在本教程中，您将扩展[Claude 桌面](https://claude.ai/download)，使其能够从您的计算机文件系统中读取，写入新文件，移动文件，甚至搜索文件。

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-filesystem.png" />
</Frame>

Don't worry — it will ask you for your permission before executing these actions!
别担心 — 它会在执行这些操作之前询问您的权限！

## 1. Download Claude for Desktop
## 1. 下载桌面版 Claude

Start by downloading [Claude for Desktop](https://claude.ai/download), choosing either macOS or Windows. (Linux is not yet supported for Claude for Desktop.)
首先下载 [桌面版 Claude](https://claude.ai/download)，选择 macOS 或 Windows。（桌面版 Claude 目前不支持 Linux。）

Follow the installation instructions.
按照安装说明进行操作。

If you already have Claude for Desktop, make sure it's on the latest version by clicking on the Claude menu on your computer and selecting "Check for Updates..."
如果您已经安装了 Claude for Desktop，请确保它是最新版本，通过点击电脑上的 Claude 菜单并选择“检查更新...”来确认。

<Accordion title="Why Claude for Desktop and not Claude.ai?">
  Because servers are locally run, MCP currently only supports desktop hosts. Remote hosts are in active development.
</Accordion>
 因为服务器是本地运行的，MCP 目前仅支持桌面主机。远程主机正在积极开发中。 

## 2. Add the Filesystem MCP Server
## 2. 添加文件系统 MCP 服务器

To add this filesystem functionality, we will be installing a pre-built [Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) to Claude for Desktop. This is one of dozens of [servers](https://github.com/modelcontextprotocol/servers/tree/main) created by Anthropic and the community.
要添加此文件系统功能，我们将安装一个预构建的[文件系统 MCP 服务器](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)到 Claude for Desktop。这是由 Anthropic 和社区创建的数十个[服务器](https://github.com/modelcontextprotocol/servers/tree/main)之一。

Get started by opening up the Claude menu on your computer and select "Settings..." Please note that these are not the Claude Account Settings found in the app window itself.
通过打开电脑上的 Claude 菜单并选择“设置...”开始使用。请注意，这些不是在应用窗口中找到的 Claude 账户设置。

This is what it should look like on a Mac:
这就是它在 Mac 上的样子：

<Frame style={{ textAlign: 'center' }}>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-menu.png" width="400" />
</Frame>

Click on "Developer" in the left-hand bar of the Settings pane, and then click on "Edit Config":
在设置窗口的左侧栏中点击“开发者”，然后点击“编辑配置”：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-developer.png" />
</Frame>

This will create a configuration file at:
这将创建一个配置文件在：

* macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
* Windows: `%APPDATA%\Claude\claude_desktop_config.json`

if you don't already have one, and will display the file in your file system.
如果您还没有，并且将在您的文件系统中显示该文件。

Open up the configuration file in any text editor. Replace the file contents with this:
使用任何文本编辑器打开配置文件。将文件内容替换为以下内容：

<Tabs>
  <Tab title="MacOS/Linux">
    ```json
    {
      "mcpServers": {
        "filesystem": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "/Users/username/Desktop",
            "/Users/username/Downloads"
          ]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Windows">
    ```json
    {
      "mcpServers": {
        "filesystem": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "C:\\Users\\username\\Desktop",
            "C:\\Users\\username\\Downloads"
          ]
        }
      }
    }
    ```
  </Tab>
</Tabs>

Make sure to replace `username` with your computer's username. The paths should point to valid directories that you want Claude to be able to access and modify. It's set up to work for Desktop and Downloads, but you can add more paths as well.
确保将 `username` 替换为您的计算机用户名。路径应指向您希望 Claude 能够访问和修改的有效目录。默认设置为桌面和下载，但您也可以添加更多路径。

You will also need [Node.js](https://nodejs.org) on your computer for this to run properly. To verify you have Node installed, open the command line on your computer.
您的计算机上还需要安装 [Node.js](https://nodejs.org) 才能正常运行。要验证是否已安装 Node，请打开计算机上的命令行。

* On macOS, open the Terminal from your Applications folder
* On Windows, press Windows + R, type "cmd", and press Enter
* 在 macOS 上，从应用程序文件夹中打开终端 * 在 Windows 上，按 Windows + R，输入 "cmd"，然后按 Enter

Once in the command line, verify you have Node installed by entering in the following command:
进入命令行后，通过输入以下命令来验证您已安装 Node：

```bash
node --version
```

If you get an error saying "command not found" or "node is not recognized", download Node from [nodejs.org](https://nodejs.org/).
如果出现错误提示“命令未找到”或“未识别 node”，请从 [nodejs.org](https://nodejs.org/) 下载 Node。

<Tip>
  **How does the configuration file work?**
<提示> **配置文件是如何工作的？**

  This configuration file tells Claude for Desktop which MCP servers to start up every time you start the application. In this case, we have added one server called "filesystem" that will use the Node `npx` command to install and run `@modelcontextprotocol/server-filesystem`. This server, described [here](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem), will let you access your file system in Claude for Desktop.
</Tip>
这个配置文件告诉 Claude for Desktop 在每次启动应用程序时启动哪些 MCP 服务器。在这种情况下，我们添加了一个名为“filesystem”的服务器，该服务器将使用 Node `npx` 命令安装并运行 `@modelcontextprotocol/server-filesystem`。这个服务器，如[此处](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)所述，将允许你在 Claude for Desktop 中访问你的文件系统。

<Warning>
  **Command Privileges**
<警告> **命令权限**

  Claude for Desktop will run the commands in the configuration file with the permissions of your user account, and access to your local files. Only add commands if you understand and trust the source.
</Warning>
Claude for Desktop 将以你的用户账户权限运行配置文件中的命令，并访问你的本地文件。只有在你理解并信任来源的情况下才添加命令。

## 3. Restart Claude  ## 3. 重新启动 Claude

After updating your configuration file, you need to restart Claude for Desktop.
更新配置文件后，您需要重新启动 Claude for Desktop。

Upon restarting, you should see a hammer <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-hammer-icon.svg" style={{display: 'inline', margin: 0, height: '1.3em'}} /> icon in the bottom right corner of the input box:
重新启动后，您应该在输入框的右下角看到锤子图标 ：

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-hammer.png" />
</Frame>

After clicking on the hammer icon, you should see the tools that come with the Filesystem MCP Server:
点击锤子图标后，您应该能看到与文件系统 MCP 服务器一起提供的工具：

<Frame style={{ textAlign: 'center' }}>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-tools.png" width="400" />
</Frame>

If your server isn't being picked up by Claude for Desktop, proceed to the [Troubleshooting](#troubleshooting) section for debugging tips.
如果您的服务器没有被 Claude for Desktop 识别，请转到[故障排除](#troubleshooting)部分以获取调试技巧。

## 4. Try it out!
## 4. 尝试一下！

You can now talk to Claude and ask it about your filesystem. It should know when to call the relevant tools.
现在，您可以与 Claude 交谈并询问有关文件系统的问题。它应该知道何时调用相关工具。

Things you might try asking Claude:
你可能会尝试询问 Claude 的内容：

* Can you write a poem and save it to my desktop?
* What are some work-related files in my downloads folder?
* Can you take all the images on my desktop and move them to a new folder called "Images"?
* 能否为我写一首诗并保存到我的桌面？ * 我的下载文件夹中有哪些与工作相关的文件？ * 能否将我桌面上的所有图片移动到一个名为“图片”的新文件夹中？

As needed, Claude will call the relevant tools and seek your approval before taking an action:
如有需要，Claude 将调用相关工具并在采取行动前寻求您的批准：

<Frame style={{ textAlign: 'center' }}>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-approve.png" width="500" />
</Frame>

## Troubleshooting  故障排除

<AccordionGroup>
  <Accordion title="Server not showing up in Claude / hammer icon missing">
    1. Restart Claude for Desktop completely
    2. Check your `claude_desktop_config.json` file syntax
    3. Make sure the file paths included in `claude_desktop_config.json` are valid and that they are absolute and not relative
    4. Look at [logs](#getting-logs-from-claude-for-desktop) to see why the server is not connecting
    5. In your command line, try manually running the server (replacing `username` as you did in `claude_desktop_config.json`) to see if you get any errors:
  1. 完全重启 Claude for Desktop 2. 检查您的 `claude_desktop_config.json` 文件语法 3. 确保包含在 `claude_desktop_config.json` 中的文件路径是有效的，并且它们是绝对路径而不是相对路径 4. 查看 [日志](#从 Claude for Desktop 获取日志) 以了解服务器未连接的原因 5. 在您的命令行中，尝试手动运行服务器（替换 `username` 为您在 `claude_desktop_config.json` 中使用的用户名）以查看是否有任何错误：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        npx -y @modelcontextprotocol/server-filesystem /Users/username/Desktop /Users/username/Downloads
        ```
      </Tab>

      <Tab title="Windows">
        ```bash
        npx -y @modelcontextprotocol/server-filesystem C:\Users\username\Desktop C:\Users\username\Downloads
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Getting logs from Claude for Desktop">
    Claude.app logging related to MCP is written to log files in:
与 MCP 相关的 Claude.app 日志被写入以下日志文件中：

    * macOS: `~/Library/Logs/Claude`

    * Windows: `%APPDATA%\Claude\logs`

    * `mcp.log` will contain general logging about MCP connections and connection failures.
* `mcp.log` 将包含有关 MCP 连接和连接失败的常规日志。

    * Files named `mcp-server-SERVERNAME.log` will contain error (stderr) logging from the named server.
* 命名为 `mcp-server-SERVERNAME.log` 的文件将包含来自指定服务器的错误（stderr）日志。

    You can run the following command to list recent logs and follow along with any new ones (on Windows, it will only show recent logs):
您可以使用以下命令列出最近的日志并跟踪任何新的日志（在 Windows 上，它只会显示最近的日志）：

    <Tabs>
      <Tab title="MacOS/Linux">
        ```bash
        # Check Claude's logs for errors
        tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
        ```
      </Tab>
  ```bash # 检查 Claude 的日志错误 tail -n 20 -f ~/Library/Logs/Claude/mcp*.log ``` 

      <Tab title="Windows">
        ```bash
        type "%APPDATA%\Claude\logs\mcp*.log"
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Tool calls failing silently">
    If Claude attempts to use the tools but they fail:
如果 Claude 尝试使用工具但它们失败：

    1. Check Claude's logs for errors
    2. Verify your server builds and runs without errors
    3. Try restarting Claude for Desktop
  </Accordion>
1. 检查 Claude 的日志以查找错误 2. 验证您的服务器构建和运行是否没有错误 3. 尝试重新启动 Claude 桌面版

  <Accordion title="None of this is working. What do I do?">
    Please refer to our [debugging guide](/docs/tools/debugging) for better debugging tools and more detailed guidance.
  </Accordion>
请参阅我们的[调试指南](/docs/tools/debugging)，以获取更好的调试工具和更详细的指导。

  <Accordion title="ENOENT error and `${APPDATA}` in paths on Windows">
    If your configured server fails to load, and you see within its logs an error referring to `${APPDATA}` within a path, you may need to add the expanded value of `%APPDATA%` to your `env` key in `claude_desktop_config.json`:
如果您的配置服务器无法加载，并在其日志中看到引用路径中的`${APPDATA}`的错误，您可能需要将`%APPDATA%`的展开值添加到`claude_desktop_config.json`中的`env`键：

    ```json
    {
      "brave-search": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-brave-search"],
        "env": {
          "APPDATA": "C:\\Users\\user\\AppData\\Roaming\\",
          "BRAVE_API_KEY": "..."
        }
      }
    }
    ```

    With this change in place, launch Claude Desktop once again.
在此更改生效后，再次启动 Claude 桌面。

    <Warning>
      **NPM should be installed globally**
<警告> **应全局安装 NPM**

      The `npx` command may continue to fail if you have not installed NPM globally. If NPM is already installed globally, you will find `%APPDATA%\npm` exists on your system. If not, you can install NPM globally by running the following command:
如果您未全局安装 NPM，`npx` 命令可能会继续失败。如果 NPM 已经全局安装，您将在系统上找到 `%APPDATA%\npm`。如果没有，您可以通过运行以下命令全局安装 NPM：

      ```bash
      npm install -g npm
      ```
    </Warning>
  </Accordion>
</AccordionGroup>

## Next steps  下一步

<CardGroup cols={2}>
  <Card title="Explore other servers" icon="grid" href="/examples">
    Check out our gallery of official MCP servers and implementations
  </Card>
  查看我们的官方 MCP 服务器和实现示例库 

  <Card title="Build your own server" icon="code" href="/quickstart/server">
    Now build your own custom server to use in Claude for Desktop and other clients
  </Card>
</CardGroup>
 现在构建您自己的自定义服务器，用于 Claude for Desktop 和其他客户端  


# MCP Client
Source: https://modelcontextprotocol.io/sdk/java/mcp-client
# MCP 客户端源：https://modelcontextprotocol.io/sdk/java/mcp-client

Learn how to use the Model Context Protocol (MCP) client to interact with MCP servers
学习如何使用模型上下文协议（MCP）客户端与 MCP 服务器交互

# Model Context Protocol Client
# 模型上下文协议客户端

The MCP Client is a key component in the Model Context Protocol (MCP) architecture, responsible for establishing and managing connections with MCP servers. It implements the client-side of the protocol, handling:
MCP 客户端是模型上下文协议（MCP）架构中的关键组件，负责建立和管理与 MCP 服务器的连接。它实现了协议的客户端部分，处理以下功能：

* Protocol version negotiation to ensure compatibility with servers
* Capability negotiation to determine available features
* Message transport and JSON-RPC communication
* Tool discovery and execution
* Resource access and management
* Prompt system interactions
* Optional features like roots management and sampling support
* 协议版本协商以确保与服务器兼容 * 功能协商以确定可用功能 * 消息传输和 JSON-RPC 通信 * 工具发现和执行 * 资源访问和管理 * 提示系统交互 * 可选功能如根管理和支持采样

<Tip>
  The core `io.modelcontextprotocol.sdk:mcp` module provides STDIO and SSE client transport implementations  without requiring external web frameworks.
<提示> 核心模块 `io.modelcontextprotocol.sdk:mcp` 提供了 STDIO 和 SSE 客户端传输实现，无需外部 Web 框架。

  Spring-specific transport implementations are available as an **optional** dependency `io.modelcontextprotocol.sdk:mcp-spring-webflux` for [Spring Framework](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html) users.
</Tip>
专为 Spring 框架用户提供的特定传输实现作为 **可选** 依赖项 `io.modelcontextprotocol.sdk:mcp-spring-webflux`。[Spring 框架](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html) 用户可以使用。 

The client provides both synchronous and asynchronous APIs for flexibility in different application contexts.
客户端提供同步和异步 API，以适应不同的应用场景。

<Tabs>
  <Tab title="Sync API">
    ```java
    // Create a sync client with custom configuration
    McpSyncClient client = McpClient.sync(transport)
        .requestTimeout(Duration.ofSeconds(10))
        .capabilities(ClientCapabilities.builder()
            .roots(true)      // Enable roots capability
            .sampling()       // Enable sampling capability
            .build())
        .sampling(request -> new CreateMessageResult(response))
        .build();
<标签> <标签标题="同步 API"> ```java // 使用自定义配置创建同步客户端 McpSyncClient client = McpClient.sync(transport) .requestTimeout(Duration.ofSeconds(10)) .capabilities(ClientCapabilities.builder() .roots(true) // 启用 roots 功能 .sampling() // 启用采样功能 .build()) .sampling(request -> new CreateMessageResult(response)) .build();

    // Initialize connection
    client.initialize();
// 初始化连接 client.initialize();

    // List available tools
    ListToolsResult tools = client.listTools();
// 列出可用工具 ListToolsResult tools = client.listTools();

    // Call a tool
    CallToolResult result = client.callTool(
        new CallToolRequest("calculator", 
            Map.of("operation", "add", "a", 2, "b", 3))
    );
// 调用一个工具 CallToolResult result = client.callTool( new CallToolRequest("calculator", Map.of("operation", "add", "a", 2, "b", 3)) );

    // List and read resources
    ListResourcesResult resources = client.listResources();
    ReadResourceResult resource = client.readResource(
        new ReadResourceRequest("resource://uri")
    );
// 列出并读取资源 ListResourcesResult resources = client.listResources(); ReadResourceResult resource = client.readResource( new ReadResourceRequest("resource://uri") );

    // List and use prompts
    ListPromptsResult prompts = client.listPrompts();
    GetPromptResult prompt = client.getPrompt(
        new GetPromptRequest("greeting", Map.of("name", "Spring"))
    );
// 获取提示列表 ListPromptsResult prompts = client.listPrompts(); 获取提示结果 GetPromptResult prompt = client.getPrompt(new GetPromptRequest("greeting", Map.of("name", "Spring")));

    // Add/remove roots
    client.addRoot(new Root("file:///path", "description"));
    client.removeRoot("file:///path");
// 添加/移除根 client.addRoot(new Root("file:///path", "description")); client.removeRoot("file:///path");

    // Close client
    client.closeGracefully();
    ```
  </Tab>
// 关闭客户端 client.closeGracefully(); ``` 

  <Tab title="Async API">
    ```java
    // Create an async client with custom configuration
    McpAsyncClient client = McpClient.async(transport)
        .requestTimeout(Duration.ofSeconds(10))
        .capabilities(ClientCapabilities.builder()
            .roots(true)      // Enable roots capability
            .sampling()       // Enable sampling capability
            .build())
        .sampling(request -> Mono.just(new CreateMessageResult(response)))
        .toolsChangeConsumer(tools -> Mono.fromRunnable(() -> {
            logger.info("Tools updated: {}", tools);
        }))
        .resourcesChangeConsumer(resources -> Mono.fromRunnable(() -> {
            logger.info("Resources updated: {}", resources);
        }))
        .promptsChangeConsumer(prompts -> Mono.fromRunnable(() -> {
            logger.info("Prompts updated: {}", prompts);
        }))
        .build();
 ```java // 使用自定义配置创建异步客户端 McpAsyncClient client = McpClient.async(transport) .requestTimeout(Duration.ofSeconds(10)) .capabilities(ClientCapabilities.builder() .roots(true) // 启用根能力 .sampling() // 启用采样能力 .build()) .sampling(request -> Mono.just(new CreateMessageResult(response))) .toolsChangeConsumer(tools -> Mono.fromRunnable(() -> { logger.info("Tools updated: {}", tools); })) .resourcesChangeConsumer(resources -> Mono.fromRunnable(() -> { logger.info("Resources updated: {}", resources); })) .promptsChangeConsumer(prompts -> Mono.fromRunnable(() -> { logger.info("Prompts updated: {}", prompts); })) .build();

    // Initialize connection and use features
    client.initialize()
        .flatMap(initResult -> client.listTools())
        .flatMap(tools -> {
            return client.callTool(new CallToolRequest(
                "calculator", 
                Map.of("operation", "add", "a", 2, "b", 3)
            ));
        })
        .flatMap(result -> {
            return client.listResources()
                .flatMap(resources -> 
                    client.readResource(new ReadResourceRequest("resource://uri"))
                );
        })
        .flatMap(resource -> {
            return client.listPrompts()
                .flatMap(prompts ->
                    client.getPrompt(new GetPromptRequest(
                        "greeting", 
                        Map.of("name", "Spring")
                    ))
                );
        })
        .flatMap(prompt -> {
            return client.addRoot(new Root("file:///path", "description"))
                .then(client.removeRoot("file:///path"));            
        })
        .doFinally(signalType -> {
            client.closeGracefully().subscribe();
        })
        .subscribe();
    ```
  </Tab>
</Tabs>
初始化连接并使用功能客户端.client.initialize().flatMap(initResult -> client.listTools()).flatMap(tools -> { return client.callTool(new CallToolRequest( "calculator", Map.of("operation", "add", "a", 2, "b", 3) )); }).flatMap(result -> { return client.listResources().flatMap(resources -> client.readResource(new ReadResourceRequest("resource://uri")) ); }).flatMap(resource -> { return client.listPrompts().flatMap(prompts -> client.getPrompt(new GetPromptRequest( "greeting", Map.of("name", "Spring") )) ); }).flatMap(prompt -> { return client.addRoot(new Root("file:///path", "description")).then(client.removeRoot("file:///path")); }).doFinally(signalType -> { client.closeGracefully().subscribe(); }).subscribe();

## Client Transport  客户端传输

The transport layer handles the communication between MCP clients and servers, providing different implementations for various use cases. The client transport manages message serialization, connection establishment, and protocol-specific communication patterns.
传输层处理 MCP 客户端和服务器之间的通信，为各种用例提供不同的实现。客户端传输管理消息序列化、连接建立和特定协议的通信模式。

<Tabs>
  <Tab title="STDIO">
    Creates transport for in-process based communication
  创建基于进程内通信的传输

    ```java
    ServerParameters params = ServerParameters.builder("npx")
        .args("-y", "@modelcontextprotocol/server-everything", "dir")
        .build();
    McpTransport transport = new StdioClientTransport(params);
    ```
  </Tab>

  <Tab title="SSE (HttpClient)">
    Creates a framework agnostic (pure Java API) SSE client transport. Included in the core mcp module.
 创建一个框架无关（纯 Java API）的 SSE 客户端传输。包含在核心 mcp 模块中。

    ```java
    McpTransport transport = new HttpClientSseClientTransport("http://your-mcp-server");
    ```
  </Tab>

  <Tab title="SSE (WebFlux)">
    Creates WebFlux-based SSE client transport. Requires the mcp-webflux-sse-transport dependency.
 创建基于 WebFlux 的 SSE 客户端传输。需要 mcp-webflux-sse-transport 依赖项。

    ```java
    WebClient.Builder webClientBuilder = WebClient.builder()
        .baseUrl("http://your-mcp-server");
    McpTransport transport = new WebFluxSseClientTransport(webClientBuilder);
    ```
  </Tab>
</Tabs>

## Client Capabilities  ## 客户端功能

The client can be configured with various capabilities:
客户端可以配置各种功能：

```java
var capabilities = ClientCapabilities.builder()
    .roots(true)      // Enable filesystem roots support with list changes notifications
    .sampling()       // Enable LLM sampling support
    .build();
```
```java var capabilities = ClientCapabilities.builder() .roots(true) // 启用文件系统根支持，带有列表更改通知 .sampling() // 启用 LLM 样本支持 .build(); ```

### Roots Support  根支持

Roots define the boundaries of where servers can operate within the filesystem:
根定义了服务器在文件系统中可以操作的范围：

```java
// Add a root dynamically
client.addRoot(new Root("file:///path", "description"));
```java // 动态添加根 client.addRoot(new Root("file:///path", "description"));

// Remove a root
client.removeRoot("file:///path");
// 移除根 client.removeRoot("file:///path");

// Notify server of roots changes
client.rootsListChangedNotification();
```
// 通知服务器根目录变更 client.rootsListChangedNotification(); ```

The roots capability allows servers to:
根能力允许服务器：

* Request the list of accessible filesystem roots
* Receive notifications when the roots list changes
* Understand which directories and files they have access to
* 请求可访问的文件系统根目录列表 * 接收根目录列表变更通知 * 理解它们可以访问哪些目录和文件

### Sampling Support  ### 样本支持

Sampling enables servers to request LLM interactions ("completions" or "generations") through the client:
样本化使服务器能够通过客户端请求 LLM 次交互（“完成”或“生成”）：

```java
// Configure sampling handler
Function<CreateMessageRequest, CreateMessageResult> samplingHandler = request -> {
    // Sampling implementation that interfaces with LLM
    return new CreateMessageResult(response);
};
```java // 配置采样处理程序 Function samplingHandler = request -> { // 采样实现与 LLM 接口 return new CreateMessageResult(response); };

// Create client with sampling support
var client = McpClient.sync(transport)
    .capabilities(ClientCapabilities.builder()
        .sampling()
        .build())
    .sampling(samplingHandler)
    .build();
```
// 创建具有采样支持的客户端 var client = McpClient.sync(transport) .capabilities(ClientCapabilities.builder() .sampling() .build()) .sampling(samplingHandler) .build(); ```

This capability allows:  此功能允许：

* Servers to leverage AI capabilities without requiring API keys
* Clients to maintain control over model access and permissions
* Support for both text and image-based interactions
* Optional inclusion of MCP server context in prompts
* 利用 AI 能力而无需 API 密钥的服务器 * 客户端维护对模型访问和权限的控制 * 支持基于文本和图像的交互 * 可选包含 MCP 服务器上下文在提示中

### Logging Support  ### 日志支持

The client can register a logging consumer to receive log messages from the server and set the minimum logging level to filter messages:
客户端可以注册日志消费者以接收来自服务器的日志消息，并设置最小日志级别以过滤消息：

```java
var mcpClient = McpClient.sync(transport)
        .loggingConsumer(notification -> {
            System.out.println("Received log message: " + notification.data());
        })
        .build();

mcpClient.initialize();

mcpClient.setLoggingLevel(McpSchema.LoggingLevel.INFO);

// Call the tool that can sends logging notifications
CallToolResult result = mcpClient.callTool(new McpSchema.CallToolRequest("logging-test", Map.of()));
```
// 调用可以发送日志通知的工具 CallToolResult result = mcpClient.callTool(new McpSchema.CallToolRequest("logging-test", Map.of())); ```

Clients can control the minimum logging level they receive through the `mcpClient.setLoggingLevel(level)` request. Messages below the set level will be filtered out.
Supported logging levels (in order of increasing severity): DEBUG (0), INFO (1), NOTICE (2), WARNING (3), ERROR (4), CRITICAL (5), ALERT (6), EMERGENCY (7)
客户可以通过 `mcpClient.setLoggingLevel(level)` 请求控制他们接收到的最小日志级别。低于设置级别的消息将被过滤。支持的日志级别（按严重程度递增排序）：DEBUG（0）、INFO（1）、NOTICE（2）、WARNING（3）、ERROR（4）、CRITICAL（5）、ALERT（6）、EMERGENCY（7）

## Using MCP Clients  使用 MCP 客户端

### Tool Execution  工具执行

Tools are server-side functions that clients can discover and execute. The MCP client provides methods to list available tools and execute them with specific parameters. Each tool has a unique name and accepts a map of parameters.
工具是服务器端函数，客户端可以查找并执行。MCP 客户端提供列出可用工具和执行它们的方法，每个工具都有一个唯一的名称，并接受参数映射。

<Tabs>
  <Tab title="Sync API">
    ```java
    // List available tools and their names
    var tools = client.listTools();
    tools.forEach(tool -> System.out.println(tool.getName()));
  ```java // 列出可用工具及其名称 var tools = client.listTools(); tools.forEach(tool -> System.out.println(tool.getName()));

    // Execute a tool with parameters
    var result = client.callTool("calculator", Map.of(
        "operation", "add",
        "a", 1,
        "b", 2
    ));
    ```
  </Tab>
// 执行一个带有参数的工具 var result = client.callTool("calculator", Map.of( "operation", "add", "a", 1, "b", 2 )); ``` 

  <Tab title="Async API">
    ```java
    // List available tools asynchronously
    client.listTools()
        .doOnNext(tools -> tools.forEach(tool -> 
            System.out.println(tool.getName())))
        .subscribe();
 ```java // 异步列出可用的工具 client.listTools() .doOnNext(tools -> tools.forEach(tool -> System.out.println(tool.getName()))) .subscribe();

    // Execute a tool asynchronously
    client.callTool("calculator", Map.of(
            "operation", "add",
            "a", 1,
            "b", 2
        ))
        .subscribe();
    ```
  </Tab>
</Tabs>
// 异步执行一个工具 client.callTool("calculator", Map.of( "operation", "add", "a", 1, "b", 2 )) .subscribe(); ```  

### Resource Access  ### 资源访问

Resources represent server-side data sources that clients can access using URI templates. The MCP client provides methods to discover available resources and retrieve their contents through a standardized interface.
资源代表客户端可以通过 URI 模板访问的服务端数据源。MCP 客户端提供方法来发现可用的资源并通过标准接口检索它们的内 容。

<Tabs>
  <Tab title="Sync API">
    ```java
    // List available resources and their names
    var resources = client.listResources();
    resources.forEach(resource -> System.out.println(resource.getName()));
  ```java // 列出可用的资源和它们的名称 var resources = client.listResources(); resources.forEach(resource -> System.out.println(resource.getName())); 

    // Retrieve resource content using a URI template
    var content = client.getResource("file", Map.of(
        "path", "/path/to/file.txt"
    ));
    ```
  </Tab>
// 使用 URI 模板检索资源内容 var content = client.getResource("file", Map.of( "path", "/path/to/file.txt" )); ``` 

  <Tab title="Async API">
    ```java
    // List available resources asynchronously
    client.listResources()
        .doOnNext(resources -> resources.forEach(resource -> 
            System.out.println(resource.getName())))
        .subscribe();
 ```java // 异步列出可用的资源 client.listResources() .doOnNext(resources -> resources.forEach(resource -> System.out.println(resource.getName()))) .subscribe(); 

    // Retrieve resource content asynchronously
    client.getResource("file", Map.of(
            "path", "/path/to/file.txt"
        ))
        .subscribe();
    ```
  </Tab>
</Tabs>
// 异步获取资源内容 client.getResource("file", Map.of( "path", "/path/to/file.txt" )).subscribe(); ```  

### Prompt System  ### 提示系统

The prompt system enables interaction with server-side prompt templates. These templates can be discovered and executed with custom parameters, allowing for dynamic text generation based on predefined patterns.
提示系统允许与服务器端提示模板交互。这些模板可以通过自定义参数进行发现和执行，从而根据预定义模式动态生成文本。

<Tabs>
  <Tab title="Sync API">
    ```java
    // List available prompt templates
    var prompts = client.listPrompts();
    prompts.forEach(prompt -> System.out.println(prompt.getName()));
  ```java // 列出可用的提示模板 var prompts = client.listPrompts(); prompts.forEach(prompt -> System.out.println(prompt.getName()));

    // Execute a prompt template with parameters
    var response = client.executePrompt("echo", Map.of(
        "text", "Hello, World!"
    ));
    ```
  </Tab>
// 执行一个带有参数的提示模板 var response = client.executePrompt("echo", Map.of( "text", "Hello, World!" )); ``` 

  <Tab title="Async API">
    ```java
    // List available prompt templates asynchronously
    client.listPrompts()
        .doOnNext(prompts -> prompts.forEach(prompt -> 
            System.out.println(prompt.getName())))
        .subscribe();
 ```java // 异步列出可用的提示模板 client.listPrompts() .doOnNext(prompts -> prompts.forEach(prompt -> System.out.println(prompt.getName()))) .subscribe();

    // Execute a prompt template asynchronously
    client.executePrompt("echo", Map.of(
            "text", "Hello, World!"
        ))
        .subscribe();
    ```
  </Tab>
</Tabs>
// 异步执行提示模板 client.executePrompt("echo", Map.of( "text", "Hello, World!" )) .subscribe(); ```  

### Using Completion  ### 使用补全

As part of the [Completion capabilities](/specification/2025-03-26/server/utilities/completion), MCP provides a provides a standardized way for servers to offer argument autocompletion suggestions for prompts and resource URIs.
作为[完成功能](/specification/2025-03-26/server/utilities/completion)的一部分，MCP 为服务器提供了一种标准化的方式，以便为提示和资源 URI 提供参数自动补全建议。

Check the [Server Completion capabilities](/sdk/java/mcp-server#completion-specification) to learn how to enable and configure completions on the server side.
查看如何启用和配置服务器端补全的[服务器完成功能](/sdk/java/mcp-server#completion-specification)。

On the client side, the MCP client provides methods to request auto-completions:
在客户端，MCP 客户端提供方法来请求自动补全：

<Tabs>
  <Tab title="Sync API">
    ```java
  ```java

    CompleteRequest request = new CompleteRequest(
            new PromptReference("code_review"),
            new CompleteRequest.CompleteArgument("language", "py"));

    CompleteResult result = syncMcpClient.completeCompletion(request);

    ```
  </Tab>

  <Tab title="Async API">
    ```java

    CompleteRequest request = new CompleteRequest(
            new PromptReference("code_review"),
            new CompleteRequest.CompleteArgument("language", "py"));
CompleteRequest 请求 = new CompleteRequest( new PromptReference("代码审查"), new CompleteRequest.CompleteArgument("language", "py"));

    Mono<CompleteResult> result = mcpClient.completeCompletion(request);
Mono结果 = mcpClient.completeCompletion(请求);

    ```
  </Tab>
</Tabs>


# Overview
Source: https://modelcontextprotocol.io/sdk/java/mcp-overview
# 概述 来源：https://modelcontextprotocol.io/sdk/java/mcp-overview

Introduction to the Model Context Protocol (MCP) Java SDK
模型上下文协议（MCP）Java SDK 简介

Java SDK for the [Model Context Protocol](https://modelcontextprotocol.org/docs/concepts/architecture)
enables standardized integration between AI models and tools.
模型上下文协议（MCP）Java SDK 可实现人工智能模型与工具之间的标准化集成。

<Note>
  ### Breaking Changes in 0.8.x ⚠️
<注意> 0.8.x 版本重大变更 ⚠️

  **Note:** Version 0.8.x introduces several breaking changes including a new session-based architecture.
  If you're upgrading from 0.7.0, please refer to the [Migration Guide](https://github.com/modelcontextprotocol/java-sdk/blob/main/migration-0.8.0.md) for detailed instructions.
</Note>
**注意：** 0.8.x 版本引入了包括基于会话的新架构在内的多个重大变更。如果您从 0.7.0 版本升级，请参阅[迁移指南](https://github.com/modelcontextprotocol/java-sdk/blob/main/migration-0.8.0.md)以获取详细说明。

## Features  功能

* MCP Client and MCP Server implementations supporting:
  * Protocol [version compatibility negotiation](/specification/2024-11-05/basic/lifecycle/#initialization)
  * [Tool](/specification/2024-11-05/server/tools/) discovery, execution, list change notifications
  * [Resource](/specification/2024-11-05/server/resources/) management with URI templates
  * [Roots](/specification/2024-11-05/client/roots/) list management and notifications
  * [Prompt](/specification/2024-11-05/server/prompts/) handling and management
  * [Sampling](/specification/2024-11-05/client/sampling/) support for AI model interactions
* Multiple transport implementations:
  * Default transports (included in core `mcp` module, no external web frameworks required):
    * Stdio-based transport for process-based communication
    * Java HttpClient-based SSE client transport for HTTP SSE Client-side streaming
    * Servlet-based SSE server transport for HTTP SSE Server streaming
  * Optional Spring-based transports (convenience if using Spring Framework):
    * WebFlux SSE client and server transports for reactive HTTP streaming
    * WebMVC SSE transport for servlet-based HTTP streaming
* Supports Synchronous and Asynchronous programming paradigms
MCP 客户端和 MCP 服务器实现支持：* 协议[版本兼容性协商](/specification/2024-11-05/basic/lifecycle/#initialization)* [工具](/specification/2024-11-05/server/tools/)发现、执行、列表变更通知* [资源](/specification/2024-11-05/server/resources/)管理使用 URI 模板* [根](/specification/2024-11-05/client/roots/)列表管理和通知* [提示](/specification/2024-11-05/server/prompts/)处理和管理* [采样](/specification/2024-11-05/client/sampling/)支持 AI 模型交互* 多种传输实现：* 默认传输（包含在核心`mcp`模块中，无需外部 Web 框架）：* 基于 Stdio 的传输用于进程间通信* 基于 Java HttpClient 的 SSE 客户端传输用于 HTTP SSE 客户端流* 基于 Servlet 的 SSE 服务器传输用于 HTTP SSE 服务器流* 可选基于 Spring 的传输（如果使用 Spring 框架则方便）：* WebFlux SSE 客户端和服务器传输用于反应式 HTTP 流* WebMVC SSE 传输用于基于 Servlet 的 HTTP 流* 支持同步和异步编程范式

<Tip>
  The core `io.modelcontextprotocol.sdk:mcp` module provides default STDIO and SSE client and server transport implementations without requiring external web frameworks.
<提示> 核心模块 `io.modelcontextprotocol.sdk:mcp` 提供默认的 STDIO 和 SSE 客户端和服务器传输实现，无需使用外部 Web 框架。

  Spring-specific transports are available as optional dependencies for convenience when using the [Spring Framework](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html).
</Tip>
Spring 特定的传输作为可选依赖项提供，方便在使用 [Spring 框架](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html) 时使用。

## Architecture  ## 架构

The SDK follows a layered architecture with clear separation of concerns:
SDK 采用分层架构，关注点分离清晰：

![MCP Stack Architecture](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/mcp-stack.svg)
![MCP 堆栈架构](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/mcp-stack.svg)

* **Client/Server Layer (McpClient/McpServer)**: Both use McpSession for sync/async operations,
  with McpClient handling client-side protocol operations and McpServer managing server-side protocol operations.
* **Session Layer (McpSession)**: Manages communication patterns and state using DefaultMcpSession implementation.
* **Transport Layer (McpTransport)**: Handles JSON-RPC message serialization/deserialization via:
  * StdioTransport (stdin/stdout) in the core module
  * HTTP SSE transports in dedicated transport modules (Java HttpClient, Spring WebFlux, Spring WebMVC)
* **客户端/服务器层 (McpClient/McpServer)**: 都使用 McpSession 进行同步/异步操作，其中 McpClient 处理客户端协议操作，McpServer 管理服务器端协议操作。* **会话层 (McpSession)**: 使用 DefaultMcpSession 实现管理通信模式和状态。* **传输层 (McpTransport)**: 通过以下方式处理 JSON-RPC 消息的序列化和反序列化：* 核心模块中的 StdioTransport (stdin/stdout) * 专用传输模块中的 HTTP SSE 传输（Java HttpClient、Spring WebFlux、Spring WebMVC）

The MCP Client is a key component in the Model Context Protocol (MCP) architecture, responsible for establishing and managing connections with MCP servers.
It implements the client-side of the protocol.
MCP 客户端是模型上下文协议（MCP）架构中的关键组件，负责与 MCP 服务器建立和管理连接。它实现了协议的客户端部分。

![Java MCP Client Architecture](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/java-mcp-client-architecture.jpg)
![Java MCP 客户端架构](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/java-mcp-client-architecture.jpg)

The MCP Server is a foundational component in the Model Context Protocol (MCP) architecture that provides tools, resources, and capabilities to clients.
It implements the server-side of the protocol.
MCP 服务器是模型上下文协议（MCP）架构中的基础组件，为客户端提供工具、资源和能力。它实现了协议的服务器端部分。

![Java MCP Server Architecture](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/java-mcp-server-architecture.jpg)
![Java MCP 服务器架构](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/java-mcp-server-architecture.jpg)

Key Interactions:  关键交互：

* **Client/Server Initialization**: Transport setup, protocol compatibility check, capability negotiation, and implementation details exchange.
* **Message Flow**: JSON-RPC message handling with validation, type-safe response processing, and error handling.
* **Resource Management**: Resource discovery, URI template-based access, subscription system, and content retrieval.
* **客户端/服务器初始化**：传输设置、协议兼容性检查、能力协商和实现细节交换。* **消息流**：JSON-RPC 消息处理，包括验证、类型安全的响应处理和错误处理。* **资源管理**：资源发现、基于 URI 模板的访问、订阅系统和内容检索。

## Dependencies  ## 依赖项

Add the following Maven dependency to your project:
将以下 Maven 依赖项添加到您的项目中：

<Tabs>
  <Tab title="Maven">
    The core MCP functionality:
  核心 MCP 功能：

    ```xml
    <dependency>
        <groupId>io.modelcontextprotocol.sdk</groupId>
        <artifactId>mcp</artifactId>
    </dependency>
    ```

    The core `mcp` module already includes default STDIO and SSE transport implementations and doesn't require external web frameworks.
核心 mcp 模块已包含默认的 STDIO 和 SSE 传输实现，无需外部 Web 框架。

    If you're using the Spring Framework and want to use Spring-specific transport implementations, add one of the following optional dependencies:
如果你正在使用 Spring 框架并希望使用 Spring 特定的传输实现，请添加以下可选依赖项之一：

    ```xml
    <!-- Optional: Spring WebFlux-based SSE client and server transport -->
    <dependency>
        <groupId>io.modelcontextprotocol.sdk</groupId>
        <artifactId>mcp-spring-webflux</artifactId>
    </dependency>
```xml   io.modelcontextprotocol.sdk mcp-spring-webflux 

    <!-- Optional: Spring WebMVC-based SSE server transport -->
    <dependency>
        <groupId>io.modelcontextprotocol.sdk</groupId>
        <artifactId>mcp-spring-webmvc</artifactId>
    </dependency>
    ```
  </Tab>
 io.modelcontextprotocol.sdk mcp-spring-webmvc  ``` 

  <Tab title="Gradle">
    The core MCP functionality:
MCP 核心功能：

    ```groovy
    dependencies {
      implementation platform("io.modelcontextprotocol.sdk:mcp")
      //...
    }
    ```

    The core `mcp` module already includes default STDIO and SSE transport implementations and doesn't require external web frameworks.
核心的 `mcp` 模块已包含默认的 STDIO 和 SSE 传输实现，无需外部 Web 框架。

    If you're using the Spring Framework and want to use Spring-specific transport implementations, add one of the following optional dependencies:
如果您正在使用 Spring 框架并希望使用 Spring 特定的传输实现，请添加以下可选依赖项之一：

    ```groovy
    // Optional: Spring WebFlux-based SSE client and server transport
    dependencies {
      implementation platform("io.modelcontextprotocol.sdk:mcp-spring-webflux")
    }
```groovy // 可选：基于 Spring WebFlux 的 SSE 客户端和服务器传输依赖项 { implementation platform("io.modelcontextprotocol.sdk:mcp-spring-webflux") }

    // Optional: Spring WebMVC-based SSE server transport
    dependencies {
      implementation platform("io.modelcontextprotocol.sdk:mcp-spring-webmvc")
    }
    ```
  </Tab>
</Tabs>
// 可选：基于 Spring WebMVC 的 SSE 服务器传输依赖项 { implementation platform("io.modelcontextprotocol.sdk:mcp-spring-webmvc") } ```  

### Bill of Materials (BOM)
### 材料清单（BOM）

The Bill of Materials (BOM) declares the recommended versions of all the dependencies used by a given release.
Using the BOM from your application's build script avoids the need for you to specify and maintain the dependency versions yourself.
Instead, the version of the BOM you're using determines the utilized dependency versions.
It also ensures that you're using supported and tested versions of the dependencies by default, unless you choose to override them.
材料清单（BOM）声明了给定版本中使用的所有依赖项的推荐版本。使用您应用程序构建脚本中的 BOM 可以避免您自己指定和维护依赖项版本。相反，您使用的 BOM 版本决定了所使用的依赖项版本。它还确保您默认使用受支持和经过测试的依赖项版本，除非您选择覆盖它们。

Add the BOM to your project:
将 BOM 添加到您的项目中：

<Tabs>
  <Tab title="Maven">
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>io.modelcontextprotocol.sdk</groupId>
                <artifactId>mcp-bom</artifactId>
                <version>0.9.0</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```
  </Tab>

  <Tab title="Gradle">
    ```groovy
    dependencies {
      implementation platform("io.modelcontextprotocol.sdk:mcp-bom:0.9.0")
      //...
    }
    ```

    Gradle users can also use the Spring AI MCP BOM by leveraging Gradle (5.0+) native support for declaring dependency constraints using a Maven BOM.
    This is implemented by adding a 'platform' dependency handler method to the dependencies section of your Gradle build script.
    As shown in the snippet above this can then be followed by version-less declarations of the Starter Dependencies for the one or more spring-ai modules you wish to use, e.g. spring-ai-openai.
  </Tab>
</Tabs>
Gradle 用户还可以通过利用 Gradle（5.0+）对 Maven BOM 声明依赖约束的原生支持来使用 Spring AI MCP BOM。这是通过在 Gradle 构建脚本的依赖部分添加一个'platform'依赖处理方法来实现的。如上代码片段所示，然后可以跟随后面版本无关的 Starter Dependencies 声明，例如使用 spring-ai-openai 等一个或多个 spring-ai 模块。  

Replace the version number with the version of the BOM you want to use.
将版本号替换为您想要使用的 BOM 版本。

### Available Dependencies
### 可用依赖

The following dependencies are available and managed by the BOM:
以下依赖项可用并由 BOM 管理：

* Core Dependencies
  * `io.modelcontextprotocol.sdk:mcp` - Core MCP library providing the base functionality and APIs for Model Context Protocol implementation, including default STDIO and SSE client and server transport implementations. No external web frameworks required.
* Optional Transport Dependencies (convenience if using Spring Framework)
  * `io.modelcontextprotocol.sdk:mcp-spring-webflux` - WebFlux-based Server-Sent Events (SSE) transport implementation for reactive applications.
  * `io.modelcontextprotocol.sdk:mcp-spring-webmvc` - WebMVC-based Server-Sent Events (SSE) transport implementation for servlet-based applications.
* Testing Dependencies
  * `io.modelcontextprotocol.sdk:mcp-test` - Testing utilities and support for MCP-based applications.
* 核心依赖 * `io.modelcontextprotocol.sdk:mcp` - 提供基础功能及 API 的 MCP 核心库，包括默认的 STDIO 和 SSE 客户端和服务器传输实现。无需外部 Web 框架。* 可选传输依赖（如果使用 Spring 框架则方便）* `io.modelcontextprotocol.sdk:mcp-spring-webflux` - 基于 WebFlux 的 SSE 传输实现，适用于反应式应用程序。* `io.modelcontextprotocol.sdk:mcp-spring-webmvc` - 基于 WebMVC 的 SSE 传输实现，适用于基于 servlet 的应用程序。* 测试依赖 * `io.modelcontextprotocol.sdk:mcp-test` - 基于 MCP 应用程序的测试工具和支持。


# MCP Server
Source: https://modelcontextprotocol.io/sdk/java/mcp-server
# MCP 服务器源：https://modelcontextprotocol.io/sdk/java/mcp-server

Learn how to implement and configure a Model Context Protocol (MCP) server
学习如何实现和配置模型上下文协议（MCP）服务器

<Note>
  ### Breaking Changes in 0.8.x ⚠️
<注意> ### 0.8.x 版本的重大变更 ⚠️

  **Note:** Version 0.8.x introduces several breaking changes including a new session-based architecture.
  If you're upgrading from 0.7.0, please refer to the [Migration Guide](https://github.com/modelcontextprotocol/java-sdk/blob/main/migration-0.8.0.md) for detailed instructions.
</Note>
**注意**：0.8.x 版本引入了多个重大变更，包括新的基于会话的架构。如果您从 0.7.0 版本升级，请参阅[迁移指南](https://github.com/modelcontextprotocol/java-sdk/blob/main/migration-0.8.0.md)以获取详细说明。

## Overview  ## 概述

The MCP Server is a foundational component in the Model Context Protocol (MCP) architecture that provides tools, resources, and capabilities to clients. It implements the server-side of the protocol, responsible for:
MCP 服务器是模型上下文协议（MCP）架构中的基础组件，为客户端提供工具、资源和功能。它实现了协议的客户端，负责：

* Exposing tools that clients can discover and execute
* Managing resources with URI-based access patterns
* Providing prompt templates and handling prompt requests
* Supporting capability negotiation with clients
* Implementing server-side protocol operations
* Managing concurrent client connections
* Providing structured logging and notifications
* 暴露客户可以发现和执行的工具 * 使用基于 URI 的访问模式管理资源 * 提供快速模板并处理请求 * 支持与客户端的能力协商 * 实现服务器端协议操作 * 管理并发客户端连接 * 提供结构化日志和通知

<Tip>
  The core `io.modelcontextprotocol.sdk:mcp` module provides STDIO and SSE server transport implementations  without requiring external web frameworks.
<提示> 核心模块 `io.modelcontextprotocol.sdk:mcp` 提供了无需外部 Web 框架的 STDIO 和 SSE 服务器传输实现。

  Spring-specific transport implementations are available as an **optional** dependencies `io.modelcontextprotocol.sdk:mcp-spring-webflux`, `io.modelcontextprotocol.sdk:mcp-spring-webmvc` for [Spring Framework](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html) users.
</Tip>
Spring 特定的传输实现作为**可选**依赖项提供，`io.modelcontextprotocol.sdk:mcp-spring-webflux`，`io.modelcontextprotocol.sdk:mcp-spring-webmvc`，供[Spring 框架](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html)用户使用。

The server supports both synchronous and asynchronous APIs, allowing for flexible integration in different application contexts.
服务器支持同步和异步 API，允许在不同应用程序上下文中灵活集成。

<Tabs>
  <Tab title="Sync API">
    ```java
    // Create a server with custom configuration
    McpSyncServer syncServer = McpServer.sync(transportProvider)
        .serverInfo("my-server", "1.0.0")
        .capabilities(ServerCapabilities.builder()
            .resources(true)     // Enable resource support
            .tools(true)         // Enable tool support
            .prompts(true)       // Enable prompt support
            .logging()           // Enable logging support
            .completions()      // Enable completions support
            .build())
        .build();
  ```java // 使用自定义配置创建服务器 McpSyncServer syncServer = McpServer.sync(transportProvider) .serverInfo("my-server", "1.0.0") .capabilities(ServerCapabilities.builder() .resources(true) // 启用资源支持 .tools(true) // 启用工具支持 .prompts(true) // 启用提示支持 .logging() // 启用日志支持 .completions() // 启用补全支持 .build()) .build();

    // Register tools, resources, and prompts
    syncServer.addTool(syncToolSpecification);
    syncServer.addResource(syncResourceSpecification);
    syncServer.addPrompt(syncPromptSpecification);
// 注册工具、资源和提示 syncServer.addTool(syncToolSpecification); syncServer.addResource(syncResourceSpecification); syncServer.addPrompt(syncPromptSpecification);

    // Close the server when done
    syncServer.close();
    ```
  </Tab>
// 完成后关闭服务器 syncServer.close(); ``` 

  <Tab title="Async API">
    ```java
    // Create an async server with custom configuration
    McpAsyncServer asyncServer = McpServer.async(transportProvider)
        .serverInfo("my-server", "1.0.0")
        .capabilities(ServerCapabilities.builder()
            .resources(true)     // Enable resource support
            .tools(true)         // Enable tool support
            .prompts(true)       // Enable prompt support
            .logging()           // Enable logging support
            .build())
        .build();
 ```java // 使用自定义配置创建异步服务器 McpAsyncServer asyncServer = McpServer.async(transportProvider) .serverInfo("my-server", "1.0.0") .capabilities(ServerCapabilities.builder() .resources(true) // 启用资源支持 .tools(true) // 启用工具支持 .prompts(true) // 启用提示支持 .logging() // 启用日志支持 .build()) .build();

    // Register tools, resources, and prompts
    asyncServer.addTool(asyncToolSpecification)
        .doOnSuccess(v -> logger.info("Tool registered"))
        .subscribe();
注册工具、资源和提示 asyncServer.addTool(asyncToolSpecification) .doOnSuccess(v -> logger.info("工具已注册")) .subscribe();

    asyncServer.addResource(asyncResourceSpecification)
        .doOnSuccess(v -> logger.info("Resource registered"))
        .subscribe();
asyncServer.addResource(asyncResourceSpecification) .doOnSuccess(v -> logger.info("资源已注册")) .subscribe();

    asyncServer.addPrompt(asyncPromptSpecification)
        .doOnSuccess(v -> logger.info("Prompt registered"))
        .subscribe();
asyncServer.addPrompt(asyncPromptSpecification) .doOnSuccess(v -> logger.info("提示已注册")) .subscribe();

    // Close the server when done
    asyncServer.close()
        .doOnSuccess(v -> logger.info("Server closed"))
        .subscribe();
    ```
  </Tab>
</Tabs>
关闭服务器 asyncServer.close() .doOnSuccess(v -> logger.info("服务器已关闭")) .subscribe();

## Server Transport Providers
## 服务器传输提供商

The transport layer in the MCP SDK is responsible for handling the communication between clients and servers.
It provides different implementations to support various communication protocols and patterns.
The SDK includes several built-in transport provider implementations:
在 MCP SDK 中，传输层负责处理客户端和服务器之间的通信。它提供不同的实现来支持各种通信协议和模式。SDK 包括几个内置的传输提供者实现：

<Tabs>
  <Tab title="STDIO">
    <>
      Create in-process based transport:
  <> 基于进程内创建传输：

      ```java
      StdioServerTransportProvider transportProvider = new StdioServerTransportProvider(new ObjectMapper());
      ```

      Provides bidirectional JSON-RPC message handling over standard input/output streams with non-blocking message processing, serialization/deserialization, and graceful shutdown support.
提供基于标准输入/输出流的双向 JSON-RPC 消息处理，具有非阻塞消息处理、序列化/反序列化以及优雅关闭支持。

      Key features:  关键特性：

      <ul>
        <li>Bidirectional communication through stdin/stdout</li>
        <li>Process-based integration support</li>
        <li>Simple setup and configuration</li>
        <li>Lightweight implementation</li>
      </ul>
    </>
  </Tab>
 
通过 stdin/stdout 进行双向通信
 
基于进程的集成支持
 
简单设置和配置
 
轻量级实现
 
 

  <Tab title="SSE (WebFlux)">
    <>
      <p>Creates WebFlux-based SSE server transport.<br />Requires the <code>mcp-spring-webflux</code> dependency.</p>
 <> 
创建基于 WebFlux 的 SSE 服务器传输。
需要mcp-spring-webflux依赖。



      ```java
      @Configuration
      class McpConfig {
          @Bean
          WebFluxSseServerTransportProvider webFluxSseServerTransportProvider(ObjectMapper mapper) {
              return new WebFluxSseServerTransportProvider(mapper, "/mcp/message");
          }

          @Bean
          RouterFunction<?> mcpRouterFunction(WebFluxSseServerTransportProvider transportProvider) {
              return transportProvider.getRouterFunction();
          }
      }
      ```
@Bean RouterFunction mcpRouterFunction(WebFluxSseServerTransportProvider transportProvider) { return transportProvider.getRouterFunction(); } }

      <p>Implements the MCP HTTP with SSE transport specification, providing:</p>
实现 MCP HTTP 与 SSE 传输规范，提供：

      <ul>
        <li>Reactive HTTP streaming with WebFlux</li>
        <li>Concurrent client connections through SSE endpoints</li>
        <li>Message routing and session management</li>
        <li>Graceful shutdown capabilities</li>
      </ul>
    </>
  </Tab>
 
基于 WebFlux 的响应式 HTTP 流式传输
 
通过 SSE 端点实现并发客户端连接
 
消息路由和会话管理
 
优雅关闭功能
 
 

  <Tab title="SSE (WebMvc)">
    <>
      <p>Creates WebMvc-based SSE server transport.<br />Requires the <code>mcp-spring-webmvc</code> dependency.</p>
 <> 
创建基于 WebMvc 的 SSE 服务器传输。
需要mcp-spring-webmvc依赖。



      ```java
      @Configuration
      @EnableWebMvc
      class McpConfig {
          @Bean
          WebMvcSseServerTransportProvider webMvcSseServerTransportProvider(ObjectMapper mapper) {
              return new WebMvcSseServerTransportProvider(mapper, "/mcp/message");
          }

          @Bean
          RouterFunction<ServerResponse> mcpRouterFunction(WebMvcSseServerTransportProvider transportProvider) {
              return transportProvider.getRouterFunction();
          }
      }
      ```

      <p>Implements the MCP HTTP with SSE transport specification, providing:</p>
实现了 MCP HTTP 与 SSE 传输规范，提供：



      <ul>
        <li>Server-side event streaming</li>
        <li>Integration with Spring WebMVC</li>
        <li>Support for traditional web applications</li>
        <li>Synchronous operation handling</li>
      </ul>
    </>
  </Tab>
 
服务器端事件流
 
与 Spring WebMVC 集成
 
支持传统 Web 应用
 
同步操作处理
 
  

  <Tab title="SSE (Servlet)">
    <>
      <p>
        Creates a Servlet-based SSE server transport. It is included in the core <code>mcp</code> module.<br />
        The <code>HttpServletSseServerTransport</code> can be used with any Servlet container.<br />
        To use it with a Spring Web application, you can register it as a Servlet bean:
      </p>
 <> 
 创建基于 Servlet 的 SSE 服务器传输。它包含在核心 mcp 模块中。
 HttpServletSseServerTransport 可以与任何 Servlet 容器一起使用。
 要在 Spring Web 应用程序中使用它，您可以将其注册为 Servlet Bean：



      ```java
      @Configuration
      @EnableWebMvc
      public class McpServerConfig implements WebMvcConfigurer {

          @Bean
          public HttpServletSseServerTransportProvider servletSseServerTransportProvider() {
              return new HttpServletSseServerTransportProvider(new ObjectMapper(), "/mcp/message");
          }

          @Bean
          public ServletRegistrationBean customServletBean(HttpServletSseServerTransportProvider transportProvider) {
              return new ServletRegistrationBean(transportProvider);
          }
      }
      ```

      <p>
        Implements the MCP HTTP with SSE transport specification using the traditional Servlet API, providing:
      </p>
使用传统的 Servlet API 实现 MCP HTTP 与 SSE 传输规范，提供：



      <ul>
        <li>Asynchronous message handling using Servlet 6.0 async support</li>
        <li>Session management for multiple client connections</li>
 
使用 Servlet 6.0 异步支持进行异步消息处理
 
管理多个客户端连接的会话


        <li>
          Two types of endpoints:
两种类型的端点：


          <ul>
            <li>SSE endpoint (<code>/sse</code>) for server-to-client events</li>
            <li>Message endpoint (configurable) for client-to-server requests</li>
          </ul>
        </li>
 
SSE 端点（/sse）用于服务器到客户端的事件
 
消息端点（可配置）用于客户端到服务器的请求
 
 

        <li>Error handling and response formatting</li>
        <li>Graceful shutdown support</li>
      </ul>
    </>
  </Tab>
</Tabs>
错误处理和响应格式化
 
优雅关闭支持
    

## Server Capabilities  ## 服务器功能

The server can be configured with various capabilities:
服务器可以配置以下各种功能：

```java
var capabilities = ServerCapabilities.builder()
    .resources(false, true)  // Resource support with list changes notifications
    .tools(true)            // Tool support with list changes notifications
    .prompts(true)          // Prompt support with list changes notifications
    .logging()              // Enable logging support (enabled by default with logging level INFO)
    .build();
```
```java var capabilities = ServerCapabilities.builder() .resources(false, true) // 资源支持，带有列表变更通知 .tools(true) // 工具支持，带有列表变更通知 .prompts(true) // 提示支持，带有列表变更通知 .logging() // 启用日志支持（默认启用，日志级别为 INFO） .build(); ```

### Logging Support  ### 日志支持

The server provides structured logging capabilities that allow sending log messages to clients with different severity levels:
服务器提供结构化日志功能，允许将不同严重级别的日志消息发送到客户端：

```java
// Send a log message to clients
server.loggingNotification(LoggingMessageNotification.builder()
    .level(LoggingLevel.INFO)
    .logger("custom-logger")
    .data("Custom log message")
    .build());
```
```java // 向客户端发送日志消息 server.loggingNotification(LoggingMessageNotification.builder() .level(LoggingLevel.INFO) .logger("custom-logger") .data("Custom log message") .build()); ```

Clients can control the minimum logging level they receive through the `mcpClient.setLoggingLevel(level)` request. Messages below the set level will be filtered out.
Supported logging levels (in order of increasing severity): DEBUG (0), INFO (1), NOTICE (2), WARNING (3), ERROR (4), CRITICAL (5), ALERT (6), EMERGENCY (7)
客户端可以通过 `mcpClient.setLoggingLevel(level)` 请求控制接收到的最小日志级别。低于设置级别的消息将被过滤。支持的日志级别（按严重程度递增）：DEBUG（0）、INFO（1）、NOTICE（2）、WARNING（3）、ERROR（4）、CRITICAL（5）、ALERT（6）、EMERGENCY（7）

### Tool Specification  工具规范

The Model Context Protocol allows servers to [expose tools](/specification/2024-11-05/server/tools/) that can be invoked by language models.
The Java SDK allows implementing a Tool Specifications with their handler functions.
Tools enable AI models to perform calculations, access external APIs, query databases, and manipulate files:
模型上下文协议允许服务器[暴露工具](/specification/2024-11-05/server/tools/)，这些工具可以被语言模型调用。Java SDK 允许通过其处理函数实现工具规范。工具使 AI 模型能够执行计算、访问外部 API、查询数据库以及操作文件：

<Tabs>
  <Tab title="Sync">
    ```java
    // Sync tool specification
    var schema = """
                {
                  "type" : "object",
                  "id" : "urn:jsonschema:Operation",
                  "properties" : {
                    "operation" : {
                      "type" : "string"
                    },
                    "a" : {
                      "type" : "number"
                    },
                    "b" : {
                      "type" : "number"
                    }
                  }
                }
                """;
    var syncToolSpecification = new McpServerFeatures.SyncToolSpecification(
        new Tool("calculator", "Basic calculator", schema),
        (exchange, arguments) -> {
            // Tool implementation
            return new CallToolResult(result, false);
        }
    );
    ```
  </Tab>
  ```java // 同步工具规范 var schema = """ { "type" : "object", "id" : "urn:jsonschema:Operation", "properties" : { "operation" : { "type" : "string" }, "a" : { "type" : "number" }, "b" : { "type" : "number" } } } """; var syncToolSpecification = new McpServerFeatures.SyncToolSpecification( new Tool("calculator", "Basic calculator", schema), (exchange, arguments) -> { // 工具实现 return new CallToolResult(result, false); } ); ``` 

  <Tab title="Async">
    ```java
    // Async tool specification
    var schema = """
                {
                  "type" : "object",
                  "id" : "urn:jsonschema:Operation",
                  "properties" : {
                    "operation" : {
                      "type" : "string"
                    },
                    "a" : {
                      "type" : "number"
                    },
                    "b" : {
                      "type" : "number"
                    }
                  }
                }
                """;
    var asyncToolSpecification = new McpServerFeatures.AsyncToolSpecification(
        new Tool("calculator", "Basic calculator", schema),
        (exchange, arguments) -> {
            // Tool implementation
            return Mono.just(new CallToolResult(result, false));
        }
    );
    ```
  </Tab>
</Tabs>
 ```java // 异步工具规范 var schema = """ { "type" : "object", "id" : "urn:jsonschema:Operation", "properties" : { "operation" : { "type" : "string" }, "a" : { "type" : "number" }, "b" : { "type" : "number" } } } """; var asyncToolSpecification = new McpServerFeatures.AsyncToolSpecification( new Tool("calculator", "Basic calculator", schema), (exchange, arguments) -> { // 工具实现 return Mono.just(new CallToolResult(result, false)); } ); ```  

The Tool specification includes a Tool definition with `name`, `description`, and `parameter schema` followed by a call handler that implements the tool's logic.
The function's first argument is `McpAsyncServerExchange` for client interaction, and the second is a map of tool arguments.
工具规范包括一个带有 `name`、`description` 和 `parameter schema` 的 Tool 定义，后面跟着实现工具逻辑的调用处理程序。函数的第一个参数是 `McpAsyncServerExchange` 用于客户端交互，第二个参数是工具参数的映射。

### Resource Specification
### 资源规范

Specification of a resource with its handler function.
Resources provide context to AI models by exposing data such as: File contents, Database records, API responses, System information, Application state.
Example resource specification:
资源及其处理函数的规范。资源通过暴露数据（如：文件内容、数据库记录、API 响应、系统信息、应用程序状态）为 AI 模型提供上下文。示例资源规范：

<Tabs>
  <Tab title="Sync">
    ```java
    // Sync resource specification
    var syncResourceSpecification = new McpServerFeatures.SyncResourceSpecification(
        new Resource("custom://resource", "name", "description", "mime-type", null),
        (exchange, request) -> {
            // Resource read implementation
            return new ReadResourceResult(contents);
        }
    );
    ```
  </Tab>
  ```java // 同步资源规范 var syncResourceSpecification = new McpServerFeatures.SyncResourceSpecification( new Resource("custom://resource", "name", "description", "mime-type", null), (exchange, request) -> { // 资源读取实现 return new ReadResourceResult(contents); } ); ``` 

  <Tab title="Async">
    ```java
    // Async resource specification
    var asyncResourceSpecification = new McpServerFeatures.AsyncResourceSpecification(
        new Resource("custom://resource", "name", "description", "mime-type", null),
        (exchange, request) -> {
            // Resource read implementation
            return Mono.just(new ReadResourceResult(contents));
        }
    );
    ```
  </Tab>
</Tabs>
 ```java // 异步资源规范 var asyncResourceSpecification = new McpServerFeatures.AsyncResourceSpecification( new Resource("custom://resource", "name", "description", "mime-type", null), (exchange, request) -> { // 资源读取实现 return Mono.just(new ReadResourceResult(contents)); } ); ```  

The resource specification comprised of resource definitions and resource read handler.
The resource definition including `name`, `description`, and `MIME type`.
The first argument of the function that handles resource read requests is an `McpAsyncServerExchange` upon which the server can
interact with the connected client.
The second arguments is a `McpSchema.ReadResourceRequest`.
资源规范由资源定义和资源读取处理程序组成。资源定义包括 `名称`、`描述` 和 `MIME 类型`。处理资源读取请求的函数的第一个参数是 `McpAsyncServerExchange`，服务器可以通过它与连接的客户端交互。第二个参数是 `McpSchema.ReadResourceRequest`。

### Prompt Specification  ### 提示规范

As part of the [Prompting capabilities](/specification/2024-11-05/server/prompts/), MCP provides a standardized way for servers to expose prompt templates to clients.
The Prompt Specification is a structured template for AI model interactions that enables consistent message formatting, parameter substitution, context injection, response formatting, and instruction templating.
作为[提示功能](/specification/2024-11-05/server/prompts/)的一部分，MCP 为服务器提供了一种标准化的方式，以便向客户端公开提示模板。提示规范是 AI 模型交互的结构化模板，它能够实现一致的消息格式化、参数替换、上下文注入、响应格式化和指令模板。

<Tabs>
  <Tab title="Sync">
    ```java
    // Sync prompt specification
    var syncPromptSpecification = new McpServerFeatures.SyncPromptSpecification(
        new Prompt("greeting", "description", List.of(
            new PromptArgument("name", "description", true)
        )),
        (exchange, request) -> {
            // Prompt implementation
            return new GetPromptResult(description, messages);
        }
    );
    ```
  </Tab>
  ```java // 同步提示规范 var syncPromptSpecification = new McpServerFeatures.SyncPromptSpecification( new Prompt("greeting", "description", List.of( new PromptArgument("name", "description", true) )), (exchange, request) -> { // 提示实现 return new GetPromptResult(description, messages); } ); ``` 

  <Tab title="Async">
    ```java
    // Async prompt specification
    var asyncPromptSpecification = new McpServerFeatures.AsyncPromptSpecification(
        new Prompt("greeting", "description", List.of(
            new PromptArgument("name", "description", true)
        )),
        (exchange, request) -> {
            // Prompt implementation
            return Mono.just(new GetPromptResult(description, messages));
        }
    );
    ```
  </Tab>
</Tabs>
 ```java // 异步提示规范 var asyncPromptSpecification = new McpServerFeatures.AsyncPromptSpecification( new Prompt("greeting", "description", List.of( new PromptArgument("name", "description", true) )), (exchange, request) -> { // 提示实现 return Mono.just(new GetPromptResult(description, messages)); } ); ```  

The prompt definition includes name (identifier for the prompt), description (purpose of the prompt), and list of arguments (parameters for templating).
The handler function processes requests and returns formatted templates.
The first argument is `McpAsyncServerExchange` for client interaction, and the second argument is a `GetPromptRequest` instance.
提示定义包括名称（提示标识符）、描述（提示目的）和参数列表（模板参数）。处理函数处理请求并返回格式化模板。第一个参数是 `McpAsyncServerExchange` 用于客户端交互，第二个参数是 `GetPromptRequest` 实例。

### Completion Specification
### 完成规范

As part of the [Completion capabilities](/specification/2025-03-26/server/utilities/completion), MCP provides a provides a standardized way for servers to offer argument autocompletion suggestions for prompts and resource URIs.
作为 [完成功能](/specification/2025-03-26/server/utilities/completion) 的一部分，MCP 为服务器提供了一种标准化的方式，以便为提示和资源 URI 提供参数自动完成建议。

<Tabs>
  <Tab title="Sync">
    ```java
    // Sync completion specification
    var syncCompletionSpecification = new McpServerFeatures.SyncCompletionSpecification(
    			new McpSchema.PromptReference("code_review"), (exchange, request) -> {
  ```java // 同步完成规范 var syncCompletionSpecification = new McpServerFeatures.SyncCompletionSpecification( new McpSchema.PromptReference("code_review"), (exchange, request) -> {

            // completion implementation ...

            return new McpSchema.CompleteResult(
                new CompleteResult.CompleteCompletion(
                  List.of("python", "pytorch", "pyside"), 
                  10, // total
                  false // hasMore
                ));
          }
    );
返回一个新的 McpSchema.CompleteResult 对象（new CompleteResult.CompleteCompletion( List.of("python", "pytorch", "pyside"), 10, // total false // hasMore )); } );

    // Create a sync server with completion capabilities
    var mcpServer = McpServer.sync(mcpServerTransportProvider)
      .capabilities(ServerCapabilities.builder()
        .completions() // enable completions support
          // ...
        .build())
      // ...
      .completions(new McpServerFeatures.SyncCompletionSpecification( // register completion specification
          new McpSchema.PromptReference("code_review"), syncCompletionSpecification))
      .build();
// 创建一个具有补全功能的同步服务器 var mcpServer = McpServer.sync(mcpServerTransportProvider) .capabilities(ServerCapabilities.builder() .completions() // 启用补全支持 // ... .build()) // ... .completions(new McpServerFeatures.SyncCompletionSpecification( // 注册补全规范 new McpSchema.PromptReference("code_review"), syncCompletionSpecification)) .build();

    ```
  </Tab>

  <Tab title="Async">
    ```java
    // Async prompt specification
    var asyncCompletionSpecification = new McpServerFeatures.AsyncCompletionSpecification(
    			new McpSchema.PromptReference("code_review"), (exchange, request) -> {
异步提示规范 `var asyncCompletionSpecification = new McpServerFeatures.AsyncCompletionSpecification( new McpSchema.PromptReference("code_review"), (exchange, request) -> {`

            // completion implementation ...
// 完成实现 ...

            return Mono.just(new McpSchema.CompleteResult(
                new CompleteResult.CompleteCompletion(
                  List.of("python", "pytorch", "pyside"), 
                  10, // total
                  false // hasMore
                )));
          }
    );
return Mono.just(new McpSchema.CompleteResult( new CompleteResult.CompleteCompletion( List.of("python", "pytorch", "pyside"), 10, // 总计 false // 是否还有更多))); }

    // Create a async server with completion capabilities
    var mcpServer = McpServer.async(mcpServerTransportProvider)
      .capabilities(ServerCapabilities.builder()
        .completions() // enable completions support
          // ...
        .build())
      // ...
      .completions(new McpServerFeatures.AsyncCompletionSpecification( // register completion specification
          new McpSchema.PromptReference("code_review"), asyncCompletionSpecification))
      .build();
// 创建具有完成功能的异步服务器 var mcpServer = McpServer.async(mcpServerTransportProvider) .capabilities(ServerCapabilities.builder() .completions() // 启用完成支持 // ... .build()) // ... .completions(new McpServerFeatures.AsyncCompletionSpecification( // 注册完成规范 new McpSchema.PromptReference("code_review"), asyncCompletionSpecification)) .build();

    ```
  </Tab>
</Tabs>

The `McpSchema.CompletionReference` definition defines the type (`PromptRefernce` or `ResourceRefernce`) and the identifier for the completion specification (e.g handler).
The handler function processes requests and returns the complition response.
The first argument is `McpAsyncServerExchange` for client interaction, and the second argument is a `CompleteRequest` instance.
`McpSchema.CompletionReference` 定义了完成规范的类型（`PromptRefernce` 或 `ResourceRefernce`）及其标识符（例如处理器）。处理器函数处理请求并返回完成响应。第一个参数是用于客户端交互的 `McpAsyncServerExchange`，第二个参数是一个 `CompleteRequest` 实例。

Check the [using completion](/sdk/java/mcp-client#using-completion) to learn how to use the completion capabilities on the client side.
查看使用完成[使用完成](/sdk/java/mcp-client#using-completion)以了解如何在客户端使用完成功能。

### Using Sampling from a Server
### 从服务器使用采样

To use [Sampling capabilities](/specification/2024-11-05/client/sampling/), connect to a client that supports sampling.
No special server configuration is needed, but verify client sampling support before making requests.
Learn about [client sampling support](./mcp-client#sampling-support).
使用[采样功能](/specification/2024-11-05/client/sampling/)，请连接到支持采样的客户端。无需特殊服务器配置，但在发送请求之前请验证客户端是否支持采样。了解[客户端采样支持](./mcp-client#sampling-support)。

Once connected to a compatible client, the server can request language model generations:
连接到兼容客户端后，服务器可以请求语言模型生成：

<Tabs>
  <Tab title="Sync API">
    ```java
    // Create a server
    McpSyncServer server = McpServer.sync(transportProvider)
        .serverInfo("my-server", "1.0.0")
        .build();
  ```java // 创建服务器 McpSyncServer server = McpServer.sync(transportProvider) .serverInfo("my-server", "1.0.0") .build();

    // Define a tool that uses sampling
    var calculatorTool = new McpServerFeatures.SyncToolSpecification(
        new Tool("ai-calculator", "Performs calculations using AI", schema),
        (exchange, arguments) -> {
            // Check if client supports sampling
            if (exchange.getClientCapabilities().sampling() == null) {
                return new CallToolResult("Client does not support AI capabilities", false);
            }
// 定义使用采样的工具 var calculatorTool = new McpServerFeatures.SyncToolSpecification( new Tool("ai-calculator", "使用 AI 进行计算", schema), (exchange, arguments) -> { // 检查客户端是否支持采样 if (exchange.getClientCapabilities().sampling() == null) { return new CallToolResult("客户端不支持 AI 功能", false); }

            // Create a sampling request
            McpSchema.CreateMessageRequest request = McpSchema.CreateMessageRequest.builder()
                .messages(List.of(new McpSchema.SamplingMessage(McpSchema.Role.USER,
                    new McpSchema.TextContent("Calculate: " + arguments.get("expression")))
                .modelPreferences(McpSchema.ModelPreferences.builder()
                    .hints(List.of(
                        McpSchema.ModelHint.of("claude-3-sonnet"),
                        McpSchema.ModelHint.of("claude")
                    ))
                    .intelligencePriority(0.8)  // Prioritize intelligence
                    .speedPriority(0.5)         // Moderate speed importance
                    .build())
                .systemPrompt("You are a helpful calculator assistant. Provide only the numerical answer.")
                .maxTokens(100)
                .build();
// 创建采样请求 McpSchema.CreateMessageRequest request = McpSchema.CreateMessageRequest.builder() .messages(List.of(new McpSchema.SamplingMessage(McpSchema.Role.USER, new McpSchema.TextContent("计算: " + arguments.get("expression"))) .modelPreferences(McpSchema.ModelPreferences.builder() .hints(List.of( McpSchema.ModelHint.of("claude-3-sonnet"), McpSchema.ModelHint.of("claude") )) .intelligencePriority(0.8) // 优先考虑智能 .speedPriority(0.5) // 适度考虑速度 .build()) .systemPrompt("你是一个有用的计算助手。只提供数值答案。") .maxTokens(100) .build();

            // Request sampling from the client
            McpSchema.CreateMessageResult result = exchange.createMessage(request);
// 从客户端请求采样 McpSchema.CreateMessageResult result = exchange.createMessage(request);

            // Process the result
            String answer = result.content().text();
            return new CallToolResult(answer, false);
        }
    );
// 处理结果 String answer = result.content().text(); return new CallToolResult(answer, false); } );

    // Add the tool to the server
    server.addTool(calculatorTool);
    ```
  </Tab>
// 将工具添加到服务器 server.addTool(calculatorTool); ``` 

  <Tab title="Async API">
    ```java
    // Create a server
    McpAsyncServer server = McpServer.async(transportProvider)
        .serverInfo("my-server", "1.0.0")
        .build();
 ```java // 创建服务器 McpAsyncServer server = McpServer.async(transportProvider) .serverInfo("my-server", "1.0.0") .build();

    // Define a tool that uses sampling
    var calculatorTool = new McpServerFeatures.AsyncToolSpecification(
        new Tool("ai-calculator", "Performs calculations using AI", schema),
        (exchange, arguments) -> {
            // Check if client supports sampling
            if (exchange.getClientCapabilities().sampling() == null) {
                return Mono.just(new CallToolResult("Client does not support AI capabilities", false));
            }
// 定义一个使用采样的工具 var calculatorTool = new McpServerFeatures.AsyncToolSpecification( new Tool("ai-calculator", "使用 AI 进行计算", schema), (exchange, arguments) -> { // 检查客户端是否支持采样 if (exchange.getClientCapabilities().sampling() == null) { return Mono.just(new CallToolResult("客户端不支持 AI 功能", false)); }

            // Create a sampling request
            McpSchema.CreateMessageRequest request = McpSchema.CreateMessageRequest.builder()
                .content(new McpSchema.TextContent("Calculate: " + arguments.get("expression")))
                .modelPreferences(McpSchema.ModelPreferences.builder()
                    .hints(List.of(
                        McpSchema.ModelHint.of("claude-3-sonnet"),
                        McpSchema.ModelHint.of("claude")
                    ))
                    .intelligencePriority(0.8)  // Prioritize intelligence
                    .speedPriority(0.5)         // Moderate speed importance
                    .build())
                .systemPrompt("You are a helpful calculator assistant. Provide only the numerical answer.")
                .maxTokens(100)
                .build();
// 创建采样请求 McpSchema.CreateMessageRequest request = McpSchema.CreateMessageRequest.builder() .content(new McpSchema.TextContent("计算: " + arguments.get("expression"))) .modelPreferences(McpSchema.ModelPreferences.builder() .hints(List.of( McpSchema.ModelHint.of("claude-3-sonnet"), McpSchema.ModelHint.of("claude") )) .intelligencePriority(0.8) // 优先考虑智能 .speedPriority(0.5) // 调整速度重要性 .build()) .systemPrompt("你是一个有用的计算助手。只提供数值答案。") .maxTokens(100) .build();

            // Request sampling from the client
            return exchange.createMessage(request)
                .map(result -> {
                    // Process the result
                    String answer = result.content().text();
                    return new CallToolResult(answer, false);
                });
        }
    );
// 从客户端请求采样返回 exchange.createMessage(request) .map(result -> { // 处理结果 String answer = result.content().text(); return new CallToolResult(answer, false); }); }

    // Add the tool to the server
    server.addTool(calculatorTool)
        .subscribe();
    ```
  </Tab>
</Tabs>
// 将工具添加到服务器 server.addTool(calculatorTool) .subscribe(); ```  

The `CreateMessageRequest` object allows you to specify: `Content` - the input text or image for the model,
`Model Preferences` - hints and priorities for model selection, `System Prompt` - instructions for the model's behavior and
`Max Tokens` - maximum length of the generated response.
`CreateMessageRequest` 对象允许您指定：`Content` - 模型的输入文本或图像，`Model Preferences` - 模型选择的提示和优先级，`System Prompt` - 模型的行为说明，以及 `Max Tokens` - 生成响应的最大长度。

### Logging Support  ### 日志支持

The server provides structured logging capabilities that allow sending log messages to clients with different severity levels. The
log notifications can only be sent from within an existing client session, such as tools, resources, and prompts calls.
服务器提供结构化日志功能，允许将不同严重级别的日志消息发送到客户端。日志通知只能从现有的客户端会话中发送，例如工具、资源和提示调用。

For example, we can send a log message from within a tool handler function.
On the client side, you can register a logging consumer to receive log messages from the server and set the minimum logging level to filter messages.
例如，我们可以在工具处理函数内部发送日志消息。在客户端，您可以注册一个日志消费者以接收来自服务器的日志消息，并设置最小日志级别以过滤消息。

```java
var mcpClient = McpClient.sync(transport)
        .loggingConsumer(notification -> {
            System.out.println("Received log message: " + notification.data());
        })
        .build();

mcpClient.initialize();

mcpClient.setLoggingLevel(McpSchema.LoggingLevel.INFO);

// Call the tool that sends logging notifications
CallToolResult result = mcpClient.callTool(new McpSchema.CallToolRequest("logging-test", Map.of()));
```
// 调用发送日志通知的工具 CallToolResult result = mcpClient.callTool(new McpSchema.CallToolRequest("logging-test", Map.of())); ```

The server can send log messages using the `McpAsyncServerExchange`/`McpSyncServerExchange` object in the tool/resource/prompt handler function:
服务器可以使用工具/资源/提示处理函数中的 `McpAsyncServerExchange`/`McpSyncServerExchange` 对象发送日志消息：

```java
var tool = new McpServerFeatures.AsyncToolSpecification(
    new McpSchema.Tool("logging-test", "Test logging notifications", emptyJsonSchema),
    (exchange, request) -> {  

      exchange.loggingNotification( // Use the exchange to send log messages
          McpSchema.LoggingMessageNotification.builder()
            .level(McpSchema.LoggingLevel.DEBUG)
            .logger("test-logger")
            .data("Debug message")
            .build())
        .block();
exchange.loggingNotification( // 使用 exchange 发送日志消息 McpSchema.LoggingMessageNotification.builder() .level(McpSchema.LoggingLevel.DEBUG) .logger("test-logger") .data("Debug message") .build()) .block();

      return Mono.just(new CallToolResult("Logging test completed", false));
    });

var mcpServer = McpServer.async(mcpServerTransportProvider)
  .serverInfo("test-server", "1.0.0")
  .capabilities(
    ServerCapabilities.builder()
      .logging() // Enable logging support
      .tools(true)
      .build())
  .tools(tool)
  .build();
```
var mcpServer = McpServer.async(mcpServerTransportProvider) .serverInfo("test-server", "1.0.0") .capabilities( ServerCapabilities.builder() .logging() // 启用日志支持 .tools(true) .build()) .tools(tool) .build(); ```

Clients can control the minimum logging level they receive through the `mcpClient.setLoggingLevel(level)` request. Messages below the set level will be filtered out.
Supported logging levels (in order of increasing severity): DEBUG (0), INFO (1), NOTICE (2), WARNING (3), ERROR (4), CRITICAL (5), ALERT (6), EMERGENCY (7)
客户端可以通过 `mcpClient.setLoggingLevel(level)` 请求控制他们接收到的最小日志级别。低于设置级别的消息将被过滤。支持的日志级别（按严重程度递增排序）：DEBUG（0）、INFO（1）、NOTICE（2）、WARNING（3）、ERROR（4）、CRITICAL（5）、ALERT（6）、EMERGENCY（7）

## Error Handling  错误处理

The SDK provides comprehensive error handling through the McpError class, covering protocol compatibility, transport communication, JSON-RPC messaging, tool execution, resource management, prompt handling, timeouts, and connection issues. This unified error handling approach ensures consistent and reliable error management across both synchronous and asynchronous operations.
SDK 通过 McpError 类提供全面的错误处理，涵盖协议兼容性、传输通信、JSON-RPC 消息、工具执行、资源管理、提示处理、超时和连接问题。这种统一的错误处理方法确保了同步和异步操作中的一致和可靠的错误管理。


# Architecture
Source: https://modelcontextprotocol.io/specification/2024-11-05/architecture/index
# 架构来源：https://modelcontextprotocol.io/specification/2024-11-05/architecture/index



The Model Context Protocol (MCP) follows a client-host-server architecture where each
host can run multiple client instances. This architecture enables users to integrate AI
capabilities across applications while maintaining clear security boundaries and
isolating concerns. Built on JSON-RPC, MCP provides a stateful session protocol focused
on context exchange and sampling coordination between clients and servers.
模型上下文协议（MCP）遵循客户端-主机-服务器架构，每个主机可以运行多个客户端实例。这种架构使用户能够在保持清晰的边界和隔离关注点的同时，将 AI 能力集成到应用程序中。基于 JSON-RPC，MCP 提供了一种面向上下文交换和客户端与服务器之间采样协调的状态会话协议。

## Core Components  核心组件

```mermaid
graph LR
    subgraph "Application Host Process"
        H[Host]
        C1[Client 1]
        C2[Client 2]
        C3[Client 3]
        H --> C1
        H --> C2
        H --> C3
    end
```mermaid graph LR subgraph "应用主机进程" H[主机] C1[客户端 1] C2[客户端 2] C3[客户端 3] H --> C1 H --> C2 H --> C3 end

    subgraph "Local machine"
        S1[Server 1<br>Files & Git]
        S2[Server 2<br>Database]
        R1[("Local<br>Resource A")]
        R2[("Local<br>Resource B")]
subgraph "本地机器" S1[服务器 1
文件 & Git] S2[服务器 2
数据库] R1[("本地
资源 A")] R2[("本地
资源 B")]

        C1 --> S1
        C2 --> S2
        S1 <--> R1
        S2 <--> R2
    end

    subgraph "Internet"
        S3[Server 3<br>External APIs]
        R3[("Remote<br>Resource C")]
subgraph "互联网" S3[服务器 3
外部 API] R3[("远程
资源 C")]

        C3 --> S3
        S3 <--> R3
    end
```
C3 --> S3 S3 <--> R3 结束 ```

### Host  ### 主机

The host process acts as the container and coordinator:
主进程作为容器和协调者：

* Creates and manages multiple client instances
* Controls client connection permissions and lifecycle
* Enforces security policies and consent requirements
* Handles user authorization decisions
* Coordinates AI/LLM integration and sampling
* Manages context aggregation across clients
* 创建和管理多个客户端实例 * 控制客户端连接权限和生命周期 * 强制执行安全策略和同意要求 * 处理用户授权决策 * 协调 AI/LLM 集成和采样 * 管理跨客户端的上下文聚合

### Clients  ### 客户端

Each client is created by the host and maintains an isolated server connection:
每个客户端由主机创建并维护一个独立的服务器连接：

* Establishes one stateful session per server
* Handles protocol negotiation and capability exchange
* Routes protocol messages bidirectionally
* Manages subscriptions and notifications
* Maintains security boundaries between servers
* 为每个服务器建立一个有状态的会话 * 处理协议协商和能力交换 * 双向路由协议消息 * 管理订阅和通知 * 维护服务器之间的安全边界

A host application creates and manages multiple clients, with each client having a 1:1
relationship with a particular server.
主应用程序创建并管理多个客户端，每个客户端与特定的服务器保持一对一的关系。

### Servers  ### 服务器

Servers provide specialized context and capabilities:
服务器提供专业上下文和功能：

* Expose resources, tools and prompts via MCP primitives
* Operate independently with focused responsibilities
* Request sampling through client interfaces
* Must respect security constraints
* Can be local processes or remote services
* 通过 MCP 原语公开资源、工具和提示 * 独立运行，具有明确的职责 * 通过客户端接口请求采样 * 必须遵守安全约束 * 可以为本地进程或远程服务

## Design Principles  ## 设计原则

MCP is built on several key design principles that inform its architecture and
implementation:
MCP 构建在多个关键设计原则之上，这些原则指导了其架构和实现：

1. **Servers should be extremely easy to build**
1. **服务器应极其易于构建**

   * Host applications handle complex orchestration responsibilities
   * Servers focus on specific, well-defined capabilities
   * Simple interfaces minimize implementation overhead
   * Clear separation enables maintainable code
* 宿主应用处理复杂的编排任务 * 服务器专注于特定、定义明确的职能 * 简单的接口最小化实现开销 * 清晰的分离使代码易于维护

2. **Servers should be highly composable**
2. **服务器应高度可组合**

   * Each server provides focused functionality in isolation
   * Multiple servers can be combined seamlessly
   * Shared protocol enables interoperability
   * Modular design supports extensibility
每个服务器都提供独立的专注功能 * 多个服务器可以无缝结合 * 共享协议实现互操作性 * 模块化设计支持可扩展性

3. **Servers should not be able to read the whole conversation, nor "see into" other
   servers**
3. **服务器不应能够读取整个对话，也不应“窥视”其他服务器**

   * Servers receive only necessary contextual information
   * Full conversation history stays with the host
   * Each server connection maintains isolation
   * Cross-server interactions are controlled by the host
   * Host process enforces security boundaries
服务器仅接收必要上下文信息 * 完整对话历史保留在主机端 * 每个服务器连接保持隔离 * 服务器间交互由主机控制 * 主机进程强制执行安全边界

4. **Features can be added to servers and clients progressively**
   * Core protocol provides minimal required functionality
   * Additional capabilities can be negotiated as needed
   * Servers and clients evolve independently
   * Protocol designed for future extensibility
   * Backwards compatibility is maintained
4. **功能可以逐步添加到服务器和客户端** * 核心协议提供最小必需的功能 * 根据需要协商附加功能 * 服务器和客户端独立发展 * 协议设计用于未来扩展 * 保持向后兼容性

## Message Types  ## 消息类型

MCP defines three core message types based on
[JSON-RPC 2.0](https://www.jsonrpc.org/specification):
MCP 定义了三种基于[JSON-RPC 2.0](https://www.jsonrpc.org/specification)的核心消息类型：

* **Requests**: Bidirectional messages with method and parameters expecting a response
* **Responses**: Successful results or errors matching specific request IDs
* **Notifications**: One-way messages requiring no response
* **请求**：具有方法和参数的双向消息，期望得到响应 * **响应**：匹配特定请求 ID 的成功结果或错误 * **通知**：不需要响应的单向消息

Each message type follows the JSON-RPC 2.0 specification for structure and delivery
semantics.
每种消息类型都遵循 JSON-RPC 2.0 规范的结构和交付语义。

## Capability Negotiation
## 能力协商

The Model Context Protocol uses a capability-based negotiation system where clients and
servers explicitly declare their supported features during initialization. Capabilities
determine which protocol features and primitives are available during a session.
模型上下文协议使用基于能力协商的系统，客户端和服务器在初始化期间明确声明它们支持的功能。能力决定了会话期间可用的协议功能和原语。

* Servers declare capabilities like resource subscriptions, tool support, and prompt
  templates
* Clients declare capabilities like sampling support and notification handling
* Both parties must respect declared capabilities throughout the session
* Additional capabilities can be negotiated through extensions to the protocol
* 服务器声明的能力包括资源订阅、工具支持和提示模板 * 客户端声明的能力包括采样支持和通知处理 * 双方必须在整个会话中尊重声明的能力 * 可以通过协议的扩展协商额外的能力

```mermaid
sequenceDiagram
    participant Host
    participant Client
    participant Server
```mermaid 序列图参与者 主机 参与者 客户端 参与者 服务器

    Host->>+Client: Initialize client
    Client->>+Server: Initialize session with capabilities
    Server-->>Client: Respond with supported capabilities
主机->>+客户端：初始化客户端 客户端->>+服务器：初始化会话并协商功能 服务器-->>客户端：响应支持的功能

    Note over Host,Server: Active Session with Negotiated Features
注释 主机,服务器：已协商功能的活跃会话

    loop Client Requests
        Host->>Client: User- or model-initiated action
        Client->>Server: Request (tools/resources)
        Server-->>Client: Response
        Client-->>Host: Update UI or respond to model
    end
循环 客户端请求 主机->>客户端：用户或模型触发的动作 客户端->>服务器：请求（工具/资源） 服务器-->>客户端：响应 客户端-->>主机：更新 UI 或响应模型结束

    loop Server Requests
        Server->>Client: Request (sampling)
        Client->>Host: Forward to AI
        Host-->>Client: AI response
        Client-->>Server: Response
    end
循环服务器请求 服务器->>客户端：请求（采样） 客户端->>主机：转发给 AI 主机-->>客户端：AI 响应 客户端->>服务器：响应结束

    loop Notifications
        Server--)Client: Resource updates
        Client--)Server: Status changes
    end
循环通知 服务器--)客户端：资源更新 服务器--)服务器：状态变更结束

    Host->>Client: Terminate
    Client->>-Server: End session
    deactivate Server
```
主机->>客户端：终止 客户端->>-服务器：结束会话，停用服务器

Each capability unlocks specific protocol features for use during the session. For
example:
每个功能解锁特定协议功能，以便在会话期间使用。例如：

* Implemented [server features](/specification/2024-11-05/server) must be
  advertised in the server's capabilities
* Emitting resource subscription notifications requires the server to declare
  subscription support
* Tool invocation requires the server to declare tool capabilities
* [Sampling](/specification/2024-11-05/client) requires the client to
  declare support in its capabilities
* 实现的 [服务器功能](/specification/2024-11-05/server) 必须在服务器的能力中宣传 * 发出资源订阅通知需要服务器声明支持订阅 * 工具调用需要服务器声明工具能力 * [采样](/specification/2024-11-05/client) 需要客户端在其能力中声明支持

This capability negotiation ensures clients and servers have a clear understanding of
supported functionality while maintaining protocol extensibility.
这种能力协商确保客户端和服务器对支持的功能有清晰的理解，同时保持协议的可扩展性。


# Overview
Source: https://modelcontextprotocol.io/specification/2024-11-05/basic/index
# 概述 来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/index



<Info>**Protocol Revision**: 2024-11-05</Info>
<信息>**协议版本**: 2024-11-05

All messages between MCP clients and servers **MUST** follow the
[JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines
three fundamental types of messages:
所有 MCP 客户端和服务器之间的消息**必须**遵循[JSON-RPC 2.0](https://www.jsonrpc.org/specification)规范。该协议定义了三种基本的消息类型：

| Type            | Description                            | Requirements                           |
| --------------- | -------------------------------------- | -------------------------------------- |
| `Requests`      | Messages sent to initiate an operation | Must include unique ID and method name |
| `Responses`     | Messages sent in reply to requests     | Must include same ID as request        |
| `Notifications` | One-way messages with no reply         | Must not include an ID                 |
类型 | 描述 | 要求 | | --------------- | -------------------------------------- | -------------------------------------- | | `Requests` | 发起操作的请求消息 | 必须包含唯一的 ID 和方法名称 | | `Responses` | 作为请求回复的消息 | 必须包含与请求相同的 ID | | `Notifications` | 无回复的单向消息 | 必须不包含 ID |

**Responses** are further sub-categorized as either **successful results** or **errors**.
Results can follow any JSON object structure, while errors must include an error code and
message at minimum.
**响应**进一步细分为**成功结果**或**错误**。结果可以遵循任何 JSON 对象结构，而错误至少必须包含错误代码和消息。

## Protocol Layers  ## 协议层

The Model Context Protocol consists of several key components that work together:
模型上下文协议由几个关键组件组成，它们协同工作：

* **Base Protocol**: Core JSON-RPC message types
* **Lifecycle Management**: Connection initialization, capability negotiation, and
  session control
* **Server Features**: Resources, prompts, and tools exposed by servers
* **Client Features**: Sampling and root directory lists provided by clients
* **Utilities**: Cross-cutting concerns like logging and argument completion
* **基础协议**：核心 JSON-RPC 消息类型 * **生命周期管理**：连接初始化、能力协商和会话控制 * **服务器功能**：服务器提供的资源、提示和工具 * **客户端功能**：客户端提供的采样和根目录列表 * **实用工具**：跨切面关注点，如日志记录和参数完成

All implementations **MUST** support the base protocol and lifecycle management
components. Other components **MAY** be implemented based on the specific needs of the
application.
所有实现都必须支持基础协议和生命周期管理组件。其他组件可根据应用程序的具体需求进行实现。

These protocol layers establish clear separation of concerns while enabling rich
interactions between clients and servers. The modular design allows implementations to
support exactly the features they need.
这些协议层建立了清晰的关注点分离，同时使客户端和服务器之间能够进行丰富的交互。模块化设计允许实现支持它们需要的精确功能。

See the following pages for more details on the different components:
请参阅以下页面以获取有关不同组件的更多详细信息：

<CardGroup cols={3}>
  <Card title="Lifecycle" icon="arrows-rotate" href="/specification/2024-11-05/basic/lifecycle" />
 

  <Card title="Resources" icon="file-lines" href="/specification/2024-11-05/server/resources" />


  <Card title="Prompts" icon="message" href="/specification/2024-11-05/server/prompts" />


  <Card title="Tools" icon="wrench" href="/specification/2024-11-05/server/tools" />


  <Card title="Logging" icon="rectangle-list" href="/specification/2024-11-05/server/utilities/logging" />


  <Card title="Sampling" icon="code" href="/specification/2024-11-05/client/sampling" />
</CardGroup>


## Auth  ## 认证

Authentication and authorization are not currently part of the core MCP specification,
but we are considering ways to introduce them in future. Join us in
[GitHub Discussions](https://github.com/modelcontextprotocol/specification/discussions)
to help shape the future of the protocol!
认证和授权目前不是核心 MCP 规范的一部分，但我们正在考虑在未来引入它们。加入我们，在[GitHub 讨论](https://github.com/modelcontextprotocol/specification/discussions)中帮助塑造协议的未来！

Clients and servers **MAY** negotiate their own custom authentication and authorization
strategies.
客户端和服务器**可以**协商他们自己的自定义认证和授权策略。

## Schema  ## 架构

The full specification of the protocol is defined as a
[TypeScript schema](http://github.com/modelcontextprotocol/specification/tree/main/schema/2024-11-05/schema.ts).
This is the source of truth for all protocol messages and structures.
协议的完整规范定义为[TypeScript 架构](http://github.com/modelcontextprotocol/specification/tree/main/schema/2024-11-05/schema.ts)。这是所有协议消息和结构的真实来源。

There is also a
[JSON Schema](http://github.com/modelcontextprotocol/specification/tree/main/schema/2024-11-05/schema.json),
which is automatically generated from the TypeScript source of truth, for use with
various automated tooling.
也有一个[JSON Schema](http://github.com/modelcontextprotocol/specification/tree/main/schema/2024-11-05/schema.json)，该 Schema 从 TypeScript 源代码自动生成，用于与各种自动化工具配合使用。


# Lifecycle
Source: https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle
# 生命周期来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle



<Info>**Protocol Revision**: 2024-11-05</Info>
<信息>**协议版本**：2024-11-05

The Model Context Protocol (MCP) defines a rigorous lifecycle for client-server
connections that ensures proper capability negotiation and state management.
模型上下文协议（MCP）定义了客户端-服务器连接的严格生命周期，确保适当的协商能力和状态管理。

1. **Initialization**: Capability negotiation and protocol version agreement
2. **Operation**: Normal protocol communication
3. **Shutdown**: Graceful termination of the connection
1. **初始化**：能力协商和协议版本协商 2. **操作**：正常协议通信 3. **关闭**：连接优雅终止

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client,Server: Initialization Phase
    activate Client
    Client->>+Server: initialize request
    Server-->>Client: initialize response
    Client--)Server: initialized notification
注意：客户端、服务器：初始化阶段激活客户端 客户端->>+服务器：初始化请求 服务器-->>客户端：初始化响应 服务器--)客户端：初始化通知

    Note over Client,Server: Operation Phase
    rect rgb(200, 220, 250)
        note over Client,Server: Normal protocol operations
    end
注意：客户端、服务器：操作阶段 矩形 rgb(200, 220, 250) 注意：客户端、服务器：正常协议操作结束

    Note over Client,Server: Shutdown
    Client--)-Server: Disconnect
    deactivate Server
    Note over Client,Server: Connection closed
```
注意：客户端、服务器：关闭 客户端--)-服务器：断开连接 激活服务器 注意：客户端、服务器：连接关闭 ```

## Lifecycle Phases  生命周期阶段

### Initialization  初始化

The initialization phase **MUST** be the first interaction between client and server.
During this phase, the client and server:
初始化阶段 **必须** 是客户端和服务器之间的第一次交互。在此阶段，客户端和服务器：

* Establish protocol version compatibility
* Exchange and negotiate capabilities
* Share implementation details
* 建立协议版本兼容性 * 交换和协商能力 * 分享实现细节

The client **MUST** initiate this phase by sending an `initialize` request containing:
客户端 **必须** 通过发送包含以下内容的 `initialize` 请求来启动此阶段：

* Protocol version supported
* Client capabilities
* Client implementation information
* 支持的协议版本 * 客户端能力 * 客户端实现信息

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "roots": {
        "listChanged": true
      },
      "sampling": {}
    },
    "clientInfo": {
      "name": "ExampleClient",
      "version": "1.0.0"
    }
  }
}
```

The server **MUST** respond with its own capabilities and information:
服务器**必须**响应其自身的功能和信息：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "logging": {},
      "prompts": {
        "listChanged": true
      },
      "resources": {
        "subscribe": true,
        "listChanged": true
      },
      "tools": {
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "ExampleServer",
      "version": "1.0.0"
    }
  }
}
```

After successful initialization, the client **MUST** send an `initialized` notification
to indicate it is ready to begin normal operations:
初始化成功后，客户端**必须**发送一个`initialized`通知，以表明它已准备好开始正常操作：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

* The client **SHOULD NOT** send requests other than
  [pings](/specification/2024-11-05/basic/utilities/ping) before the server
  has responded to the `initialize` request.
* The server **SHOULD NOT** send requests other than
  [pings](/specification/2024-11-05/basic/utilities/ping) and
  [logging](/specification/2024-11-05/server/utilities/logging) before
  receiving the `initialized` notification.
* 客户端 **不应** 在服务器对 `initialize` 请求做出响应之前发送除 [ping](/specification/2024-11-05/basic/utilities/ping) 之外的其他请求。 * 服务器 **不应** 在收到 `initialized` 通知之前发送除 [ping](/specification/2024-11-05/basic/utilities/ping) 和 [日志记录](/specification/2024-11-05/server/utilities/logging) 之外的其他请求。

#### Version Negotiation  #### 版本协商

In the `initialize` request, the client **MUST** send a protocol version it supports.
This **SHOULD** be the *latest* version supported by the client.
在 `initialize` 请求中，客户端 **必须** 发送它支持的协议版本。这 **应该** 是客户端支持的 *最新* 版本。

If the server supports the requested protocol version, it **MUST** respond with the same
version. Otherwise, the server **MUST** respond with another protocol version it
supports. This **SHOULD** be the *latest* version supported by the server.
如果服务器支持请求的协议版本，它**必须**以相同的版本响应。否则，服务器**必须**以它支持的另一个协议版本响应。这**应该**是服务器支持的*最新*版本。

If the client does not support the version in the server's response, it **SHOULD**
disconnect.
如果客户端不支持服务器响应中的版本，它**应该**断开连接。

#### Capability Negotiation
#### 能力协商

Client and server capabilities establish which optional protocol features will be
available during the session.
客户端和服务器的能力确定在会话期间将可用哪些可选协议功能。

Key capabilities include:
核心功能包括：

| Category | Capability     | Description                                                                         |
| -------- | -------------- | ----------------------------------------------------------------------------------- |
| Client   | `roots`        | Ability to provide filesystem [roots](/specification/2024-11-05/client/roots)       |
| Client   | `sampling`     | Support for LLM [sampling](/specification/2024-11-05/client/sampling) requests      |
| Client   | `experimental` | Describes support for non-standard experimental features                            |
| Server   | `prompts`      | Offers [prompt templates](/specification/2024-11-05/server/prompts)                 |
| Server   | `resources`    | Provides readable [resources](/specification/2024-11-05/server/resources)           |
| Server   | `tools`        | Exposes callable [tools](/specification/2024-11-05/server/tools)                    |
| Server   | `logging`      | Emits structured [log messages](/specification/2024-11-05/server/utilities/logging) |
| Server   | `experimental` | Describes support for non-standard experimental features                            |
| Category | Capability | Description | | -------- | -------------- | ----------------------------------------------------------------------------------- | | Client | `roots` | 能够提供文件系统 [roots](/specification/2024-11-05/client/roots) | | Client | `sampling` | 支持 LLM [sampling](/specification/2024-11-05/client/sampling) 请求 | | Client | `experimental` | 描述对非标准实验性功能的支持 | | Server | `prompts` | 提供 [提示模板](/specification/2024-11-05/server/prompts) | | Server | `resources` | 提供可读的 [资源](/specification/2024-11-05/server/resources) | | Server | `tools` | 暴露可调用的 [工具](/specification/2024-11-05/server/tools) | | Server | `logging` | 发出结构化的 [日志消息](/specification/2024-11-05/server/utilities/logging) | | Server | `experimental` | 描述对非标准实验性功能的支持 |

Capability objects can describe sub-capabilities like:
能力对象可以描述子能力，例如：

* `listChanged`: Support for list change notifications (for prompts, resources, and
  tools)
* `subscribe`: Support for subscribing to individual items' changes (resources only)
* `listChanged`: 支持列表变更通知（针对提示、资源和工具） * `subscribe`: 支持订阅单个项目的变更（仅限资源）

### Operation  ### 操作

During the operation phase, the client and server exchange messages according to the
negotiated capabilities.
在操作阶段，客户端和服务器根据协商的能力交换消息。

Both parties **SHOULD**:  双方 **应当**：

* Respect the negotiated protocol version
* Only use capabilities that were successfully negotiated
* 尊重协商的协议版本 * 只使用成功协商的能力

### Shutdown  ### 关闭

During the shutdown phase, one side (usually the client) cleanly terminates the protocol
connection. No specific shutdown messages are defined—instead, the underlying transport
mechanism should be used to signal connection termination:
在关闭阶段，一方（通常是客户端）干净地终止协议连接。没有定义特定的关闭消息——相反，应使用底层传输机制来表示连接终止：

#### stdio  #### 标准输入输出

For the stdio [transport](/specification/2024-11-05/basic/transports), the
client **SHOULD** initiate shutdown by:
对于标准输入输出 [传输](/specification/2024-11-05/basic/transports)，客户端 **应当** 通过以下方式启动关闭：

1. First, closing the input stream to the child process (the server)
2. Waiting for the server to exit, or sending `SIGTERM` if the server does not exit
   within a reasonable time
3. Sending `SIGKILL` if the server does not exit within a reasonable time after `SIGTERM`
1. 首先关闭子进程（服务器）的输入流 2. 等待服务器退出，或者在服务器在合理时间内未退出时发送 `SIGTERM` 3. 如果在发送 `SIGTERM` 后合理时间内服务器仍未退出，则发送 `SIGKILL`

The server **MAY** initiate shutdown by closing its output stream to the client and
exiting.
服务器 **可能** 通过关闭其输出流到客户端并退出来启动关闭。

#### HTTP

For HTTP [transports](/specification/2024-11-05/basic/transports), shutdown
is indicated by closing the associated HTTP connection(s).
对于 HTTP [传输](/specification/2024-11-05/basic/transports)，关闭是通过关闭相关的 HTTP 连接来指示的。

## Error Handling  错误处理

Implementations **SHOULD** be prepared to handle these error cases:
实现应准备好处理以下错误情况：

* Protocol version mismatch
* Failure to negotiate required capabilities
* Initialize request timeout
* Shutdown timeout
* 协议版本不匹配 * 无法协商所需功能 * 初始化请求超时 * 关闭超时

Implementations **SHOULD** implement appropriate timeouts for all requests, to prevent
hung connections and resource exhaustion.
实现应实现所有请求的适当超时，以防止连接挂起和资源耗尽。

Example initialization error:
示例初始化错误：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Unsupported protocol version",
    "data": {
      "supported": ["2024-11-05"],
      "requested": "1.0.0"
    }
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "error": { "code": -32602, "message": "不支持的协议版本", "data": { "supported": ["2024-11-05"], "requested": "1.0.0" } } } ```


# Messages
Source: https://modelcontextprotocol.io/specification/2024-11-05/basic/messages
# 消息来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/messages



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**：2024-11-05

All messages in MCP **MUST** follow the
[JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines
three types of messages:
所有 MCP 消息都必须遵循[JSON-RPC 2.0](https://www.jsonrpc.org/specification)规范。该协议定义了三种类型的消息：

## Requests  ## 请求

Requests are sent from the client to the server or vice versa.
请求是从客户端发送到服务器或反之亦然。

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* Requests **MUST** include a string or integer ID.
* Unlike base JSON-RPC, the ID **MUST NOT** be `null`.
* The request ID **MUST NOT** have been previously used by the requestor within the same
  session.
* 请求**必须**包含一个字符串或整数 ID。* 与基础 JSON-RPC 不同，ID**不能**为`null`。* 请求 ID**不能**在同一个会话中由请求者之前使用过。

## Responses  ## 响应

Responses are sent in reply to requests.
响应是针对请求发送的。

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  result?: {
    [key: string]: unknown;
  }
  error?: {
    code: number;
    message: string;
    data?: unknown;
  }
}
```

* Responses **MUST** include the same ID as the request they correspond to.
* Either a `result` or an `error` **MUST** be set. A response **MUST NOT** set both.
* Error codes **MUST** be integers.
* 响应 **必须** 包含与请求相对应的相同 ID。* 必须设置 `result` 或 `error` 之一。响应 **不得** 同时设置两者。* 错误代码 **必须** 是整数。

## Notifications  ## 通知

Notifications are sent from the client to the server or vice versa. They do not expect a
response.
通知是从客户端发送到服务器或反之亦然。它们不期望收到响应。

```typescript
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* Notifications **MUST NOT** include an ID.
* 通知**不得**包含 ID。


# Transports
Source: https://modelcontextprotocol.io/specification/2024-11-05/basic/transports
# 传输来源：https://modelcontextprotocol.io/specification/2024-11-05/basic/transports



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**：2024-11-05

MCP currently defines two standard transport mechanisms for client-server communication:
MCP 目前定义了两种标准传输机制用于客户端-服务器通信：

1. [stdio](#stdio), communication over standard in and standard out
2. [HTTP with Server-Sent Events](#http-with-sse) (SSE)
1. [stdio](#stdio)，标准输入和标准输出通信 2. [HTTP 与服务器发送事件](#http-with-sse)（SSE）

Clients **SHOULD** support stdio whenever possible.
客户端**应**尽可能支持 stdio。

It is also possible for clients and servers to implement
[custom transports](#custom-transports) in a pluggable fashion.
客户端和服务器也可以以可插拔的方式实现[自定义传输](#custom-transports)。

## stdio

In the **stdio** transport:
在 **stdio** 传输中：

* The client launches the MCP server as a subprocess.
* The server receives JSON-RPC messages on its standard input (`stdin`) and writes
  responses to its standard output (`stdout`).
* Messages are delimited by newlines, and **MUST NOT** contain embedded newlines.
* The server **MAY** write UTF-8 strings to its standard error (`stderr`) for logging
  purposes. Clients **MAY** capture, forward, or ignore this logging.
* The server **MUST NOT** write anything to its `stdout` that is not a valid MCP message.
* The client **MUST NOT** write anything to the server's `stdin` that is not a valid MCP
  message.
* 客户端以子进程的形式启动 MCP 服务器。 * 服务器在其标准输入（`stdin`）上接收 JSON-RPC 消息，并将响应写入其标准输出（`stdout`）。 * 消息由换行符分隔，**不得**包含嵌入的换行符。 * 服务器**可以**将其标准错误（`stderr`）写入 UTF-8 字符串以进行日志记录。客户端**可以**捕获、转发或忽略此日志。 * 服务器**不得**将其 `stdout` 写入任何非有效 MCP 消息。 * 客户端**不得**将其 `stdin` 写入任何非有效 MCP 消息。

```mermaid
sequenceDiagram
    participant Client
    participant Server Process
```mermaid sequenceDiagram participant 客户端 participant 服务器 Process

    Client->>+Server Process: Launch subprocess
    loop Message Exchange
        Client->>Server Process: Write to stdin
        Server Process->>Client: Write to stdout
        Server Process--)Client: Optional logs on stderr
    end
    Client->>Server Process: Close stdin, terminate subprocess
    deactivate Server Process
```
客户端->>+服务器 Process: 启动子进程循环 客户端->>服务器 Process: 写入 stdin 服务器 Process->>客户端: 写入 stdout 服务器 Process--)客户端: 可选的日志在 stderr 上结束 客户端->>服务器 Process: 关闭 stdin，终止子进程 deactivate 服务器 Process ```

## HTTP with SSE  ## HTTP 与 SSE

In the **SSE** transport, the server operates as an independent process that can handle
multiple client connections.
在**SSE**传输中，服务器作为一个独立进程运行，可以处理多个客户端连接。

#### Security Warning  #### 安全警告

When implementing HTTP with SSE transport:
实现 HTTP 与 SSE 传输时：

1. Servers **MUST** validate the `Origin` header on all incoming connections to prevent DNS rebinding attacks
2. When running locally, servers **SHOULD** bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)
3. Servers **SHOULD** implement proper authentication for all connections
1. 服务器 **必须** 验证所有传入连接的 `Origin` 标头，以防止 DNS 重绑定攻击 2. 当本地运行时，服务器 **应该** 仅绑定到 localhost (127.0.0.1)，而不是所有网络接口 (0.0.0.0) 3. 服务器 **应该** 为所有连接实现适当的身份验证

Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites.
如果没有这些保护措施，攻击者可能会使用 DNS 重绑定从远程网站与本地 MCP 服务器交互。

The server **MUST** provide two endpoints:
服务器 **必须** 提供两个端点：

1. An SSE endpoint, for clients to establish a connection and receive messages from the
   server
2. A regular HTTP POST endpoint for clients to send messages to the server
1. 一个 SSE 端点，供客户端建立连接并从服务器接收消息 2. 一个常规 HTTP POST 端点，供客户端向服务器发送消息

When a client connects, the server **MUST** send an `endpoint` event containing a URI for
the client to use for sending messages. All subsequent client messages **MUST** be sent
as HTTP POST requests to this endpoint.
当客户端连接时，服务器 **必须** 发送一个包含客户端用于发送消息的 URI 的 `endpoint` 事件。所有后续客户端消息 **必须** 作为 HTTP POST 请求发送到该端点。

Server messages are sent as SSE `message` events, with the message content encoded as
JSON in the event data.
服务器消息以 SSE `message` 事件的形式发送，消息内容以 JSON 编码在事件数据中。

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Client->>Server: Open SSE connection
    Server->>Client: endpoint event
    loop Message Exchange
        Client->>Server: HTTP POST messages
        Server->>Client: SSE message events
    end
    Client->>Server: Close SSE connection
```
客户端->>服务器：打开 SSE 连接 服务器->>客户端：端点事件循环 消息交换 客户端->>服务器：HTTP POST 消息 服务器->>客户端：SSE 消息事件结束 客户端->>服务器：关闭 SSE 连接

## Custom Transports  ## 自定义传输

Clients and servers **MAY** implement additional custom transport mechanisms to suit
their specific needs. The protocol is transport-agnostic and can be implemented over any
communication channel that supports bidirectional message exchange.
客户端和服务器 **可以** 实现额外的自定义传输机制以满足其特定需求。该协议与传输无关，可以在支持双向消息交换的任何通信通道上实现。

Implementers who choose to support custom transports **MUST** ensure they preserve the
JSON-RPC message format and lifecycle requirements defined by MCP. Custom transports
**SHOULD** document their specific connection establishment and message exchange patterns
to aid interoperability.
选择支持自定义传输的实现者**必须**确保它们保留 MCP 定义的 JSON-RPC 消息格式和生命周期要求。自定义传输**应该**记录其特定的连接建立和消息交换模式，以帮助互操作性。


# Cancellation
Source: https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/cancellation
# 取消源：https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/cancellation



<Info>**Protocol Revision**: 2024-11-05</Info>
<信息>**协议修订版**：2024-11-05

The Model Context Protocol (MCP) supports optional cancellation of in-progress requests
through notification messages. Either side can send a cancellation notification to
indicate that a previously-issued request should be terminated.
模型上下文协议（MCP）支持通过通知消息取消正在进行的请求。任何一方都可以发送取消通知，以指示应终止之前发出的请求。

## Cancellation Flow  ## 取消流程

When a party wants to cancel an in-progress request, it sends a `notifications/cancelled`
notification containing:
当一个党派想要取消一个正在进行的请求时，它发送一个包含以下内容的`notifications/cancelled`通知：

* The ID of the request to cancel
* An optional reason string that can be logged or displayed
*请求取消的 ID* 可选的日志或显示的取消原因字符串

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/cancelled",
  "params": {
    "requestId": "123",
    "reason": "User requested cancellation"
  }
}
```
```json { "jsonrpc": "2.0", "method": "notifications/cancelled", "params": { "requestId": "123", "reason": "用户请求取消" } } ```

## Behavior Requirements  ## 行为要求

1. Cancellation notifications **MUST** only reference requests that:
   * Were previously issued in the same direction
   * Are believed to still be in-progress
2. The `initialize` request **MUST NOT** be cancelled by clients
3. Receivers of cancellation notifications **SHOULD**:
   * Stop processing the cancelled request
   * Free associated resources
   * Not send a response for the cancelled request
4. Receivers **MAY** ignore cancellation notifications if:
   * The referenced request is unknown
   * Processing has already completed
   * The request cannot be cancelled
5. The sender of the cancellation notification **SHOULD** ignore any response to the
   request that arrives afterward
1. 取消通知**必须**仅引用以下请求：*之前已在同一方向发出的请求*认为仍在进行中的请求 2. 客户**不得**取消`initialize`请求 3. 接收取消通知的接收者**应该**：*停止处理已取消的请求*释放相关资源*不发送对已取消请求的响应 4. 接收者**可以**忽略以下取消通知：*引用的请求未知*处理已完成*请求无法取消 5. 取消通知的发送者**应该**忽略之后到达的任何对请求的响应

## Timing Considerations  时间考虑因素

Due to network latency, cancellation notifications may arrive after request processing
has completed, and potentially after a response has already been sent.
由于网络延迟，取消通知可能会在请求处理完成后到达，甚至可能在响应已经发送之后。

Both parties **MUST** handle these race conditions gracefully:
双方**必须**优雅地处理这些竞态条件：

```mermaid
sequenceDiagram
   participant Client
   participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

   Client->>Server: Request (ID: 123)
   Note over Server: Processing starts
   Client--)Server: notifications/cancelled (ID: 123)
   alt
      Note over Server: Processing may have<br/>completed before<br/>cancellation arrives
   else If not completed
      Note over Server: Stop processing
   end
```
客户端->服务器：请求（ID：123）备注在服务器上：处理开始 客户端--)服务器：通知/已取消（ID：123）备选备注在服务器上：处理可能已完成，在取消到达之前
否则如果未完成 备注在服务器上：停止处理 end

## Implementation Notes  实现说明

* Both parties **SHOULD** log cancellation reasons for debugging
* Application UIs **SHOULD** indicate when cancellation is requested
* 双方 **应** 记录取消原因以供调试 * 应用程序用户界面 **应** 显示已请求取消

## Error Handling  错误处理

Invalid cancellation notifications **SHOULD** be ignored:
无效的取消通知 **应** 被忽略：

* Unknown request IDs
* Already completed requests
* Malformed notifications
* 未知请求 ID * 已完成的请求 * 格式错误的通知

This maintains the "fire and forget" nature of notifications while allowing for race
conditions in asynchronous communication.
这保持了通知的“火速行动，不问结果”特性，同时允许异步通信中的竞态条件。


# Ping
Source: https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/ping
# Ping 来源: https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/ping



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**: 2024-11-05

The Model Context Protocol includes an optional ping mechanism that allows either party
to verify that their counterpart is still responsive and the connection is alive.
模型上下文协议包含一个可选的 ping 机制，允许任何一方验证对方是否仍然响应并且连接是活跃的。

## Overview  ## 概述

The ping functionality is implemented through a simple request/response pattern. Either
the client or server can initiate a ping by sending a `ping` request.
ping 功能通过简单的请求/响应模式实现。客户端或服务器都可以通过发送`ping`请求来发起 ping。

## Message Format  消息格式

A ping request is a standard JSON-RPC request with no parameters:
ping 请求是一个没有参数的标准 JSON-RPC 请求：

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "method": "ping"
}
```

## Behavior Requirements  行为需求

1. The receiver **MUST** respond promptly with an empty response:
1. 接收方 **必须** 立即响应，返回一个空响应：

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {}
}
```

2. If no response is received within a reasonable timeout period, the sender **MAY**:
   * Consider the connection stale
   * Terminate the connection
   * Attempt reconnection procedures
2. 如果在合理的超时时间内没有收到响应，发送方 **可以**： * 考虑连接已失效 * 终止连接 * 尝试重新连接过程

## Usage Patterns  使用模式

```mermaid
sequenceDiagram
    participant Sender
    participant Receiver
```mermaid sequenceDiagram participant 发送者 participant 接收者

    Sender->>Receiver: ping request
    Receiver->>Sender: empty response
```
发送者->>接收者: ping 请求 接收者->>发送者: 空响应 ```

## Implementation Considerations
实现考虑

* Implementations **SHOULD** periodically issue pings to detect connection health
* The frequency of pings **SHOULD** be configurable
* Timeouts **SHOULD** be appropriate for the network environment
* Excessive pinging **SHOULD** be avoided to reduce network overhead
* 实现应定期发送 ping 来检测连接健康 * ping 的频率**应**可配置 * 超时**应**适合网络环境 * 应避免过度 ping 以减少网络开销

## Error Handling  ## 错误处理

* Timeouts **SHOULD** be treated as connection failures
* Multiple failed pings **MAY** trigger connection reset
* Implementations **SHOULD** log ping failures for diagnostics
* 超时**应**被视为连接故障 * 多次失败的 ping**可能**触发连接重置 * 实现应记录 ping 失败以供诊断


# Progress
Source: https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/progress
# 进度来源: https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/progress



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**: 2024-11-05

The Model Context Protocol (MCP) supports optional progress tracking for long-running
operations through notification messages. Either side can send progress notifications to
provide updates about operation status.
模型上下文协议（MCP）支持通过通知消息进行可选的进度跟踪，以支持长时间运行的操作。任何一方都可以发送进度通知，以提供操作状态的更新。

## Progress Flow  ## 进度流程

When a party wants to *receive* progress updates for a request, it includes a
`progressToken` in the request metadata.
当一方希望接收请求的进度更新时，它会在请求元数据中包含一个 `progressToken`。

* Progress tokens **MUST** be a string or integer value
* Progress tokens can be chosen by the sender using any means, but **MUST** be unique
  across all active requests.
* 进度令牌 **必须** 是字符串或整数值 * 发送方可以使用任何方式选择进度令牌，但 **必须** 在所有活动请求中保持唯一。

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "some_method",
  "params": {
    "_meta": {
      "progressToken": "abc123"
    }
  }
}
```

The receiver **MAY** then send progress notifications containing:
接收方 **可以** 然后发送包含以下内容的进度通知：

* The original progress token
* The current progress value so far
* An optional "total" value
* 原始进度令牌 * 到目前为止的当前进度值 * 可选的 "总" 值

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "abc123",
    "progress": 50,
    "total": 100
  }
}
```

* The `progress` value **MUST** increase with each notification, even if the total is
  unknown.
* The `progress` and the `total` values **MAY** be floating point.
* `progress` 值 **必须** 随每个通知递增，即使总数量未知。* `progress` 和 `total` 值 **可能** 是浮点数。

## Behavior Requirements  ## 行为要求

1. Progress notifications **MUST** only reference tokens that:
1. 进度通知 **必须** 仅引用以下令牌：

   * Were provided in an active request
   * Are associated with an in-progress operation
* 已提供在活动请求中 * 与正在进行的操作相关联

2. Receivers of progress requests **MAY**:
   * Choose not to send any progress notifications
   * Send notifications at whatever frequency they deem appropriate
   * Omit the total value if unknown
2. 进度请求的接收者 **可以**：* 选择不发送任何进度通知 * 根据他们认为合适的频率发送通知 * 如果未知，则省略总价值

```mermaid
sequenceDiagram
    participant Sender
    participant Receiver
```mermaid sequenceDiagram participant 发送者 participant 接收者

    Note over Sender,Receiver: Request with progress token
    Sender->>Receiver: Method request with progressToken
注释在 发送者,接收者 上：带有进度令牌的请求 发送者->>接收者：带有进度令牌的方法请求

    Note over Sender,Receiver: Progress updates
    loop Progress Updates
        Receiver-->>Sender: Progress notification (0.2/1.0)
        Receiver-->>Sender: Progress notification (0.6/1.0)
        Receiver-->>Sender: Progress notification (1.0/1.0)
    end
发送者，接收者：进度更新循环 接收者-->>发送者：进度通知（0.2/1.0）接收者-->>发送者：进度通知（0.6/1.0）接收者-->>发送者：进度通知（1.0/1.0）结束

    Note over Sender,Receiver: Operation complete
    Receiver->>Sender: Method response
```
发送者，接收者：操作完成 接收者->>发送者：方法响应 ```

## Implementation Notes  实现说明

* Senders and receivers **SHOULD** track active progress tokens
* Both parties **SHOULD** implement rate limiting to prevent flooding
* Progress notifications **MUST** stop after completion
* 发送者和接收者 **应** 跟踪活跃的进度令牌 * 双方 **应** 实现速率限制以防止洪水 * 进度通知 **必须** 在完成后停止


# Roots
Source: https://modelcontextprotocol.io/specification/2024-11-05/client/roots
根源来源：https://modelcontextprotocol.io/specification/2024-11-05/client/roots



<Info>**Protocol Revision**: 2024-11-05</Info>
<信息>**协议版本**：2024-11-05

The Model Context Protocol (MCP) provides a standardized way for clients to expose
filesystem "roots" to servers. Roots define the boundaries of where servers can operate
within the filesystem, allowing them to understand which directories and files they have
access to. Servers can request the list of roots from supporting clients and receive
notifications when that list changes.
模型上下文协议（MCP）为客户端向服务器暴露文件系统“根”提供了一种标准化的方式。根定义了服务器在文件系统中可以操作的范围，使它们能够了解哪些目录和文件它们可以访问。服务器可以从支持客户端请求根列表，并在该列表发生变化时接收通知。

## User Interaction Model
## 用户交互模型

Roots in MCP are typically exposed through workspace or project configuration interfaces.
MCP 中的根通常通过工作区或项目配置界面暴露。

For example, implementations could offer a workspace/project picker that allows users to
select directories and files the server should have access to. This can be combined with
automatic workspace detection from version control systems or project files.
例如，实现可以提供工作区/项目选择器，允许用户选择服务器应有权访问的目录和文件。这可以与来自版本控制系统或项目文件的自动工作区检测相结合。

However, implementations are free to expose roots through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.
然而，实现可以自由选择任何适合其需求的接口模式来暴露根——协议本身并不强制任何特定的用户交互模型。

## Capabilities  ## 功能

Clients that support roots **MUST** declare the `roots` capability during
[initialization](/specification/2024-11-05/basic/lifecycle#initialization):
支持根的客户端必须在[初始化](/specification/2024-11-05/basic/lifecycle#initialization)期间声明`roots`功能：

```json
{
  "capabilities": {
    "roots": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the client will emit notifications when the list of roots
changes.
`listChanged`表示客户端是否会在根列表发生变化时发出通知。

## Protocol Messages  ## 协议消息

### Listing Roots  ### 根目录列表

To retrieve roots, servers send a `roots/list` request:
要检索根目录，服务器发送一个 `roots/list` 请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "roots/list"
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "roots": [
      {
        "uri": "file:///home/user/projects/myproject",
        "name": "My Project"
      }
    ]
  }
}
```

### Root List Changes  ### 根列表变更

When roots change, clients that support `listChanged` **MUST** send a notification:
当根变更时，支持 `listChanged` 的客户端 **必须** 发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/roots/list_changed"
}
```

## Message Flow  ## 消息流程

```mermaid
sequenceDiagram
    participant Server
    participant Client
```mermaid sequenceDiagram participant 服务器 participant 客户端

    Note over Server,Client: Discovery
    Server->>Client: roots/list
    Client-->>Server: Available roots
注释在服务器、客户端上方：发现服务器-->>客户端：roots/list 客户端-->>服务器：可用的根

    Note over Server,Client: Changes
    Client--)Server: notifications/roots/list_changed
    Server->>Client: roots/list
    Client-->>Server: Updated roots
```
注意：服务器、客户端：客户端更改--服务器：通知/roots/list_changed 服务器>>>客户端：roots/list 客户端-->>服务器：已更新 roots

## Data Types  数据类型

### Root  ### 根

A root definition includes:
根定义包括：

* `uri`: Unique identifier for the root. This **MUST** be a `file://` URI in the current
  specification.
* `name`: Optional human-readable name for display purposes.
* `uri`：根的唯一标识符。在本规范中，此 **必须** 是 `file://` URI。* `name`：可选的用于显示的易读名称。

Example roots for different use cases:
不同用例的示例根

#### Project Directory  #### 项目目录

```json
{
  "uri": "file:///home/user/projects/myproject",
  "name": "My Project"
}
```

#### Multiple Repositories
#### 多个仓库

```json
[
  {
    "uri": "file:///home/user/repos/frontend",
    "name": "Frontend Repository"
  },
  {
    "uri": "file:///home/user/repos/backend",
    "name": "Backend Repository"
  }
]
```
```json [{ "uri": "file:///home/user/repos/frontend", "name": "前端仓库" }, { "uri": "file:///home/user/repos/backend", "name": "后端仓库" }] ```

## Error Handling  ## 错误处理

Clients **SHOULD** return standard JSON-RPC errors for common failure cases:
客户端 **应当** 返回标准 JSON-RPC 错误以处理常见的失败情况：

* Client does not support roots: `-32601` (Method not found)
* Internal errors: `-32603`
* 客户端不支持根节点：`-32601`（方法未找到） * 内部错误：`-32603`

Example error:  示例错误：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32601,
    "message": "Roots not supported",
    "data": {
      "reason": "Client does not have roots capability"
    }
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "error": { "code": -32601, "message": "不支持根", "data": { "reason": "客户端没有根能力" } } } ```

## Security Considerations
安全注意事项

1. Clients **MUST**:  1. 客户端 **必须**：

   * Only expose roots with appropriate permissions
   * Validate all root URIs to prevent path traversal
   * Implement proper access controls
   * Monitor root accessibility
* 仅暴露具有适当权限的根 * 验证所有根 URI 以防止路径遍历 * 实现适当的访问控制 * 监控根的可访问性

2. Servers **SHOULD**:
   * Handle cases where roots become unavailable
   * Respect root boundaries during operations
   * Validate all paths against provided roots
应该处理根不可用的情况 * 尊重操作过程中的根边界 * 对所有路径与提供的根进行验证

## Implementation Guidelines
实施指南

1. Clients **SHOULD**:  1. 客户端 **SHOULD**:

   * Prompt users for consent before exposing roots to servers
   * Provide clear user interfaces for root management
   * Validate root accessibility before exposing
   * Monitor for root changes
* 在向服务器暴露根之前提示用户同意 * 为根管理提供清晰的用户界面 * 在暴露之前验证根的可访问性 * 监控根的变化

2. Servers **SHOULD**:
   * Check for roots capability before usage
   * Handle root list changes gracefully
   * Respect root boundaries in operations
   * Cache root information appropriately
应当：* 在使用前检查 root 功能 * 优雅地处理 root 列表变更 * 在操作中尊重 root 边界 * 适当地缓存 root 信息


# Sampling
Source: https://modelcontextprotocol.io/specification/2024-11-05/client/sampling
#采样来源：https://modelcontextprotocol.io/specification/2024-11-05/client/sampling



<Info>**Protocol Revision**: 2024-11-05</Info>
<信息>**协议版本**：2024-11-05

The Model Context Protocol (MCP) provides a standardized way for servers to request LLM
sampling ("completions" or "generations") from language models via clients. This flow
allows clients to maintain control over model access, selection, and permissions while
enabling servers to leverage AI capabilities—with no server API keys necessary.
Servers can request text or image-based interactions and optionally include context from
MCP servers in their prompts.
模型上下文协议（MCP）为服务器提供了一种标准化的方式，通过客户端从语言模型请求LLM采样（“完成”或“生成”）。这种流程允许客户端维持对模型访问、选择和权限的控制，同时使服务器能够利用 AI 能力——无需服务器 API 密钥。服务器可以请求基于文本或图像的交互，并可选择在提示中包含来自 MCP 服务器的上下文。

## User Interaction Model
用户交互模型

Sampling in MCP allows servers to implement agentic behaviors, by enabling LLM calls to
occur *nested* inside other MCP server features.
在 MCP 中进行采样允许服务器通过启用LLM调用在其它 MCP 服务器功能中嵌套发生，以实现代理行为。

Implementations are free to expose sampling through any interface pattern that suits
their needs—the protocol itself does not mandate any specific user interaction
model.
实现者可以根据自己的需求自由选择任何接口模式来公开采样，协议本身并不强制规定任何特定的用户交互模型。

<Warning>
  For trust & safety and security, there **SHOULD** always
  be a human in the loop with the ability to deny sampling requests.
<警告>为了信任与安全以及安全起见，始终应该有人工智能在循环中，并具有拒绝采样请求的能力。

  Applications **SHOULD**:
应用程序 **应当**：

  * Provide UI that makes it easy and intuitive to review sampling requests
  * Allow users to view and edit prompts before sending
  * Present generated responses for review before delivery
</Warning>
* 提供易于审查采样请求的用户界面 * 允许用户在发送前查看和编辑提示 * 在交付前展示生成的响应以供审查 

## Capabilities  ## 功能

Clients that support sampling **MUST** declare the `sampling` capability during
[initialization](/specification/2024-11-05/basic/lifecycle#initialization):
支持采样的客户端 **必须** 在 [初始化](/specification/2024-11-05/basic/lifecycle#initialization) 时声明 `sampling` 功能：

```json
{
  "capabilities": {
    "sampling": {}
  }
}
```

## Protocol Messages  ## 协议消息

### Creating Messages  ### 创建消息

To request a language model generation, servers send a `sampling/createMessage` request:
请求语言模型生成时，服务器发送 `sampling/createMessage` 请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What is the capital of France?"
        }
      }
    ],
    "modelPreferences": {
      "hints": [
        {
          "name": "claude-3-sonnet"
        }
      ],
      "intelligencePriority": 0.8,
      "speedPriority": 0.5
    },
    "systemPrompt": "You are a helpful assistant.",
    "maxTokens": 100
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "method": "sampling/createMessage", "params": { "messages": [ { "role": "user", "content": { "type": "text", "text": "法国的首都是什么？" } } ], "modelPreferences": { "hints": [ { "name": "claude-3-sonnet" } ], "intelligencePriority": 0.8, "speedPriority": 0.5 }, "systemPrompt": "你是一个有用的助手。", "maxTokens": 100 } } ```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "role": "assistant",
    "content": {
      "type": "text",
      "text": "The capital of France is Paris."
    },
    "model": "claude-3-sonnet-20240307",
    "stopReason": "endTurn"
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "result": { "role": "assistant", "content": { "type": "text", "text": "法国的首都是巴黎。" }, "model": "claude-3-sonnet-20240307", "stopReason": "endTurn" } } ```

## Message Flow  消息流程

```mermaid
sequenceDiagram
    participant Server
    participant Client
    participant User
    participant LLM
```mermaid sequenceDiagram participant 服务器 participant 客户端 participant 用户 participant LLM

    Note over Server,Client: Server initiates sampling
    Server->>Client: sampling/createMessage
注释在 服务器,客户端 上: 服务器启动采样 服务器->>客户端: sampling/createMessage

    Note over Client,User: Human-in-the-loop review
    Client->>User: Present request for approval
    User-->>Client: Review and approve/modify
注释在 客户端,用户 上: 人工审核 客户端->>用户: 展示请求以供批准 用户-->>客户端: 审查并修改

    Note over Client,LLM: Model interaction
    Client->>LLM: Forward approved request
    LLM-->>Client: Return generation
客户端备注，LLM：模型交互 客户端->>LLM：转发批准的请求 LLM-->>客户端：返回生成

    Note over Client,User: Response review
    Client->>User: Present response for approval
    User-->>Client: Review and approve/modify
客户端备注，用户：响应审查 客户端->>用户：呈现待批准的响应 用户-->>客户端：审查并批准/修改

    Note over Server,Client: Complete request
    Client-->>Server: Return approved response
```
服务器备注，客户端：完成请求 客户端-->>服务器：返回批准的响应 ```

## Data Types  数据类型

### Messages  ### 消息

Sampling messages can contain:
抽样消息可能包含：

#### Text Content  #### 文本内容

```json
{
  "type": "text",
  "text": "The message content"
}
```
```json { "type": "text", "text": "消息内容" } ```

#### Image Content  图像内容

```json
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/jpeg"
}
```
```json { "type": "image", "data": "base64 编码的图像数据", "mimeType": "image/jpeg" } ```

### Model Preferences  ### 模型偏好

Model selection in MCP requires careful abstraction since servers and clients may use
different AI providers with distinct model offerings. A server cannot simply request a
specific model by name since the client may not have access to that exact model or may
prefer to use a different provider's equivalent model.
在 MCP 中进行模型选择需要仔细的抽象，因为服务器和客户端可能使用不同的 AI 提供商，具有不同的模型提供。服务器不能简单地通过名称请求特定的模型，因为客户端可能无法访问该特定模型，或者可能更喜欢使用不同提供商的等效模型。

To solve this, MCP implements a preference system that combines abstract capability
priorities with optional model hints:
为了解决这个问题，MCP 实现了一个偏好系统，该系统结合了抽象能力优先级和可选模型提示：

#### Capability Priorities
#### 能力优先级

Servers express their needs through three normalized priority values (0-1):
服务器通过三个标准化的优先级值（0-1）表达需求：

* `costPriority`: How important is minimizing costs? Higher values prefer cheaper models.
* `speedPriority`: How important is low latency? Higher values prefer faster models.
* `intelligencePriority`: How important are advanced capabilities? Higher values prefer
  more capable models.
* `costPriority`：最小化成本的重要性如何？更高的值更倾向于选择更便宜的模式。 * `speedPriority`：低延迟的重要性如何？更高的值更倾向于选择更快的模式。 * `intelligencePriority`：高级功能的重要性如何？更高的值更倾向于选择功能更强大的模式。

#### Model Hints  #### 模型提示

While priorities help select models based on characteristics, `hints` allow servers to
suggest specific models or model families:
虽然优先级有助于根据特性选择模型，但“提示”允许服务器建议特定的模型或模型系列：

* Hints are treated as substrings that can match model names flexibly
* Multiple hints are evaluated in order of preference
* Clients **MAY** map hints to equivalent models from different providers
* Hints are advisory—clients make final model selection
*提示被视为可以灵活匹配模型名称的子字符串* 多个提示按优先级顺序评估 *客户端**可以**将提示映射到不同提供商的等效模型 *提示仅供参考——客户端进行最终模型选择

For example:  例如：

```json
{
  "hints": [
    { "name": "claude-3-sonnet" }, // Prefer Sonnet-class models
    { "name": "claude" } // Fall back to any Claude model
  ],
  "costPriority": 0.3, // Cost is less important
  "speedPriority": 0.8, // Speed is very important
  "intelligencePriority": 0.5 // Moderate capability needs
}
```
```json { "hints": [ { "name": "claude-3-sonnet" }, // 优先选择 Sonnet 类模型 { "name": "claude" } // 回退到任何 Claude 模型 ], "costPriority": 0.3, // 成本不太重要 "speedPriority": 0.8, // 速度非常重要 "intelligencePriority": 0.5 // 中等能力需求 } ```

The client processes these preferences to select an appropriate model from its available
options. For instance, if the client doesn't have access to Claude models but has Gemini,
it might map the sonnet hint to `gemini-1.5-pro` based on similar capabilities.
客户端处理这些偏好以从其可用选项中选择适当的模型。例如，如果客户端无法访问 Claude 模型但拥有 Gemini，它可能会根据相似的能力将 sonnet 提示映射到`gemini-1.5-pro`。

## Error Handling  ## 错误处理

Clients **SHOULD** return errors for common failure cases:
客户 **应当** 为常见的失败情况返回错误：

Example error:  示例错误：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -1,
    "message": "User rejected sampling request"
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "error": { "code": -1, "message": "用户拒绝采样请求" } } ```

## Security Considerations
安全注意事项

1. Clients **SHOULD** implement user approval controls
2. Both parties **SHOULD** validate message content
3. Clients **SHOULD** respect model preference hints
4. Clients **SHOULD** implement rate limiting
5. Both parties **MUST** handle sensitive data appropriately
1. 客户 **应当** 实现用户批准控制 2. 双方 **应当** 验证消息内容 3. 客户 **应当** 尊重模型偏好提示 4. 客户 **应当** 实现速率限制 5. 双方 **必须** 适当处理敏感数据


# Specification
Source: https://modelcontextprotocol.io/specification/2024-11-05/index
# 规范来源：https://modelcontextprotocol.io/specification/2024-11-05/index



[Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open protocol that
enables seamless integration between LLM applications and external data sources and
tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating
custom AI workflows, MCP provides a standardized way to connect LLMs with the context
they need.
[模型上下文协议](https://modelcontextprotocol.io)（MCP）是一个开放协议，它使得 LLM 应用程序和外部数据源及工具之间能够实现无缝集成。无论您是在构建一个 AI 驱动的 IDE、增强聊天界面，还是创建定制的 AI 工作流程，MCP 都提供了一种标准化的方式来连接 LLMs 与它们所需的上下文。

This specification defines the authoritative protocol requirements, based on the
TypeScript schema in
[schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2024-11-05/schema.ts).
本规范定义了基于 TypeScript 架构的权威协议要求，架构在 [schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2024-11-05/schema.ts)。

For implementation guides and examples, visit
[modelcontextprotocol.io](https://modelcontextprotocol.io).
欲获取实施指南和示例，请访问 [modelcontextprotocol.io](https://modelcontextprotocol.io)。

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD
NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14)
\[[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)]
\[[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)] when, and only when, they
appear in all capitals, as shown here.
本文档中，“必须”、“禁止”、“必需”、“应当”、“不应当”、“应该”、“不应该”、“推荐”、“不推荐”、“可以”和“可选”等关键词，当且仅当它们全部大写，如本例所示时，应按照[BCP 14](https://datatracker.ietf.org/doc/html/bcp14) \[[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)] \[[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)]中的描述进行解释。

## Overview  ## 概述

MCP provides a standardized way for applications to:
MCP 为应用程序提供了一种标准化的方式：

* Share contextual information with language models
* Expose tools and capabilities to AI systems
* Build composable integrations and workflows
* 与语言模型共享上下文信息 * 向 AI 系统暴露工具和能力 * 构建可组合的集成和工作流程

The protocol uses [JSON-RPC](https://www.jsonrpc.org/) 2.0 messages to establish
communication between:
该协议使用[JSON-RPC](https://www.jsonrpc.org/) 2.0 消息来建立以下内容之间的通信：

* **Hosts**: LLM applications that initiate connections
* **Clients**: Connectors within the host application
* **Servers**: Services that provide context and capabilities
**主机**: LLM 发起连接的应用程序 **客户端**: 主机应用程序内的连接器 **服务器**: 提供上下文和功能的服务

MCP takes some inspiration from the
[Language Server Protocol](https://microsoft.github.io/language-server-protocol/), which
standardizes how to add support for programming languages across a whole ecosystem of
development tools. In a similar way, MCP standardizes how to integrate additional context
and tools into the ecosystem of AI applications.
MCP 从 [语言服务器协议](https://microsoft.github.io/language-server-protocol/) 中汲取了一些灵感，该协议标准化了在整个开发工具生态系统内添加对编程语言支持的方式。以类似的方式，MCP 标准化了如何将额外的上下文和工具集成到人工智能应用程序的生态系统中。

## Key Details  ## 关键细节

### Base Protocol  ### 基础协议

* [JSON-RPC](https://www.jsonrpc.org/) message format
* Stateful connections
* Server and client capability negotiation
* [JSON-RPC](https://www.jsonrpc.org/) 消息格式 * 状态连接 * 服务器和客户端能力协商

### Features  ### 功能

Servers offer any of the following features to clients:
服务器向客户端提供以下任何功能：

* **Resources**: Context and data, for the user or the AI model to use
* **Prompts**: Templated messages and workflows for users
* **Tools**: Functions for the AI model to execute
* **资源**：用户或 AI 模型使用的上下文和数据 * **提示**：为用户提供的模板消息和工作流程 * **工具**：AI 模型执行的函数

Clients may offer the following feature to servers:
客户可以向服务器提供以下功能：

* **Sampling**: Server-initiated agentic behaviors and recursive LLM interactions
* **采样**：服务器发起的代理行为和递归 LLM 交互

### Additional Utilities  ### 其他实用工具

* Configuration
* Progress tracking
* Cancellation
* Error reporting
* Logging
* 配置 * 进度跟踪 * 取消 * 错误报告 * 记录日志

## Security and Trust & Safety
安全与信任

The Model Context Protocol enables powerful capabilities through arbitrary data access
and code execution paths. With this power comes important security and trust
considerations that all implementors must carefully address.
模型上下文协议通过任意数据访问和代码执行路径提供了强大的功能。这种能力带来了重要的安全和信任考虑，所有实现者都必须仔细处理。

### Key Principles  ### 关键原则

1. **User Consent and Control**
1. **用户同意与控制**

   * Users must explicitly consent to and understand all data access and operations
   * Users must retain control over what data is shared and what actions are taken
   * Implementors should provide clear UIs for reviewing and authorizing activities
用户必须明确同意并理解所有数据访问和操作 * 用户必须保留控制权，决定共享哪些数据和采取哪些行动 * 实施者应提供清晰的用户界面，以便审查和授权活动

2. **Data Privacy**  2. **数据隐私**

   * Hosts must obtain explicit user consent before exposing user data to servers
   * Hosts must not transmit resource data elsewhere without user consent
   * User data should be protected with appropriate access controls
* 主机必须在向服务器暴露用户数据之前获得用户的明确同意 * 主机不得未经用户同意将资源数据传输到其他地方 * 应使用适当的访问控制保护用户数据

3. **Tool Safety**  3. **工具安全**

   * Tools represent arbitrary code execution and must be treated with appropriate
     caution
   * Hosts must obtain explicit user consent before invoking any tool
   * Users should understand what each tool does before authorizing its use
* 工具代表任意代码执行，必须谨慎对待 * 主机在调用任何工具之前必须获得用户的明确同意 * 用户在授权使用之前应了解每个工具的功能

4. **LLM Sampling Controls**
   * Users must explicitly approve any LLM sampling requests
   * Users should control:
     * Whether sampling occurs at all
     * The actual prompt that will be sent
     * What results the server can see
   * The protocol intentionally limits server visibility into prompts
4. **LLM 样本控制** * 用户必须明确批准任何 LLM 样本请求 * 用户应控制： * 是否进行采样 * 实际发送的提示 * 服务器可以看到的结果 * 协议有意限制服务器对提示的可见性

### Implementation Guidelines
### 实施指南

While MCP itself cannot enforce these security principles at the protocol level,
implementors **SHOULD**:
虽然 MCP 本身无法在协议级别强制执行这些安全原则，实现者 **应**：

1. Build robust consent and authorization flows into their applications
2. Provide clear documentation of security implications
3. Implement appropriate access controls and data protections
4. Follow security best practices in their integrations
5. Consider privacy implications in their feature designs
1. 在其应用程序中构建稳健的同意和授权流程 2. 提供安全影响清晰的文档 3. 实施适当的访问控制和数据保护 4. 在其集成中遵循安全最佳实践 5. 在其功能设计中考虑隐私影响

## Learn More  了解更多

Explore the detailed specification for each protocol component:
查看每个协议组件的详细规格说明：

<CardGroup cols={5}>
  <Card title="Architecture" icon="sitemap" href="architecture" />
 

  <Card title="Base Protocol" icon="code" href="basic" />


  <Card title="Server Features" icon="server" href="server" />


  <Card title="Client Features" icon="user" href="client" />


  <Card title="Contributing" icon="pencil" href="contributing" />
</CardGroup>



# Overview
Source: https://modelcontextprotocol.io/specification/2024-11-05/server/index
# 概述 来源: https://modelcontextprotocol.io/specification/2024-11-05/server/index



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**: 2024-11-05

Servers provide the fundamental building blocks for adding context to language models via
MCP. These primitives enable rich interactions between clients, servers, and language
models:
服务器为通过 MCP 添加上下文到语言模型提供了基本构建块。这些原语使得客户端、服务器和语言模型之间能够进行丰富的交互：

* **Prompts**: Pre-defined templates or instructions that guide language model
  interactions
* **Resources**: Structured data or content that provides additional context to the model
* **Tools**: Executable functions that allow models to perform actions or retrieve
  information
* **提示**：预定义的模板或指令，用于指导语言模型交互 * **资源**：提供额外上下文的结构化数据或内容 * **工具**：允许模型执行操作或检索信息的可执行函数

Each primitive can be summarized in the following control hierarchy:
每个原语可以总结如下控制层次结构：

| Primitive | Control                | Description                                        | Example                         |
| --------- | ---------------------- | -------------------------------------------------- | ------------------------------- |
| Prompts   | User-controlled        | Interactive templates invoked by user choice       | Slash commands, menu options    |
| Resources | Application-controlled | Contextual data attached and managed by the client | File contents, git history      |
| Tools     | Model-controlled       | Functions exposed to the LLM to take actions       | API POST requests, file writing |
| 原始 | 控制 | 描述 | 示例 | | --------- | ---------------------- | -------------------------------------------------- | ------------------------------- | | 提示 | 用户控制 | 用户选择触发的交互式模板 | 划分命令、菜单选项 | | 资源 | 应用控制 | 客户端附加和管理上下文数据 | 文件内容、git 历史 | | 工具 | 模型控制 | 暴露给 LLM 以执行操作的函数 | API POST 请求、文件写入 |

Explore these key primitives in more detail below:
在下面更详细地探索这些关键原始操作：

<CardGroup cols={3}>
  <Card title="Prompts" icon="message" href="prompts" />
 

  <Card title="Resources" icon="file-lines" href="resources" />


  <Card title="Tools" icon="wrench" href="tools" />
</CardGroup>
 


# Prompts
Source: https://modelcontextprotocol.io/specification/2024-11-05/server/prompts
# 提示来源: https://modelcontextprotocol.io/specification/2024-11-05/server/prompts



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**: 2024-11-05

The Model Context Protocol (MCP) provides a standardized way for servers to expose prompt
templates to clients. Prompts allow servers to provide structured messages and
instructions for interacting with language models. Clients can discover available
prompts, retrieve their contents, and provide arguments to customize them.
模型上下文协议（MCP）为服务器向客户端暴露提示模板提供了一种标准化方式。提示允许服务器提供结构化消息和指令，以便与语言模型交互。客户端可以发现可用的提示，检索其内容，并提供参数以自定义它们。

## User Interaction Model
用户交互模型

Prompts are designed to be **user-controlled**, meaning they are exposed from servers to
clients with the intention of the user being able to explicitly select them for use.
提示被设计为**用户可控**，这意味着它们从服务器暴露给客户端，目的是让用户能够明确选择它们进行使用。

Typically, prompts would be triggered through user-initiated commands in the user
interface, which allows users to naturally discover and invoke available prompts.
通常，提示将通过用户界面中的用户发起的命令来触发，这使用户能够自然地发现和调用可用的提示。

For example, as slash commands:
例如，作为斜杠命令：

![Example of prompt exposed as slash command](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2024-11-05/server/slash-command.png)
![示例：作为斜杠命令暴露的提示](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2024-11-05/server/slash-command.png)

However, implementors are free to expose prompts through any interface pattern that suits
their needs—the protocol itself does not mandate any specific user interaction
model.
然而，实现者可以根据自己的需求自由选择任何接口模式来暴露提示——协议本身并不强制规定任何特定的用户交互模型。

## Capabilities  ## 功能

Servers that support prompts **MUST** declare the `prompts` capability during
[initialization](/specification/2024-11-05/basic/lifecycle#initialization):
支持提示的服务器必须在[初始化](/specification/2024-11-05/basic/lifecycle#initialization)期间声明`prompts`功能：

```json
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the server will emit notifications when the list of
available prompts changes.
`listChanged` 表示服务器是否会在可用提示列表更改时发出通知。

## Protocol Messages  ## 协议消息

### Listing Prompts  ### 提示列表

To retrieve available prompts, clients send a `prompts/list` request. This operation
supports
[pagination](/specification/2024-11-05/server/utilities/pagination).
要获取可用的提示，客户端发送一个 `prompts/list` 请求。此操作支持[分页](/specification/2024-11-05/server/utilities/pagination)。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "prompts/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "prompts": [
      {
        "name": "code_review",
        "description": "Asks the LLM to analyze code quality and suggest improvements",
        "arguments": [
          {
            "name": "code",
            "description": "The code to review",
            "required": true
          }
        ]
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### Getting a Prompt  ### 获取提示

To retrieve a specific prompt, clients send a `prompts/get` request. Arguments may be
auto-completed through [the completion API](/specification/2024-11-05/server/utilities/completion).
客户端发送 `prompts/get` 请求以检索特定提示。参数可以通过 [完成 API](/specification/2024-11-05/server/utilities/completion) 自动完成。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "prompts/get",
  "params": {
    "name": "code_review",
    "arguments": {
      "code": "def hello():\n    print('world')"
    }
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "description": "Code review prompt",
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "Please review this Python code:\ndef hello():\n    print('world')"
        }
      }
    ]
  }
}
```
```json { "jsonrpc": "2.0", "id": 2, "result": { "description": "代码审查提示", "messages": [ { "role": "user", "content": { "type": "text", "text": "请审查以下 Python 代码：\ndef hello():\n print('world')" } } ] } } ```

### List Changed Notification
### 列表变更通知

When the list of available prompts changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:
当可用的提示列表发生变化时，声明了 `listChanged` 功能的服务器 **应当** 发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}
```

## Message Flow  ## 消息流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client,Server: Discovery
    Client->>Server: prompts/list
    Server-->>Client: List of prompts
注意：客户端、服务器：发现 客户端->>服务器：prompts/list 服务器-->>客户端：提示列表

    Note over Client,Server: Usage
    Client->>Server: prompts/get
    Server-->>Client: Prompt content
客户端、服务器：使用说明 客户端->>服务器：提示/get 服务器-->>客户端：提示内容

    opt listChanged
      Note over Client,Server: Changes
      Server--)Client: prompts/list_changed
      Client->>Server: prompts/list
      Server-->>Client: Updated prompts
    end
```
选项 listChanged 客户端、服务器：变更 服务器--)客户端：prompts/list_changed 客户端->>服务器：prompts/list 服务器-->>客户端：更新后的提示结束 ```

## Data Types  ## 数据类型

### Prompt  ### 提示

A prompt definition includes:
提示定义包括：

* `name`: Unique identifier for the prompt
* `description`: Optional human-readable description
* `arguments`: Optional list of arguments for customization
* `名称`: 提示的唯一标识符 * `描述`: 可选的易读描述 * `参数`: 可选的自定义参数列表

### PromptMessage  ### 提示消息

Messages in a prompt can contain:
提示中的消息可以包含：

* `role`: Either "user" or "assistant" to indicate the speaker
* `content`: One of the following content types:
* `角色`: 表示说话者的 "用户" 或 "助手" * `内容`: 以下内容类型之一:

#### Text Content  #### 文本内容

Text content represents plain text messages:
文本内容表示纯文本消息：

```json
{
  "type": "text",
  "text": "The text content of the message"
}
```
```json { "type": "text", "text": "消息的文本内容" } ```

This is the most common content type used for natural language interactions.
这是最常用的自然语言交互内容类型。

#### Image Content  图像内容

Image content allows including visual information in messages:
图片内容允许在消息中包含视觉信息：

```json
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/png"
}
```

The image data **MUST** be base64-encoded and include a valid MIME type. This enables
multi-modal interactions where visual context is important.
图片数据**必须**是 base64 编码的，并包含有效的 MIME 类型。这可以支持多模态交互，其中视觉上下文很重要。

#### Embedded Resources  #### 嵌入式资源

Embedded resources allow referencing server-side resources directly in messages:
嵌入式资源允许在消息中直接引用服务器端资源：

```json
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "Resource content"
  }
}
```
```json { "type": "resource", "resource": { "uri": "resource://example", "mimeType": "text/plain", "text": "资源内容" } } ```

Resources can contain either text or binary (blob) data and **MUST** include:
资源可以包含文本或二进制（blob）数据，**必须**包括：

* A valid resource URI
* The appropriate MIME type
* Either text content or base64-encoded blob data
一个有效的资源 URI * 适当的 MIME 类型 * 文本内容或 base64 编码的 blob 数据

Embedded resources enable prompts to seamlessly incorporate server-managed content like
documentation, code samples, or other reference materials directly into the conversation
flow.
嵌入式资源能够无缝地将服务器管理的文档、代码示例或其他参考资料直接集成到对话流程中。

## Error Handling  ## 错误处理

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:
服务器 **应当** 返回标准 JSON-RPC 错误以处理常见的失败情况：

* Invalid prompt name: `-32602` (Invalid params)
* Missing required arguments: `-32602` (Invalid params)
* Internal errors: `-32603` (Internal error)
* 无效的提示名称：`-32602`（无效参数）* 缺少必需的参数：`-32602`（无效参数）* 内部错误：`-32603`（内部错误）

## Implementation Considerations
## 实施注意事项

1. Servers **SHOULD** validate prompt arguments before processing
2. Clients **SHOULD** handle pagination for large prompt lists
3. Both parties **SHOULD** respect capability negotiation
1. 服务器 **应当** 在处理之前验证提示参数 2. 客户端 **应当** 处理大量提示列表的分页 3. 双方 **应当** 尊重能力协商

## Security  ## 安全

Implementations **MUST** carefully validate all prompt inputs and outputs to prevent
injection attacks or unauthorized access to resources.
实现必须仔细验证所有提示输入和输出，以防止注入攻击或未经授权访问资源。


# Resources
Source: https://modelcontextprotocol.io/specification/2024-11-05/server/resources
资源来源：https://modelcontextprotocol.io/specification/2024-11-05/server/resources



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**：2024-11-05

The Model Context Protocol (MCP) provides a standardized way for servers to expose
resources to clients. Resources allow servers to share data that provides context to
language models, such as files, database schemas, or application-specific information.
Each resource is uniquely identified by a
[URI](https://datatracker.ietf.org/doc/html/rfc3986).
模型上下文协议（MCP）为服务器向客户端暴露资源提供了一种标准化的方式。资源允许服务器共享为语言模型提供上下文的数据，例如文件、数据库模式或特定于应用程序的信息。每个资源都由一个[URI](https://datatracker.ietf.org/doc/html/rfc3986)唯一标识。

## User Interaction Model
## 用户交互模型

Resources in MCP are designed to be **application-driven**, with host applications
determining how to incorporate context based on their needs.
MCP 中的资源设计为**应用驱动**，主机应用程序根据其需求确定如何根据上下文进行整合。

For example, applications could:
例如，应用程序可以：

* Expose resources through UI elements for explicit selection, in a tree or list view
* Allow the user to search through and filter available resources
* Implement automatic context inclusion, based on heuristics or the AI model's selection
* 通过 UI 元素显式选择资源，以树形或列表视图呈现 * 允许用户搜索和筛选可用资源 * 根据启发式方法或 AI 模型的选取实现自动上下文包含

![Example of resource context picker](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2024-11-05/server/resource-picker.png)
![资源上下文选择器示例](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2024-11-05/server/resource-picker.png)

However, implementations are free to expose resources through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.
然而，实现者可以根据自己的需求自由选择任何接口模式来公开资源——协议本身并不强制规定任何特定的用户交互模型。

## Capabilities  ## 功能

Servers that support resources **MUST** declare the `resources` capability:
支持资源的服务器 **必须** 声明 `resources` 功能：

```json
{
  "capabilities": {
    "resources": {
      "subscribe": true,
      "listChanged": true
    }
  }
}
```

The capability supports two optional features:
该功能支持两个可选特性：

* `subscribe`: whether the client can subscribe to be notified of changes to individual
  resources.
* `listChanged`: whether the server will emit notifications when the list of available
  resources changes.
* `订阅`：客户端是否可以订阅以接收对单个资源的变更通知。 * `列表变更通知`：服务器是否会在可用资源列表发生变化时发出通知。

Both `subscribe` and `listChanged` are optional—servers can support neither,
either, or both:
`subscribe` 和 `listChanged` 都是可选的——服务器可以支持其中之一、两者或都不支持：

```json
{
  "capabilities": {
    "resources": {} // Neither feature supported
  }
}
```
```json { "capabilities": { "resources": {} // 两种功能均不支持 } } ```

```json
{
  "capabilities": {
    "resources": {
      "subscribe": true // Only subscriptions supported
    }
  }
}
```
```json { "capabilities": { "resources": { "subscribe": true // 仅支持订阅 } } } ```

```json
{
  "capabilities": {
    "resources": {
      "listChanged": true // Only list change notifications supported
    }
  }
}
```
```json { "capabilities": { "resources": { "listChanged": true // 仅支持列表变更通知 } } } ```

## Protocol Messages  ## 协议消息

### Listing Resources  ### 资源列表

To discover available resources, clients send a `resources/list` request. This operation
supports
[pagination](/specification/2024-11-05/server/utilities/pagination).
要发现可用资源，客户端发送 `resources/list` 请求。此操作支持[分页](/specification/2024-11-05/server/utilities/pagination)。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resources": [
      {
        "uri": "file:///project/src/main.rs",
        "name": "main.rs",
        "description": "Primary application entry point",
        "mimeType": "text/x-rust"
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### Reading Resources  ### 读取资源

To retrieve resource contents, clients send a `resources/read` request:
为了获取资源内容，客户端发送 `resources/read` 请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "resources/read",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "contents": [
      {
        "uri": "file:///project/src/main.rs",
        "mimeType": "text/x-rust",
        "text": "fn main() {\n    println!(\"Hello world!\");\n}"
      }
    ]
  }
}
```

### Resource Templates  ### 资源模板

Resource templates allow servers to expose parameterized resources using
[URI templates](https://datatracker.ietf.org/doc/html/rfc6570). Arguments may be
auto-completed through [the completion API](/specification/2024-11-05/server/utilities/completion).
资源模板允许服务器通过[URI 模板](https://datatracker.ietf.org/doc/html/rfc6570)公开参数化资源。参数可以通过[完成 API](/specification/2024-11-05/server/utilities/completion)自动补全。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/templates/list"
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "resourceTemplates": [
      {
        "uriTemplate": "file:///{path}",
        "name": "Project Files",
        "description": "Access files in the project directory",
        "mimeType": "application/octet-stream"
      }
    ]
  }
}
```
```json { "jsonrpc": "2.0", "id": 3, "result": { "resourceTemplates": [ { "uriTemplate": "file:///{path}", "name": "项目文件", "description": "访问项目目录中的文件", "mimeType": "application/octet-stream" } ] } } ```

### List Changed Notification
### 列表变更通知

When the list of available resources changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:
当可用资源列表发生变化时，声明了 `listChanged` 能力的服务器**应当**发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/list_changed"
}
```

### Subscriptions  ### 订阅

The protocol supports optional subscriptions to resource changes. Clients can subscribe
to specific resources and receive notifications when they change:
该协议支持可选的资源变更订阅。客户端可以订阅特定资源，并在资源发生变化时接收通知：

**Subscribe Request:**  **订阅请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**Update Notification:**  **更新通知：**

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

## Message Flow  ## 消息流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client,Server: Resource Discovery
    Client->>Server: resources/list
    Server-->>Client: List of resources
客户端，服务器：资源发现客户端->>服务器：resources/list 服务器-->>客户端：资源列表

    Note over Client,Server: Resource Access
    Client->>Server: resources/read
    Server-->>Client: Resource contents
客户端，服务器：资源访问客户端>>>服务器：资源/读取服务器-->>客户端：资源内容

    Note over Client,Server: Subscriptions
    Client->>Server: resources/subscribe
    Server-->>Client: Subscription confirmed
客户端，服务器：订阅 客户端->>服务器：resources/subscribe 服务器-->>客户端：订阅确认

    Note over Client,Server: Updates
    Server--)Client: notifications/resources/updated
    Client->>Server: resources/read
    Server-->>Client: Updated contents
```
客户端，服务器：更新 服务器--)客户端：notifications/resources/updated 客户端->>服务器：resources/read 服务器-->>客户端：更新内容

## Data Types  数据类型

### Resource  资源

A resource definition includes:
资源定义包括：

* `uri`: Unique identifier for the resource
* `name`: Human-readable name
* `description`: Optional description
* `mimeType`: Optional MIME type
* `uri`：资源的唯一标识符 * `name`：可读性名称 * `description`：可选描述 * `mimeType`：可选 MIME 类型

### Resource Contents  ### 资源内容

Resources can contain either text or binary data:
资源可以包含文本或二进制数据：

#### Text Content  #### 文本内容

```json
{
  "uri": "file:///example.txt",
  "mimeType": "text/plain",
  "text": "Resource content"
}
```
```json { "uri": "file:///example.txt", "mimeType": "text/plain", "text": "资源内容" } ```

#### Binary Content  #### 二进制内容

```json
{
  "uri": "file:///example.png",
  "mimeType": "image/png",
  "blob": "base64-encoded-data"
}
```
```json { "uri": "file:///example.png", "mimeType": "image/png", "blob": "base64 编码数据" } ```

## Common URI Schemes  常见 URI 方案

The protocol defines several standard URI schemes. This list not
exhaustive—implementations are always free to use additional, custom URI schemes.
协议定义了多个标准 URI 方案。此列表并不全面——实现者始终可以自由使用额外的、自定义的 URI 方案。

### https\://  ### https://

Used to represent a resource available on the web.
用于表示网络上可用的资源。

Servers **SHOULD** use this scheme only when the client is able to fetch and load the
resource directly from the web on its own—that is, it doesn’t need to read the resource
via the MCP server.
服务器**应**仅当客户端能够独立从网络获取并加载资源时才使用此方案——也就是说，它不需要通过 MCP 服务器读取资源。

For other use cases, servers **SHOULD** prefer to use another URI scheme, or define a
custom one, even if the server will itself be downloading resource contents over the
internet.
对于其他用例，服务器**应**优先使用其他 URI 方案，或者定义一个自定义方案，即使服务器本身会从互联网下载资源内容。

### file://

Used to identify resources that behave like a filesystem. However, the resources do not
need to map to an actual physical filesystem.
用于标识类似文件系统的资源。然而，这些资源不需要映射到实际的物理文件系统。

MCP servers **MAY** identify file:// resources with an
[XDG MIME type](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14),
like `inode/directory`, to represent non-regular files (such as directories) that don’t
otherwise have a standard MIME type.
MCP 服务器**可能**使用[XDG MIME 类型](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14)来标识 file://资源，例如`inode/directory`，以表示那些没有标准 MIME 类型的非常规文件（如目录）。

### git://

Git version control integration.
Git 版本控制集成。

## Error Handling  ## 错误处理

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:
服务器 **应当** 返回标准 JSON-RPC 错误以处理常见的失败情况：

* Resource not found: `-32002`
* Internal errors: `-32603`
* 资源未找到：`-32002` * 内部错误：`-32603`

Example error:  示例错误：

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "error": {
    "code": -32002,
    "message": "Resource not found",
    "data": {
      "uri": "file:///nonexistent.txt"
    }
  }
}
```

## Security Considerations
安全注意事项

1. Servers **MUST** validate all resource URIs
2. Access controls **SHOULD** be implemented for sensitive resources
3. Binary data **MUST** be properly encoded
4. Resource permissions **SHOULD** be checked before operations
1. 服务器 **必须** 验证所有资源 URI 2. 对于敏感资源，**应当** 实施访问控制 3. 二进制数据 **必须** 正确编码 4. 在操作之前，**应当** 检查资源权限


# Tools
Source: https://modelcontextprotocol.io/specification/2024-11-05/server/tools
# 工具来源: https://modelcontextprotocol.io/specification/2024-11-05/server/tools



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**: 2024-11-05

The Model Context Protocol (MCP) allows servers to expose tools that can be invoked by
language models. Tools enable models to interact with external systems, such as querying
databases, calling APIs, or performing computations. Each tool is uniquely identified by
a name and includes metadata describing its schema.
模型上下文协议（MCP）允许服务器暴露可以被语言模型调用的工具。工具使模型能够与外部系统交互，例如查询数据库、调用 API 或执行计算。每个工具都由一个名称唯一标识，并包括描述其模式的元数据。

## User Interaction Model
用户交互模型

Tools in MCP are designed to be **model-controlled**, meaning that the language model can
discover and invoke tools automatically based on its contextual understanding and the
user's prompts.
MCP 中的工具设计为**模型控制**，这意味着语言模型可以根据其上下文理解和用户的提示自动发现和调用工具。

However, implementations are free to expose tools through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.
然而，实现者可以自由选择任何适合他们需求的接口模式来公开工具——协议本身并不强制任何特定的用户交互模型。

<Warning>
  For trust & safety and security, there **SHOULD** always
  be a human in the loop with the ability to deny tool invocations.
<警告>为了信任与安全以及安全起见，**应当**始终有人在场，并具有拒绝工具调用的能力。

  Applications **SHOULD**:
应用程序 **应当**：

  * Provide UI that makes clear which tools are being exposed to the AI model
  * Insert clear visual indicators when tools are invoked
  * Present confirmation prompts to the user for operations, to ensure a human is in the
    loop
</Warning>
* 提供清晰的用户界面，以表明哪些工具被暴露给 AI 模型 * 在工具被调用时插入清晰的视觉指示器 * 对用户操作进行确认提示，以确保人类在循环中

## Capabilities  ## 功能

Servers that support tools **MUST** declare the `tools` capability:
支持工具的服务器 **必须** 声明 `tools` 功能：

```json
{
  "capabilities": {
    "tools": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the server will emit notifications when the list of
available tools changes.
`listChanged` 表示服务器是否会在可用工具列表发生变化时发出通知。

## Protocol Messages  ## 协议消息

### Listing Tools  ### 工具列表

To discover available tools, clients send a `tools/list` request. This operation supports
[pagination](/specification/2024-11-05/server/utilities/pagination).
为了发现可用的工具，客户端发送一个 `tools/list` 请求。此操作支持[分页](/specification/2024-11-05/server/utilities/pagination)。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "description": "Get current weather information for a location",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "City name or zip code"
            }
          },
          "required": ["location"]
        }
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "result": { "tools": [ { "name": "get_weather", "description": "获取当前位置的天气信息", "inputSchema": { "type": "object", "properties": { "location": { "type": "string", "description": "城市名称或邮编" } }, "required": ["location"] } } ], "nextCursor": "next-page-cursor" } } ```

### Calling Tools  ### 调用工具

To invoke a tool, clients send a `tools/call` request:
要调用工具，客户端发送 `tools/call` 请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "New York"
    }
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Current weather in New York:\nTemperature: 72°F\nConditions: Partly cloudy"
      }
    ],
    "isError": false
  }
}
```

### List Changed Notification
### 列表变更通知

When the list of available tools changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:
当可用工具列表发生变化时，声明了 `listChanged` 功能的服务器 **应当** 发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}
```

## Message Flow  ## 消息流程

```mermaid
sequenceDiagram
    participant LLM
    participant Client
    participant Server
```mermaid sequenceDiagram participant LLM participant 客户端 participant 服务器

    Note over Client,Server: Discovery
    Client->>Server: tools/list
    Server-->>Client: List of tools
客户端、服务器：发现 客户端->>服务器：工具列表 服务器-->>客户端：工具列表

    Note over Client,LLM: Tool Selection
    LLM->>Client: Select tool to use
客户端，LLM：工具选择 LLM->>客户端：选择要使用的工具

    Note over Client,Server: Invocation
    Client->>Server: tools/call
    Server-->>Client: Tool result
    Client->>LLM: Process result
客户端、服务器：调用 客户端->>服务器：工具调用 服务器-->>客户端：工具结果 客户端->>LLM：处理结果

    Note over Client,Server: Updates
    Server--)Client: tools/list_changed
    Client->>Server: tools/list
    Server-->>Client: Updated tools
```
客户端、服务器：更新 服务器--)客户端：工具变更列表 客户端->>服务器：工具列表 服务器-->>客户端：更新后的工具列表

## Data Types  数据类型

### Tool  工具

A tool definition includes:
工具定义包括：

* `name`: Unique identifier for the tool
* `description`: Human-readable description of functionality
* `inputSchema`: JSON Schema defining expected parameters
* `name`: 工具的唯一标识符 * `description`: 功能的可读描述 * `inputSchema`: 定义预期参数的 JSON Schema

### Tool Result  ### 工具结果

Tool results can contain multiple content items of different types:
工具结果可以包含多种类型的内容项：

#### Text Content  #### 文本内容

```json
{
  "type": "text",
  "text": "Tool result text"
}
```
```json { "type": "text", "text": "工具结果文本" } ```

#### Image Content  图像内容

```json
{
  "type": "image",
  "data": "base64-encoded-data",
  "mimeType": "image/png"
}
```

#### Embedded Resources  #### 嵌入资源

[Resources](/specification/2024-11-05/server/resources) **MAY** be
embedded, to provide additional context or data, behind a URI that can be subscribed to
or fetched again by the client later:
[资源](/specification/2024-11-05/server/resources) **可以**嵌入，以提供额外的上下文或数据，在客户端可以订阅或稍后再次获取的 URI 之后：

```json
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "Resource content"
  }
}
```
```json { "type": "resource", "resource": { "uri": "resource://example", "mimeType": "text/plain", "text": "资源内容" } } ```

## Error Handling  错误处理

Tools use two error reporting mechanisms:
工具使用两种错误报告机制：

1. **Protocol Errors**: Standard JSON-RPC errors for issues like:
1. **协议错误**：标准 JSON-RPC 错误，例如：

   * Unknown tools
   * Invalid arguments
   * Server errors
* 未知工具 * 无效参数 * 服务器错误

2. **Tool Execution Errors**: Reported in tool results with `isError: true`:
   * API failures
   * Invalid input data
   * Business logic errors
**工具执行错误**：在工具结果中报告，`isError: true`：* API 故障 * 无效输入数据 * 业务逻辑错误

Example protocol error:  示例协议错误：

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "error": {
    "code": -32602,
    "message": "Unknown tool: invalid_tool_name"
  }
}
```
```json { "jsonrpc": "2.0", "id": 3, "error": { "code": -32602, "message": "未知工具：invalid_tool_name" } } ```

Example tool execution error:
示例工具执行错误：

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Failed to fetch weather data: API rate limit exceeded"
      }
    ],
    "isError": true
  }
}
```

## Security Considerations
安全注意事项

1. Servers **MUST**:  1. 服务器 **必须**：

   * Validate all tool inputs
   * Implement proper access controls
   * Rate limit tool invocations
   * Sanitize tool outputs
* 验证所有工具输入 * 实施适当的访问控制 * 限制工具调用频率 * 清理工具输出

2. Clients **SHOULD**:
   * Prompt for user confirmation on sensitive operations
   * Show tool inputs to the user before calling the server, to avoid malicious or
     accidental data exfiltration
   * Validate tool results before passing to LLM
   * Implement timeouts for tool calls
   * Log tool usage for audit purposes
2. 客户端 **应该**： * 在敏感操作前提示用户确认 * 在调用服务器前向用户展示工具输入，以避免恶意或意外数据泄露 * 在传递给 LLM 之前验证工具结果 * 实施工具调用的超时机制 * 记录工具使用情况以供审计


# Completion
Source: https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/completion
# 完成源：https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/completion



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**: 2024-11-05

The Model Context Protocol (MCP) provides a standardized way for servers to offer
argument autocompletion suggestions for prompts and resource URIs. This enables rich,
IDE-like experiences where users receive contextual suggestions while entering argument
values.
模型上下文协议（MCP）为服务器提供了一种标准化的方式，以便为提示和资源 URI 提供参数自动补全建议。这使用户在输入参数值时能够获得丰富的、类似 IDE 的体验。

## User Interaction Model
## 用户交互模型

Completion in MCP is designed to support interactive user experiences similar to IDE code
completion.
MCP 中的完成功能旨在支持类似于 IDE 代码补全的交互式用户体验。

For example, applications may show completion suggestions in a dropdown or popup menu as
users type, with the ability to filter and select from available options.
例如，应用程序可以在用户输入时显示下拉菜单或弹出菜单中的完成建议，并能够过滤和选择可用选项。

However, implementations are free to expose completion through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.
然而，实现者可以自由选择任何适合他们需求的用户界面模式来展示完成功能——协议本身并不强制任何特定的用户交互模型。

## Protocol Messages  ## 协议消息

### Requesting Completions
### 请求补全

To get completion suggestions, clients send a `completion/complete` request specifying
what is being completed through a reference type:
要获取补全建议，客户端发送一个指定通过引用类型进行补全的 `completion/complete` 请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "completion/complete",
  "params": {
    "ref": {
      "type": "ref/prompt",
      "name": "code_review"
    },
    "argument": {
      "name": "language",
      "value": "py"
    }
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "completion": {
      "values": ["python", "pytorch", "pyside"],
      "total": 10,
      "hasMore": true
    }
  }
}
```

### Reference Types  ### 参考类型

The protocol supports two types of completion references:
该协议支持两种完成引用类型：

| Type           | Description                 | Example                                             |
| -------------- | --------------------------- | --------------------------------------------------- |
| `ref/prompt`   | References a prompt by name | `{"type": "ref/prompt", "name": "code_review"}`     |
| `ref/resource` | References a resource URI   | `{"type": "ref/resource", "uri": "file:///{path}"}` |
| Type | 描述 | 示例 | | -------------- | --------------------------- | --------------------------------------------------- | | `ref/prompt` | 通过名称引用提示 | `{"type": "ref/prompt", "name": "code_review"}` | | `ref/resource` | 引用资源 URI | `{"type": "ref/resource", "uri": "file:///{path}"}` |

### Completion Results  ### 完成结果

Servers return an array of completion values ranked by relevance, with:
服务器返回一个按相关性排序的完成值数组，包括：

* Maximum 100 items per response
* Optional total number of available matches
* Boolean indicating if additional results exist
* 每个响应最多 100 个项目 * 可选的总匹配数 * 表示是否存在更多结果的布尔值

## Message Flow  ## 消息流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client: User types argument
    Client->>Server: completion/complete
    Server-->>Client: Completion suggestions
注意：客户端：用户输入参数 客户端->>服务器：完成/complete 服务器-->>客户端：完成建议

    Note over Client: User continues typing
    Client->>Server: completion/complete
    Server-->>Client: Refined suggestions
```
注意：客户端：用户继续输入 客户端->>服务器：完成/complete 服务器-->>客户端：细化建议 ```

## Data Types  ## 数据类型

### CompleteRequest  ### 完成请求

* `ref`: A `PromptReference` or `ResourceReference`
* `argument`: Object containing:
  * `name`: Argument name
  * `value`: Current value
* `ref`: 一个 `提示引用` 或 `资源引用` * `argument`: 包含以下内容的对象: * `name`: 参数名称 * `value`: 当前值

### CompleteResult  ### 完成结果

* `completion`: Object containing:
  * `values`: Array of suggestions (max 100)
  * `total`: Optional total matches
  * `hasMore`: Additional results flag
* `completion`: 包含以下内容的对象: * `values`: 最大 100 个建议的数组 * `total`: 可选的总匹配数 * `hasMore`: 额外结果标志

## Implementation Considerations
## 实施注意事项

1. Servers **SHOULD**:  1. 服务器 **应当**：

   * Return suggestions sorted by relevance
   * Implement fuzzy matching where appropriate
   * Rate limit completion requests
   * Validate all inputs
* 按相关性排序返回建议 * 在适当的情况下实现模糊匹配 * 限制完成请求的速率 * 验证所有输入

2. Clients **SHOULD**:
   * Debounce rapid completion requests
   * Cache completion results where appropriate
   * Handle missing or partial results gracefully
2. 客户端 **应当**： * 防抖快速完成请求 * 在适当的情况下缓存完成结果 * 优雅地处理缺失或部分结果

## Security  ## 安全

Implementations **MUST**:
实现必须：

* Validate all completion inputs
* Implement appropriate rate limiting
* Control access to sensitive suggestions
* Prevent completion-based information disclosure
*验证所有完成输入* 实施适当的速率限制*控制对敏感建议的访问*防止基于完成的情报泄露


# Logging
Source: https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/logging
#日志来源: https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/logging



<Info>**Protocol Revision**: 2024-11-05</Info>
**协议版本**: 2024-11-05

The Model Context Protocol (MCP) provides a standardized way for servers to send
structured log messages to clients. Clients can control logging verbosity by setting
minimum log levels, with servers sending notifications containing severity levels,
optional logger names, and arbitrary JSON-serializable data.
模型上下文协议（MCP）为服务器向客户端发送结构化日志消息提供了一种标准化方式。客户端可以通过设置最小日志级别来控制日志详细程度，服务器发送包含严重级别、可选的记录器名称和任意可序列化为 JSON 的数据的通知。

## User Interaction Model
## 用户交互模型

Implementations are free to expose logging through any interface pattern that suits their
needs—the protocol itself does not mandate any specific user interaction model.
实现可以自由选择通过任何适合其需求的接口模式来公开日志记录——协议本身并不强制任何特定的用户交互模型。

## Capabilities  ## 功能

Servers that emit log message notifications **MUST** declare the `logging` capability:
发出日志消息通知的服务器 **必须** 声明 `logging` 功能：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

## Log Levels  ## 日志级别

The protocol follows the standard syslog severity levels specified in
[RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1):
该协议遵循[RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1)中指定的标准 syslog 严重性级别：

| Level     | Description                      | Example Use Case           |
| --------- | -------------------------------- | -------------------------- |
| debug     | Detailed debugging information   | Function entry/exit points |
| info      | General informational messages   | Operation progress updates |
| notice    | Normal but significant events    | Configuration changes      |
| warning   | Warning conditions               | Deprecated feature usage   |
| error     | Error conditions                 | Operation failures         |
| critical  | Critical conditions              | System component failures  |
| alert     | Action must be taken immediately | Data corruption detected   |
| emergency | System is unusable               | Complete system failure    |
| 级别 | 描述 | 示例用例 |
    | --------- | -------------------------------- | -------------------------- |
    | debug | 详细调试信息 | 函数入口/退出点 |
    | info | 一般信息性消息 | 操作进度更新 |
    | notice | 正常但重要的事件 | 配置更改 |
    | warning | 警告条件 | 已弃用功能使用 |
    | error | 错误条件 | 操作失败 |
    | critical | 临界条件 | 系统组件故障 |
    | alert | 立即采取行动 | 数据损坏检测 |
    | emergency | 系统不可用 | 完全系统故障 |

## Protocol Messages  ## 协议消息

### Setting Log Level  ### 设置日志级别

To configure the minimum log level, clients **MAY** send a `logging/setLevel` request:
要配置最小日志级别，客户端**可以**发送一个`logging/setLevel`请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "logging/setLevel",
  "params": {
    "level": "info"
  }
}
```

### Log Message Notifications
### 日志消息通知

Servers send log messages using `notifications/message` notifications:
服务器使用 `notifications/message` 通知发送日志消息：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/message",
  "params": {
    "level": "error",
    "logger": "database",
    "data": {
      "error": "Connection failed",
      "details": {
        "host": "localhost",
        "port": 5432
      }
    }
  }
}
```
```json { "jsonrpc": "2.0", "method": "notifications/message", "params": { "level": "error", "logger": "database", "data": { "error": "连接失败", "details": { "host": "localhost", "port": 5432 } } } } ```

## Message Flow  ## 消息流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client,Server: Configure Logging
    Client->>Server: logging/setLevel (info)
    Server-->>Client: Empty Result
客户端，服务器：配置日志 客户端->>服务器：logging/setLevel (info) 服务器-->>客户端：空结果

    Note over Client,Server: Server Activity
    Server--)Client: notifications/message (info)
    Server--)Client: notifications/message (warning)
    Server--)Client: notifications/message (error)
客户端，服务器：服务器活动 服务器--)客户端：notifications/message (info) 服务器--)客户端：notifications/message (warning) 服务器--)客户端：notifications/message (error)

    Note over Client,Server: Level Change
    Client->>Server: logging/setLevel (error)
    Server-->>Client: Empty Result
    Note over Server: Only sends error level<br/>and above
```
客户端，服务器：级别变更 客户端->>服务器：logging/setLevel (error) 服务器-->>客户端：空结果 服务器：仅发送错误级别及以上 ```

## Error Handling  ## 错误处理

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:
服务器 **应当** 返回标准 JSON-RPC 错误以处理常见失败情况：

* Invalid log level: `-32602` (Invalid params)
* Configuration errors: `-32603` (Internal error)
* 无效日志级别：`-32602`（无效参数）* 配置错误：`-32603`（内部错误）

## Implementation Considerations
## 实施注意事项

1. Servers **SHOULD**:  1. 服务器 **应当**：

   * Rate limit log messages
   * Include relevant context in data field
   * Use consistent logger names
   * Remove sensitive information
* 限制速率的日志消息 * 在数据字段中包含相关上下文 * 使用一致的日志记录器名称 * 删除敏感信息

2. Clients **MAY**:
   * Present log messages in the UI
   * Implement log filtering/search
   * Display severity visually
   * Persist log messages
2. 客户**可以**：* 在 UI 中显示日志消息 * 实现日志过滤/搜索 * 可视化显示严重性 * 持久化日志消息

## Security  ## 安全

1. Log messages **MUST NOT** contain:
1. 日志消息**不得**包含：

   * Credentials or secrets
   * Personal identifying information
   * Internal system details that could aid attacks
凭证或机密 * 个人身份信息 * 可能帮助攻击的内部系统细节

2. Implementations **SHOULD**:
   * Rate limit messages
   * Validate all data fields
   * Control log access
   * Monitor for sensitive content
应当：* 限制消息速率 * 验证所有数据字段 * 控制日志访问 * 监测敏感内容


# Pagination
Source: https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/pagination
# 分页来源：https://modelcontextprotocol.io/specification/2024-11-05/server/utilities/pagination



<Info>**Protocol Revision**: 2024-11-05</Info>
<信息>**协议版本**：2024-11-05

The Model Context Protocol (MCP) supports paginating list operations that may return
large result sets. Pagination allows servers to yield results in smaller chunks rather
than all at once.
模型上下文协议（MCP）支持分页列表操作，可能返回大量结果集。分页允许服务器分批次返回结果，而不是一次性返回所有结果。

Pagination is especially important when connecting to external services over the
internet, but also useful for local integrations to avoid performance issues with large
data sets.
分页在连接互联网上的外部服务时尤为重要，但对于避免大型数据集的性能问题，在本地集成中也非常有用。

## Pagination Model  ## 分页模型

Pagination in MCP uses an opaque cursor-based approach, instead of numbered pages.
MCP 中的分页使用基于不可见游标的策略，而不是编号的页面。

* The **cursor** is an opaque string token, representing a position in the result set
* **Page size** is determined by the server, and clients **MUST NOT** assume a fixed page
  size
* **游标**是一个不可见的字符串令牌，表示结果集中的位置 * **页面大小**由服务器确定，客户端**不得**假设页面大小固定

## Response Format  响应格式

Pagination starts when the server sends a **response** that includes:
分页从服务器发送包含以下内容的**响应**开始：

* The current page of results
* An optional `nextCursor` field if more results exist
* 当前结果页 * 如果存在更多结果，则可选的 `nextCursor` 字段

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {
    "resources": [...],
    "nextCursor": "eyJwYWdlIjogM30="
  }
}
```

## Request Format  请求格式

After receiving a cursor, the client can *continue* paginating by issuing a request
including that cursor:
接收到游标后，客户端可以通过发送包含该游标的请求来 *继续* 分页：

```json
{
  "jsonrpc": "2.0",
  "method": "resources/list",
  "params": {
    "cursor": "eyJwYWdlIjogMn0="
  }
}
```

## Pagination Flow  ## 分页流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Client->>Server: List Request (no cursor)
    loop Pagination Loop
      Server-->>Client: Page of results + nextCursor
      Client->>Server: List Request (with cursor)
    end
```
客户端->服务器：列表请求（无游标）循环 分页循环 服务器-->>客户端：结果页 + 下一个游标 客户端->服务器：列表请求（带有游标）结束 ```

## Operations Supporting Pagination
支持分页操作

The following MCP operations support pagination:
以下 MCP 操作支持分页：

* `resources/list` - List available resources
* `resources/templates/list` - List resource templates
* `prompts/list` - List available prompts
* `tools/list` - List available tools
* `resources/list` - 列出可用资源 * `resources/templates/list` - 列出资源模板 * `prompts/list` - 列出可用提示 * `tools/list` - 列出可用工具

## Implementation Guidelines
## 实施指南

1. Servers **SHOULD**:  1. 服务器 **应当**：

   * Provide stable cursors
   * Handle invalid cursors gracefully
* 提供稳定的游标 * 优雅地处理无效的游标

2. Clients **SHOULD**:  2. 客户端 **应当**：

   * Treat a missing `nextCursor` as the end of results
   * Support both paginated and non-paginated flows
* 将缺失的 `nextCursor` 视为结果结束 * 支持分页和非分页流程

3. Clients **MUST** treat cursors as opaque tokens:
   * Don't make assumptions about cursor format
   * Don't attempt to parse or modify cursors
   * Don't persist cursors across sessions
客户 **必须** 将游标视为不透明令牌：* 不要对游标格式做出假设 * 不要尝试解析或修改游标 * 不要在会话之间持久化游标

## Error Handling  错误处理

Invalid cursors **SHOULD** result in an error with code -32602 (Invalid params).
无效的游标 **应** 导致代码为 -32602 的错误（无效参数）。


# Architecture
Source: https://modelcontextprotocol.io/specification/2025-03-26/architecture/index
# 架构来源：https://modelcontextprotocol.io/specification/2025-03-26/architecture/index



The Model Context Protocol (MCP) follows a client-host-server architecture where each
host can run multiple client instances. This architecture enables users to integrate AI
capabilities across applications while maintaining clear security boundaries and
isolating concerns. Built on JSON-RPC, MCP provides a stateful session protocol focused
on context exchange and sampling coordination between clients and servers.
模型上下文协议（MCP）遵循客户端-主机-服务器架构，其中每个主机可以运行多个客户端实例。这种架构使用户能够在保持清晰的安全边界和隔离关注点的同时，将 AI 能力集成到各个应用程序中。基于 JSON-RPC 构建的 MCP 提供了一种面向客户端和服务器之间上下文交换和采样协调的有状态会话协议。

## Core Components  核心组件

```mermaid
graph LR
    subgraph "Application Host Process"
        H[Host]
        C1[Client 1]
        C2[Client 2]
        C3[Client 3]
        H --> C1
        H --> C2
        H --> C3
    end
```mermaid graph LR subgraph "应用主机进程" H[主机] C1[客户端 1] C2[客户端 2] C3[客户端 3] H --> C1 H --> C2 H --> C3 end

    subgraph "Local machine"
        S1[Server 1<br>Files & Git]
        S2[Server 2<br>Database]
        R1[("Local<br>Resource A")]
        R2[("Local<br>Resource B")]
本地机器子图"S1[服务器 1
文件 & Git] S2[服务器 2
数据库] R1[("本地
资源 A")] R2[("本地
资源 B")]"

        C1 --> S1
        C2 --> S2
        S1 <--> R1
        S2 <--> R2
    end
C1 --> S1 C2 --> S2 S1 <--> R1 S2 <--> R2 结束

    subgraph "Internet"
        S3[Server 3<br>External APIs]
        R3[("Remote<br>Resource C")]
subgraph "互联网" S3[服务器 3
外部 API] R3[("远程
资源 C")]

        C3 --> S3
        S3 <--> R3
    end
```
C3 --> S3 S3 <--> R3 结束 ```

### Host  ### 主机

The host process acts as the container and coordinator:
主进程作为容器和协调者：

* Creates and manages multiple client instances
* Controls client connection permissions and lifecycle
* Enforces security policies and consent requirements
* Handles user authorization decisions
* Coordinates AI/LLM integration and sampling
* Manages context aggregation across clients
* 创建和管理多个客户端实例 * 控制客户端连接权限和生命周期 * 强制执行安全策略和同意要求 * 处理用户授权决策 * 协调 AI/LLM 集成和采样 * 管理跨客户端的上下文聚合

### Clients  ### 客户端

Each client is created by the host and maintains an isolated server connection:
每个客户端由主机创建并维护一个独立的服务器连接：

* Establishes one stateful session per server
* Handles protocol negotiation and capability exchange
* Routes protocol messages bidirectionally
* Manages subscriptions and notifications
* Maintains security boundaries between servers
建立每个服务器的一个状态会话 * 处理协议协商和能力交换 * 双向路由协议消息 * 管理订阅和通知 * 维护服务器之间的安全边界

A host application creates and manages multiple clients, with each client having a 1:1
relationship with a particular server.
主应用程序创建并管理多个客户端，每个客户端与特定服务器具有一对一的关系。

### Servers  ### 服务器

Servers provide specialized context and capabilities:
服务器提供专业化的上下文和能力：

* Expose resources, tools and prompts via MCP primitives
* Operate independently with focused responsibilities
* Request sampling through client interfaces
* Must respect security constraints
* Can be local processes or remote services
公开资源、工具和提示通过 MCP 原语* 独立操作，承担专注的责任* 通过客户端接口请求采样* 必须遵守安全限制* 可以为本地进程或远程服务

## Design Principles  ## 设计原则

MCP is built on several key design principles that inform its architecture and
implementation:
MCP 构建在多个关键设计原则之上，这些原则指导了其架构和实现：

1. **Servers should be extremely easy to build**
1. **服务器应极其易于构建**

   * Host applications handle complex orchestration responsibilities
   * Servers focus on specific, well-defined capabilities
   * Simple interfaces minimize implementation overhead
   * Clear separation enables maintainable code
* 宿主应用处理复杂的编排任务 * 服务器专注于特定、定义明确的职能 * 简单的接口最小化实现开销 * 清晰的分离使代码易于维护

2. **Servers should be highly composable**
2. **服务器应高度可组合**

   * Each server provides focused functionality in isolation
   * Multiple servers can be combined seamlessly
   * Shared protocol enables interoperability
   * Modular design supports extensibility
每个服务器都提供独立的专注功能 * 多个服务器可以无缝结合 * 共享协议实现互操作性 * 模块化设计支持可扩展性

3. **Servers should not be able to read the whole conversation, nor "see into" other
   servers**
3. **服务器不应能够读取整个对话，也不应“窥视”其他服务器**

   * Servers receive only necessary contextual information
   * Full conversation history stays with the host
   * Each server connection maintains isolation
   * Cross-server interactions are controlled by the host
   * Host process enforces security boundaries
服务器仅接收必要上下文信息 * 完整对话历史保留在主机端 * 每个服务器连接保持隔离 * 服务器间交互由主机控制 * 主机进程强制执行安全边界

4. **Features can be added to servers and clients progressively**
   * Core protocol provides minimal required functionality
   * Additional capabilities can be negotiated as needed
   * Servers and clients evolve independently
   * Protocol designed for future extensibility
   * Backwards compatibility is maintained
4. **功能可以逐步添加到服务器和客户端** * 核心协议提供最小必需的功能 * 根据需要协商附加功能 * 服务器和客户端独立发展 * 协议设计用于未来扩展 * 保持向后兼容性

## Capability Negotiation
能力协商

The Model Context Protocol uses a capability-based negotiation system where clients and
servers explicitly declare their supported features during initialization. Capabilities
determine which protocol features and primitives are available during a session.
模型上下文协议使用基于能力协商的系统，客户端和服务器在初始化期间明确声明它们支持的功能。能力决定了会话期间可用的协议功能和原语。

* Servers declare capabilities like resource subscriptions, tool support, and prompt
  templates
* Clients declare capabilities like sampling support and notification handling
* Both parties must respect declared capabilities throughout the session
* Additional capabilities can be negotiated through extensions to the protocol
* 服务器声明的能力包括资源订阅、工具支持和提示模板 * 客户端声明的能力包括采样支持和通知处理 * 双方必须在整个会话中尊重声明的能力 * 可以通过协议的扩展协商额外的能力

```mermaid
sequenceDiagram
    participant Host
    participant Client
    participant Server
```mermaid 序列图参与者 主机 参与者 客户端 参与者 服务器

    Host->>+Client: Initialize client
    Client->>+Server: Initialize session with capabilities
    Server-->>Client: Respond with supported capabilities
主机->>客户端：初始化客户端 客户端->>服务器：初始化具有功能特性的会话 服务器-->>客户端：响应支持的功能特性

    Note over Host,Server: Active Session with Negotiated Features
主机，服务器：具有协商功能的活跃会话

    loop Client Requests
        Host->>Client: User- or model-initiated action
        Client->>Server: Request (tools/resources)
        Server-->>Client: Response
        Client-->>Host: Update UI or respond to model
    end
循环客户端请求 主->>客户端：用户或模型触发的操作 客户端->>服务器：请求（工具/资源） 服务器-->>客户端：响应 客户端-->>主机：更新 UI 或响应模型结束

    loop Server Requests
        Server->>Client: Request (sampling)
        Client->>Host: Forward to AI
        Host-->>Client: AI response
        Client-->>Server: Response
    end
循环服务器请求 服务器->>客户端：请求（采样） 客户端->>主机：转发给 AI 主机-->>客户端：AI 响应 客户端->>服务器：响应结束

    loop Notifications
        Server--)Client: Resource updates
        Client--)Server: Status changes
    end
循环通知服务器--客户端：资源更新客户端--服务器：状态变更结束

    Host->>Client: Terminate
    Client->>-Server: End session
    deactivate Server
```
主机->>客户端：终止 客户端->>-服务器：结束会话，停用服务器

Each capability unlocks specific protocol features for use during the session. For
example:
每个功能解锁会话期间使用的特定协议功能。例如：

* Implemented [server features](/specification/2025-03-26/server) must be advertised in the
  server's capabilities
* Emitting resource subscription notifications requires the server to declare
  subscription support
* Tool invocation requires the server to declare tool capabilities
* [Sampling](/specification/2025-03-26/client) requires the client to declare support in its
  capabilities
* 实现的 [服务器功能](/specification/2025-03-26/server) 必须在服务器的能力中宣传 * 发出资源订阅通知需要服务器声明支持订阅 * 工具调用需要服务器声明工具能力 * [采样](/specification/2025-03-26/client) 需要客户端在其能力中声明支持

This capability negotiation ensures clients and servers have a clear understanding of
supported functionality while maintaining protocol extensibility.
这种能力协商确保客户端和服务器对支持的功能有清晰的理解，同时保持协议的可扩展性。


# Authorization
Source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization
# 授权来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization



<Info>**Protocol Revision**: 2025-03-26</Info>
**协议版本**：2025-03-26

## 1. Introduction  ## 1. 简介

### 1.1 Purpose and Scope
### 1.1 目的和范围

The Model Context Protocol provides authorization capabilities at the transport level,
enabling MCP clients to make requests to restricted MCP servers on behalf of resource
owners. This specification defines the authorization flow for HTTP-based transports.
模型上下文协议在传输层提供授权能力，使 MCP 客户端能够代表资源所有者向受限制的 MCP 服务器发出请求。本规范定义了基于 HTTP 传输的授权流程。

### 1.2 Protocol Requirements
### 1.2 协议要求

Authorization is **OPTIONAL** for MCP implementations. When supported:
授权对于 MCP 实现是**可选的**。当支持时：

* Implementations using an HTTP-based transport **SHOULD** conform to this specification.
* Implementations using an STDIO transport **SHOULD NOT** follow this specification, and
  instead retrieve credentials from the environment.
* Implementations using alternative transports **MUST** follow established security best
  practices for their protocol.
* 使用基于 HTTP 传输的实现**应**符合本规范。* 使用 STDIO 传输的实现**不应**遵循本规范，而应从环境中获取凭证。* 使用其他传输的实现**必须**遵循其协议的既定安全最佳实践。

### 1.3 Standards Compliance
### 1.3 标准合规性

This authorization mechanism is based on established specifications listed below, but
implements a selected subset of their features to ensure security and interoperability
while maintaining simplicity:
此授权机制基于以下列出的既定规范，但实现其功能的一个子集以确保安全性和互操作性，同时保持简单：

* [OAuth 2.1 IETF DRAFT](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12)
* OAuth 2.0 Authorization Server Metadata
  ([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414))
* OAuth 2.0 Dynamic Client Registration Protocol
  ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591))
* [OAuth 2.1 IETF 草案](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12) * OAuth 2.0 授权服务器元数据 ([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414)) * OAuth 2.0 动态客户端注册协议 ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591))

## 2. Authorization Flow  ## 2. 授权流程

### 2.1 Overview  ### 2.1 概述

1. MCP auth implementations **MUST** implement OAuth 2.1 with appropriate security
   measures for both confidential and public clients.
1. MCP 授权实现 **必须** 支持 OAuth 2.1，并为保密和公开客户端采取适当的安全措施。

2. MCP auth implementations **SHOULD** support the OAuth 2.0 Dynamic Client Registration
   Protocol ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591)).
2. MCP 认证实现**应**支持 OAuth 2.0 动态客户端注册协议([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591))。

3. MCP servers **SHOULD** and MCP clients **MUST** implement OAuth 2.0 Authorization
   Server Metadata ([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414)). Servers
   that do not support Authorization Server Metadata **MUST** follow the default URI
   schema.
3. MCP 服务器**应**和 MCP 客户端**必须**实现 OAuth 2.0 授权服务器元数据([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414))。不支持授权服务器元数据的服务器**必须**遵循默认 URI 模式。

### 2.1.1 OAuth Grant Types
### 2.1.1 OAuth 授权类型

OAuth specifies different flows or grant types, which are different ways of obtaining an
access token. Each of these targets different use cases and scenarios.
OAuth 指定了不同的流程或授权类型，这些是获取访问令牌的不同方式。每种类型都针对不同的用例和场景。

MCP servers **SHOULD** support the OAuth grant types that best align with the intended
audience. For instance:
MCP 服务器**应**支持与目标受众最匹配的 OAuth 授权类型。例如：

1. Authorization Code: useful when the client is acting on behalf of a (human) end user.
   * For instance, an agent calls an MCP tool implemented by a SaaS system.
2. Client Credentials: the client is another application (not a human)
   * For instance, an agent calls a secure MCP tool to check inventory at a specific
     store. No need to impersonate the end user.
1. 授权码：当客户端代表（人类）最终用户操作时很有用。* 例如，一个代理调用由 SaaS 系统实现的 MCP 工具。2. 客户端凭证：客户端是另一个应用程序（不是人类）* 例如，一个代理调用一个安全的 MCP 工具来检查特定商店的库存。无需代表最终用户。

### 2.2 Example: authorization code grant
### 2.2 示例：授权码授权

This demonstrates the OAuth 2.1 flow for the authorization code grant type, used for user
auth.
这演示了用于用户身份验证的授权码授权类型的 OAuth 2.1 流程。

**NOTE**: The following example assumes the MCP server is also functioning as the
authorization server. However, the authorization server may be deployed as its own
distinct service.
**注意**：以下示例假设 MCP 服务器同时作为授权服务器运行。然而，授权服务器也可以作为独立的服务进行部署。

A human user completes the OAuth flow through a web browser, obtaining an access token
that identifies them personally and allows the client to act on their behalf.
人类用户通过网页浏览器完成 OAuth 流程，获取一个代表他们个人的访问令牌，允许客户端代表他们进行操作。

When authorization is required and not yet proven by the client, servers **MUST** respond
with *HTTP 401 Unauthorized*.
当需要授权且客户端尚未证明时，服务器**必须**以*HTTP 401 未授权*响应。

Clients initiate the
[OAuth 2.1 IETF DRAFT](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#name-authorization-code-grant)
authorization flow after receiving the *HTTP 401 Unauthorized*.
客户端在收到 *HTTP 401 未授权* 后启动 [OAuth 2.1 IETF 草案](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#name-authorization-code-grant) 授权流程。

The following demonstrates the basic OAuth 2.1 for public clients using PKCE.
以下演示了使用 PKCE 的基本 OAuth 2.1 公开客户端。

```mermaid
sequenceDiagram
    participant B as User-Agent (Browser)
    participant C as Client
    participant M as MCP Server
```mermaid sequenceDiagram participant B as User-Agent (浏览器) participant C as Client participant M as MCP Server

    C->>M: MCP Request
    M->>C: HTTP 401 Unauthorized
    Note over C: Generate code_verifier and code_challenge
    C->>B: Open browser with authorization URL + code_challenge
    B->>M: GET /authorize
    Note over M: User logs in and authorizes
    M->>B: Redirect to callback URL with auth code
    B->>C: Callback with authorization code
    C->>M: Token Request with code + code_verifier
    M->>C: Access Token (+ Refresh Token)
    C->>M: MCP Request with Access Token
    Note over C,M: Begin standard MCP message exchange
```
C->>M: MCP 请求 M->>C: HTTP 401 未授权 Note over C: 生成 code_verifier 和 code_challenge C->>B: 打开带有授权 URL 和 code_challenge 的浏览器 B->>M: GET /authorize Note over M: 用户登录并授权 M->>B: 重定向到回调 URL 并带有授权码 B->>C: 回调并带有授权码 C->>M: 使用 code 和 code_verifier 的令牌请求 M->>C: 访问令牌（+刷新令牌） C->>M: 使用访问令牌的 MCP 请求 Note over C,M: 开始标准的 MCP 消息交换 ```

### 2.3 Server Metadata Discovery
### 2.3 服务器元数据发现

For server capability discovery:
对于服务器功能发现：

* MCP clients *MUST* follow the OAuth 2.0 Authorization Server Metadata protocol defined
  in [RFC8414](https://datatracker.ietf.org/doc/html/rfc8414).
* MCP server *SHOULD* follow the OAuth 2.0 Authorization Server Metadata protocol.
* MCP servers that do not support the OAuth 2.0 Authorization Server Metadata protocol,
  *MUST* support fallback URLs.
* MCP 客户端必须遵循 RFC8414 中定义的 OAuth 2.0 授权服务器元数据协议。[RFC8414](https://datatracker.ietf.org/doc/html/rfc8414)。* MCP 服务器应遵循 OAuth 2.0 授权服务器元数据协议。* 不支持 OAuth 2.0 授权服务器元数据协议的 MCP 服务器，必须支持回退 URL。

The discovery flow is illustrated below:
以下展示了发现流程：

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server

    C->>S: GET /.well-known/oauth-authorization-server
    alt Discovery Success
        S->>C: 200 OK + Metadata Document
        Note over C: Use endpoints from metadata
    else Discovery Failed
        S->>C: 404 Not Found
        Note over C: Fall back to default endpoints
    end
    Note over C: Continue with authorization flow
```
C->>S: GET /.well-known/oauth-authorization-server alt Discovery Success S->>C: 200 OK + Metadata Document Note over C: 使用元数据中的端点否则 Discovery Failed S->>C: 404 Not Found Note over C: 回退到默认端点 end Note over C: 继续授权流程 ```

#### 2.3.1 Server Metadata Discovery Headers
#### 2.3.1 服务器元数据发现头部

MCP clients *SHOULD* include the header `MCP-Protocol-Version: <protocol-version>` during
Server Metadata Discovery to allow the MCP server to respond based on the MCP protocol
version.
MCP 客户端 *SHOULD* 在服务器元数据发现期间包含头部 `MCP-Protocol-Version: `，以便 MCP 服务器根据 MCP 协议版本进行响应。

For example: `MCP-Protocol-Version: 2024-11-05`
例如：`MCP-协议版本：2024-11-05`

#### 2.3.2 Authorization Base URL
#### 2.3.2 授权基本 URL

The authorization base URL **MUST** be determined from the MCP server URL by discarding
any existing `path` component. For example:
授权基本 URL **必须** 从 MCP 服务器 URL 中确定，通过丢弃任何现有的`路径`组件。例如：

If the MCP server URL is `https://api.example.com/v1/mcp`, then:
如果 MCP 服务器 URL 是`https://api.example.com/v1/mcp`，那么：

* The authorization base URL is `https://api.example.com`
* The metadata endpoint **MUST** be at
  `https://api.example.com/.well-known/oauth-authorization-server`
* 授权基本 URL 为 `https://api.example.com` * 元数据端点 **必须** 位于 `https://api.example.com/.well-known/oauth-authorization-server`

This ensures authorization endpoints are consistently located at the root level of the
domain hosting the MCP server, regardless of any path components in the MCP server URL.
这确保了授权端点始终位于托管 MCP 服务器的域名根级别，无论 MCP 服务器 URL 中包含任何路径组件。

#### 2.3.3 Fallbacks for Servers without Metadata Discovery
#### 2.3.3 服务器无元数据发现时的回退

For servers that do not implement OAuth 2.0 Authorization Server Metadata, clients
**MUST** use the following default endpoint paths relative to the authorization base URL
(as defined in [Section 2.3.2](#232-authorization-base-url)):
对于未实现 OAuth 2.0 授权服务器元数据的服务器，客户端 **必须** 使用以下相对于授权基本 URL（如[第 2.3.2 节](#232-授权基本 URL)中定义）的默认端点路径：

| Endpoint               | Default Path | Description                          |
| ---------------------- | ------------ | ------------------------------------ |
| Authorization Endpoint | /authorize   | Used for authorization requests      |
| Token Endpoint         | /token       | Used for token exchange & refresh    |
| Registration Endpoint  | /register    | Used for dynamic client registration |
| Endpoint | 默认路径 | 描述 | | ---------------------- | ------------ | ------------------------------------ | | 授权端点 | /authorize | 用于授权请求 | | 令牌端点 | /token | 用于令牌交换和刷新 | | 注册端点 | /register | 用于动态客户端注册 |

For example, with an MCP server hosted at `https://api.example.com/v1/mcp`, the default
endpoints would be:
例如，在一个托管在 `https://api.example.com/v1/mcp` 的 MCP 服务器上，默认端点将是：

* `https://api.example.com/authorize`
* `https://api.example.com/token`
* `https://api.example.com/register`

Clients **MUST** first attempt to discover endpoints via the metadata document before
falling back to default paths. When using default paths, all other protocol requirements
remain unchanged.
客户端 **必须** 首先尝试通过元数据文档发现端点，然后再回退到默认路径。在使用默认路径时，所有其他协议要求保持不变。

### 2.4 Dynamic Client Registration
### 2.4 动态客户端注册

MCP clients and servers **SHOULD** support the
[OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591)
to allow MCP clients to obtain OAuth client IDs without user interaction. This provides a
standardized way for clients to automatically register with new servers, which is crucial
for MCP because:
MCP 客户端和服务器 **应当** 支持[OAuth 2.0 动态客户端注册协议](https://datatracker.ietf.org/doc/html/rfc7591)，以便 MCP 客户端无需用户交互即可获取 OAuth 客户端 ID。这为客户端自动注册新服务器提供了一种标准化的方式，这对于 MCP 至关重要，因为：

* Clients cannot know all possible servers in advance
* Manual registration would create friction for users
* It enables seamless connection to new servers
* Servers can implement their own registration policies
* 客户端无法事先知道所有可能的服务器 * 手动注册会给用户带来摩擦 * 它可以实现无缝连接到新服务器 * 服务器可以实施自己的注册策略

Any MCP servers that *do not* support Dynamic Client Registration need to provide
alternative ways to obtain a client ID (and, if applicable, client secret). For one of
these servers, MCP clients will have to either:
任何不支持动态客户端注册的 MCP 服务器需要提供其他方式来获取客户端 ID（以及适用时，客户端密钥）。对于这些服务器之一，MCP 客户端将不得不：

1. Hardcode a client ID (and, if applicable, client secret) specifically for that MCP
   server, or
2. Present a UI to users that allows them to enter these details, after registering an
   OAuth client themselves (e.g., through a configuration interface hosted by the
   server).
1. 为该 MCP 服务器硬编码一个客户端 ID（以及如果适用，客户端密钥），或者 2. 提供一个用户界面，允许用户在注册 OAuth 客户端后（例如，通过服务器托管的配置界面）输入这些详细信息。

### 2.5 Authorization Flow Steps
### 2.5 授权流程步骤

The complete Authorization flow proceeds as follows:
完整的授权流程如下进行：

```mermaid
sequenceDiagram
    participant B as User-Agent (Browser)
    participant C as Client
    participant M as MCP Server
```mermaid sequenceDiagram participant B as User-Agent (浏览器) participant C as Client participant M as MCP Server

    C->>M: GET /.well-known/oauth-authorization-server
    alt Server Supports Discovery
        M->>C: Authorization Server Metadata
    else No Discovery
        M->>C: 404 (Use default endpoints)
    end
C->>M: GET /.well-known/oauth-authorization-server 服务器支持发现 M->>C: 授权服务器元数据否则无发现 M->>C: 404（使用默认端点）结束

    alt Dynamic Client Registration
        C->>M: POST /register
        M->>C: Client Credentials
    end
动态客户端注册 C->>M: POST /register M->>C: 客户端凭据结束

    Note over C: Generate PKCE Parameters
    C->>B: Open browser with authorization URL + code_challenge
    B->>M: Authorization Request
    Note over M: User /authorizes
    M->>B: Redirect to callback with authorization code
    B->>C: Authorization code callback
    C->>M: Token Request + code_verifier
    M->>C: Access Token (+ Refresh Token)
    C->>M: API Requests with Access Token
```
注意 C: 生成 PKCE 参数 C->>B: 使用授权 URL 打开浏览器 + code_challenge B->>M: 授权请求注意 M: 用户/authorizes M->>B: 重定向到带有授权代码的回调 B->>C: 授权代码回调 C->>M: 令牌请求 + code_verifier M->>C: 访问令牌（+ 刷新令牌）M->>C: 使用访问令牌进行 API 请求 ```

#### 2.5.1 Decision Flow Overview
2.5.1 决策流程概述

```mermaid
flowchart TD
    A[Start Auth Flow] --> B{Check Metadata Discovery}
    B -->|Available| C[Use Metadata Endpoints]
    B -->|Not Available| D[Use Default Endpoints]
```mermaid 流程图 TD A[开始认证流程] --> B{检查元数据发现} B -->|可用| C[使用元数据端点] B -->|不可用| D[使用默认端点]

    C --> G{Check Registration Endpoint}
    D --> G
C --> G{检查注册端点} D --> G

    G -->|Available| H[Perform Dynamic Registration]
    G -->|Not Available| I[Alternative Registration Required]
G -->|可用| H[执行动态注册] G -->|不可用| I[需要替代注册]

    H --> J[Start OAuth Flow]
    I --> J
H --> J[开始 OAuth 流程] I --> J

    J --> K[Generate PKCE Parameters]
    K --> L[Request Authorization]
    L --> M[User Authorization]
    M --> N[Exchange Code for Tokens]
    N --> O[Use Access Token]
```
J --> K[生成 PKCE 参数] K --> L[请求授权] L --> M[用户授权] M --> N[交换代码以获取令牌] N --> O[使用访问令牌]

### 2.6 Access Token Usage
### 2.6 访问令牌使用

#### 2.6.1 Token Requirements
#### 2.6.1 令牌要求

Access token handling **MUST** conform to
[OAuth 2.1 Section 5](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5)
requirements for resource requests. Specifically:
访问令牌处理 **必须** 符合 [OAuth 2.1 第 5 部分](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5) 对资源请求的要求。具体来说：

1. MCP client **MUST** use the Authorization request header field
   [Section 5.1.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.1.1):
1. MCP 客户端 **必须** 使用授权请求头字段 [第 5.1.1 部分](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.1.1)：

```
Authorization: Bearer <access-token>
```
```授权：Bearer <访问令牌>```

Note that authorization **MUST** be included in every HTTP request from client to server,
even if they are part of the same logical session.
注意，授权 **必须** 包含在客户端向服务器发出的每个 HTTP 请求中，即使它们是同一逻辑会话的一部分。

2. Access tokens **MUST NOT** be included in the URI query string
2. 访问令牌 **不得** 包含在 URI 查询字符串中

Example request:  示例请求：

```http
GET /v1/contexts HTTP/1.1
Host: mcp.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

#### 2.6.2 Token Handling
#### 2.6.2 令牌处理

Resource servers **MUST** validate access tokens as described in
[Section 5.2](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.2).
If validation fails, servers **MUST** respond according to
[Section 5.3](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.3)
error handling requirements. Invalid or expired tokens **MUST** receive a HTTP 401
response.
资源服务器 **必须** 按照第 5.2 节所述验证访问令牌。[链接](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.2)。如果验证失败，服务器 **必须** 根据第 5.3 节错误处理要求进行响应。无效或过期的令牌 **必须** 返回 HTTP 401 响应。

### 2.7 Security Considerations
### 2.7 安全考虑

The following security requirements **MUST** be implemented:
以下安全要求 **必须** 实现：

1. Clients **MUST** securely store tokens following OAuth 2.0 best practices
2. Servers **SHOULD** enforce token expiration and rotation
3. All authorization endpoints **MUST** be served over HTTPS
4. Servers **MUST** validate redirect URIs to prevent open redirect vulnerabilities
5. Redirect URIs **MUST** be either localhost URLs or HTTPS URLs
1. 客户端 **必须** 按照 OAuth 2.0 最佳实践安全存储令牌 2. 服务器 **应该** 强制执行令牌过期和轮换 3. 所有授权端点 **必须** 通过 HTTPS 提供服务 4. 服务器 **必须** 验证重定向 URI 以防止开放重定向漏洞 5. 重定向 URI **必须** 是本地主机 URL 或 HTTPS URL

### 2.8 Error Handling  ### 2.8 错误处理

Servers **MUST** return appropriate HTTP status codes for authorization errors:
服务器 **必须** 返回适当的 HTTP 状态码以处理授权错误：

| Status Code | Description  | Usage                                      |
| ----------- | ------------ | ------------------------------------------ |
| 401         | Unauthorized | Authorization required or token invalid    |
| 403         | Forbidden    | Invalid scopes or insufficient permissions |
| 400         | Bad Request  | Malformed authorization request            |
| 状态码 | 描述 | 用途 | | ----------- | ------------ | ------------------------------------------ | | 401 | 未授权 | 需要授权或令牌无效 | | 403 | 禁止 | 无效的作用域或权限不足 | | 400 | 错误请求 | 授权请求格式错误 |

### 2.9 Implementation Requirements
### 2.9 实现要求

1. Implementations **MUST** follow OAuth 2.1 security best practices
2. PKCE is **REQUIRED** for all clients
3. Token rotation **SHOULD** be implemented for enhanced security
4. Token lifetimes **SHOULD** be limited based on security requirements
1. 实现必须遵循 OAuth 2.1 安全最佳实践 2. 所有客户端必须使用 PKCE 3. 应实施令牌轮换以增强安全性 4. 应根据安全要求限制令牌有效期

### 2.10 Third-Party Authorization Flow
### 2.10 第三方授权流程

#### 2.10.1 Overview  #### 2.10.1 概述

MCP servers **MAY** support delegated authorization through third-party authorization
servers. In this flow, the MCP server acts as both an OAuth client (to the third-party
auth server) and an OAuth authorization server (to the MCP client).
MCP 服务器**可能**支持通过第三方授权服务器进行委托授权。在此流程中，MCP 服务器同时充当 OAuth 客户端（对第三方授权服务器）和 OAuth 授权服务器（对 MCP 客户端）。

#### 2.10.2 Flow Description
#### 2.10.2 流程描述

The third-party authorization flow comprises these steps:
第三方授权流程包括以下步骤：

1. MCP client initiates standard OAuth flow with MCP server
2. MCP server redirects user to third-party authorization server
3. User authorizes with third-party server
4. Third-party server redirects back to MCP server with authorization code
5. MCP server exchanges code for third-party access token
6. MCP server generates its own access token bound to the third-party session
7. MCP server completes original OAuth flow with MCP client
1. MCP 客户端与 MCP 服务器启动标准的 OAuth 流程 2. MCP 服务器将用户重定向到第三方授权服务器 3. 用户在第三方服务器上进行授权 4. 第三方服务器将授权码重定向回 MCP 服务器 5. MCP 服务器用授权码交换第三方访问令牌 6. MCP 服务器生成自己的访问令牌，该令牌与第三方会话绑定 7. MCP 服务器与 MCP 客户端完成原始的 OAuth 流程

```mermaid
sequenceDiagram
    participant B as User-Agent (Browser)
    participant C as MCP Client
    participant M as MCP Server
    participant T as Third-Party Auth Server
```mermaid sequenceDiagram participant B as 用户代理（浏览器） participant C as MCP 客户端 participant M as MCP 服务器 participant T as 第三方授权服务器

    C->>M: Initial OAuth Request
    M->>B: Redirect to Third-Party /authorize
    B->>T: Authorization Request
    Note over T: User authorizes
    T->>B: Redirect to MCP Server callback
    B->>M: Authorization code
    M->>T: Exchange code for token
    T->>M: Third-party access token
    Note over M: Generate bound MCP token
    M->>B: Redirect to MCP Client callback
    B->>C: MCP authorization code
    C->>M: Exchange code for token
    M->>C: MCP access token
```
C->>M: 初始 OAuth 请求 M->>B: 重定向到第三方/authorize B->>T: 授权请求 Note over T: 用户授权 T->>B: 重定向到 MCP 服务器回调 B->>M: 授权码 M->>T: 用代码换取令牌 T->>M: 第三方访问令牌 Note over M: 生成绑定 MCP 令牌 M->>B: 重定向到 MCP 客户端回调 B->>C: MCP 授权码 C->>M: 用代码换取令牌 M->>C: MCP 访问令牌

#### 2.10.3 Session Binding Requirements
#### 2.10.3 会话绑定要求

MCP servers implementing third-party authorization **MUST**:
实现第三方授权的 MCP 服务器 **必须**：

1. Maintain secure mapping between third-party tokens and issued MCP tokens
2. Validate third-party token status before honoring MCP tokens
3. Implement appropriate token lifecycle management
4. Handle third-party token expiration and renewal
1. 维护第三方令牌与颁发的 MCP 令牌之间的安全映射 2. 在尊重 MCP 令牌之前验证第三方令牌状态 3. 实施适当的令牌生命周期管理 4. 处理第三方令牌的过期和续订

#### 2.10.4 Security Considerations
#### 2.10.4 安全考虑

When implementing third-party authorization, servers **MUST**:
当实现第三方授权时，服务器**必须**：

1. Validate all redirect URIs
2. Securely store third-party credentials
3. Implement appropriate session timeout handling
4. Consider security implications of token chaining
5. Implement proper error handling for third-party auth failures
1. 验证所有重定向 URI 2. 安全存储第三方凭证 3. 实现适当的会话超时处理 4. 考虑令牌链的安全影响 5. 实现第三方授权失败的适当错误处理

## 3. Best Practices  ## 3. 最佳实践

#### 3.1 Local clients as Public OAuth 2.1 Clients
#### 3.1 本地客户端作为公共 OAuth 2.1 客户端

We strongly recommend that local clients implement OAuth 2.1 as a public client:
我们强烈建议本地客户将 OAuth 2.1 作为公开客户端实施：

1. Utilizing code challenges (PKCE) for authorization requests to prevent interception
   attacks
2. Implementing secure token storage appropriate for the local system
3. Following token refresh best practices to maintain sessions
4. Properly handling token expiration and renewal
1. 利用代码挑战（PKCE）进行授权请求以防止拦截攻击 2. 实施适合本地系统的安全令牌存储 3. 遵循令牌刷新最佳实践以维持会话 4. 正确处理令牌过期和续订

#### 3.2 Authorization Metadata Discovery
#### 3.2 授权元数据发现

We strongly recommend that all clients implement metadata discovery. This reduces the
need for users to provide endpoints manually or clients to fallback to the defined
defaults.
我们强烈建议所有客户端实现元数据发现。这减少了用户手动提供端点或客户端回退到定义的默认值的需求。

#### 3.3 Dynamic Client Registration
#### 3.3 动态客户端注册

Since clients do not know the set of MCP servers in advance, we strongly recommend the
implementation of dynamic client registration. This allows applications to automatically
register with the MCP server, and removes the need for users to obtain client ids
manually.
由于客户端事先不知道 MCP 服务器集合，我们强烈建议实施动态客户端注册。这允许应用程序自动注册到 MCP 服务器，并消除了用户手动获取客户端 ID 的需求。


# Overview
Source: https://modelcontextprotocol.io/specification/2025-03-26/basic/index
# 概述 来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/index



<Info>**Protocol Revision**: 2025-03-26</Info>
<信息>**协议版本**：2025-03-26

The Model Context Protocol consists of several key components that work together:
模型上下文协议由几个关键组件组成，它们协同工作：

* **Base Protocol**: Core JSON-RPC message types
* **Lifecycle Management**: Connection initialization, capability negotiation, and
  session control
* **Server Features**: Resources, prompts, and tools exposed by servers
* **Client Features**: Sampling and root directory lists provided by clients
* **Utilities**: Cross-cutting concerns like logging and argument completion
* **基础协议**：核心 JSON-RPC 消息类型 * **生命周期管理**：连接初始化、能力协商和会话控制 * **服务器功能**：服务器提供的资源、提示和工具 * **客户端功能**：客户端提供的采样和根目录列表 * **实用工具**：跨切面关注点，如日志记录和参数完成

All implementations **MUST** support the base protocol and lifecycle management
components. Other components **MAY** be implemented based on the specific needs of the
application.
所有实现都必须支持基础协议和生命周期管理组件。其他组件可根据应用程序的具体需求进行实现。

These protocol layers establish clear separation of concerns while enabling rich
interactions between clients and servers. The modular design allows implementations to
support exactly the features they need.
这些协议层建立了清晰的关注点分离，同时使客户端和服务器之间能够进行丰富的交互。模块化设计允许实现支持它们需要的精确功能。

## Messages  ## 消息

All messages between MCP clients and servers **MUST** follow the
[JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines
these types of messages:
所有 MCP 客户端和服务器之间的消息**必须**遵循[JSON-RPC 2.0](https://www.jsonrpc.org/specification)规范。该协议定义了以下类型的消息：

### Requests  ### 请求

Requests are sent from the client to the server or vice versa, to initiate an operation.
请求是从客户端发送到服务器或反之亦然，以启动操作。

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* Requests **MUST** include a string or integer ID.
* Unlike base JSON-RPC, the ID **MUST NOT** be `null`.
* The request ID **MUST NOT** have been previously used by the requestor within the same
  session.
* 请求必须包含一个字符串或整数 ID。* 与基础 JSON-RPC 不同，ID **MUST NOT** 为 `null`。* 请求 ID **MUST NOT** 在同一会话中已被请求者使用过。

### Responses  ### 响应

Responses are sent in reply to requests, containing the result or error of the operation.
响应是针对请求发送的，包含操作的返回结果或错误。

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  result?: {
    [key: string]: unknown;
  }
  error?: {
    code: number;
    message: string;
    data?: unknown;
  }
}
```

* Responses **MUST** include the same ID as the request they correspond to.
* **Responses** are further sub-categorized as either **successful results** or
  **errors**. Either a `result` or an `error` **MUST** be set. A response **MUST NOT**
  set both.
* Results **MAY** follow any JSON object structure, while errors **MUST** include an
  error code and message at minimum.
* Error codes **MUST** be integers.
* 响应 **必须** 包含与请求相对应的相同 ID。* **响应** 进一步分为 **成功结果** 或 **错误**。**必须** 设置 `result` 或 `error` 之一。**响应** **不得** 同时设置两者。* 结果 **可以** 遵循任何 JSON 对象结构，而错误 **必须** 至少包含错误代码和消息。* 错误代码 **必须** 是整数。

### Notifications  ### 通知

Notifications are sent from the client to the server or vice versa, as a one-way message.
The receiver **MUST NOT** send a response.
通知从客户端发送到服务器或反之，作为单向消息。接收者 **不得** 发送响应。

```typescript
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

* Notifications **MUST NOT** include an ID.
* 通知**不得**包含 ID。

### Batching  ### 批处理

JSON-RPC also defines a means to
[batch multiple requests and notifications](https://www.jsonrpc.org/specification#batch),
by sending them in an array. MCP implementations **MAY** support sending JSON-RPC
batches, but **MUST** support receiving JSON-RPC batches.
JSON-RPC 还定义了一种方法来[批量处理多个请求和通知](https://www.jsonrpc.org/specification#batch)，即通过将它们作为一个数组发送。MCP 实现**可以**支持发送 JSON-RPC 批处理，但**必须**支持接收 JSON-RPC 批处理。

## Auth  ## 认证

MCP provides an [Authorization](/specification/2025-03-26/basic/authorization) framework for use with HTTP.
Implementations using an HTTP-based transport **SHOULD** conform to this specification,
whereas implementations using STDIO transport **SHOULD NOT** follow this specification,
and instead retrieve credentials from the environment.
MCP 提供了一个[授权](/specification/2025-03-26/basic/authorization)框架，用于与 HTTP 一起使用。使用基于 HTTP 传输的实现**应当**遵守本规范，而使用 STDIO 传输的实现**不应当**遵循本规范，而应从环境中检索凭据。

Additionally, clients and servers **MAY** negotiate their own custom authentication and
authorization strategies.
此外，客户端和服务器**可以**协商自己的自定义身份验证和授权策略。

For further discussions and contributions to the evolution of MCP’s auth mechanisms, join
us in
[GitHub Discussions](https://github.com/modelcontextprotocol/specification/discussions)
to help shape the future of the protocol!
若要进一步讨论和对 MCP 身份验证机制的演变做出贡献，请加入我们的[GitHub 讨论](https://github.com/modelcontextprotocol/specification/discussions)，共同塑造协议的未来！

## Schema  ## 架构

The full specification of the protocol is defined as a
[TypeScript schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts).
This is the source of truth for all protocol messages and structures.
协议的完整规范定义为[TypeScript 模式](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts)，这是所有协议消息和结构的真实来源。

There is also a
[JSON Schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.json),
which is automatically generated from the TypeScript source of truth, for use with
various automated tooling.
此外，还有一个[JSON 模式](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.json)，它是从 TypeScript 真实源自动生成的，用于各种自动化工具。


# Lifecycle
Source: https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle
# 生命周期来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle



<Info>**Protocol Revision**: 2025-03-26</Info>
**协议修订版**：2025-03-26

The Model Context Protocol (MCP) defines a rigorous lifecycle for client-server
connections that ensures proper capability negotiation and state management.
模型上下文协议（MCP）定义了客户端-服务器连接的严格生命周期，确保适当的协商能力和状态管理。

1. **Initialization**: Capability negotiation and protocol version agreement
2. **Operation**: Normal protocol communication
3. **Shutdown**: Graceful termination of the connection
1. **初始化**：能力协商和协议版本协商 2. **操作**：正常协议通信 3. **关闭**：连接优雅终止

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client,Server: Initialization Phase
    activate Client
    Client->>+Server: initialize request
    Server-->>Client: initialize response
    Client--)Server: initialized notification
注意：客户端、服务器：初始化阶段激活客户端 客户端->>+服务器：初始化请求 服务器-->>客户端：初始化响应 服务器--)客户端：初始化通知

    Note over Client,Server: Operation Phase
    rect rgb(200, 220, 250)
        note over Client,Server: Normal protocol operations
    end
注意：客户端、服务器：操作阶段 矩形 rgb(200, 220, 250) 注意：客户端、服务器：正常协议操作结束

    Note over Client,Server: Shutdown
    Client--)-Server: Disconnect
    deactivate Server
    Note over Client,Server: Connection closed
```
注意：客户端、服务器：关闭 客户端--)-服务器：断开连接 激活服务器 注意：客户端、服务器：连接关闭 ```

## Lifecycle Phases  生命周期阶段

### Initialization  初始化

The initialization phase **MUST** be the first interaction between client and server.
During this phase, the client and server:
初始化阶段 **必须** 是客户端和服务器之间的第一次交互。在此阶段，客户端和服务器：

* Establish protocol version compatibility
* Exchange and negotiate capabilities
* Share implementation details
* 建立协议版本兼容性 * 交换和协商能力 * 分享实现细节

The client **MUST** initiate this phase by sending an `initialize` request containing:
客户端 **必须** 通过发送包含以下内容的 `initialize` 请求来启动此阶段：

* Protocol version supported
* Client capabilities
* Client implementation information
* 支持的协议版本 * 客户端能力 * 客户端实现信息

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "roots": {
        "listChanged": true
      },
      "sampling": {}
    },
    "clientInfo": {
      "name": "ExampleClient",
      "version": "1.0.0"
    }
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "method": "初始化", "params": { "协议版本": "2024-11-05", "功能": { "roots": { "listChanged": true }, "sampling": {} }, "客户端信息": { "名称": "ExampleClient", "版本": "1.0.0" } } } ```

The initialize request **MUST NOT** be part of a JSON-RPC
[batch](https://www.jsonrpc.org/specification#batch), as other requests and notifications
are not possible until initialization has completed. This also permits backwards
compatibility with prior protocol versions that do not explicitly support JSON-RPC
batches.
初始化请求**不得**是 JSON-RPC[批量](https://www.jsonrpc.org/specification#batch)的一部分，因为初始化完成之前无法进行其他请求和通知。这也允许与不支持 JSON-RPC 批量的先前协议版本保持向后兼容。

The server **MUST** respond with its own capabilities and information:
服务器**必须**响应其自身的功能和信息：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "logging": {},
      "prompts": {
        "listChanged": true
      },
      "resources": {
        "subscribe": true,
        "listChanged": true
      },
      "tools": {
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "ExampleServer",
      "version": "1.0.0"
    },
    "instructions": "Optional instructions for the client"
  }
}
```

After successful initialization, the client **MUST** send an `initialized` notification
to indicate it is ready to begin normal operations:
初始化成功后，客户端**必须**发送一个`initialized`通知，以表明它已准备好开始正常操作：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

* The client **SHOULD NOT** send requests other than
  [pings](/specification/2025-03-26/basic/utilities/ping) before the server has responded to the
  `initialize` request.
* The server **SHOULD NOT** send requests other than
  [pings](/specification/2025-03-26/basic/utilities/ping) and
  [logging](/specification/2025-03-26/server/utilities/logging) before receiving the `initialized`
  notification.
* 客户端 **不应** 在服务器对 `initialize` 请求做出响应之前发送除 [ping](/specification/2025-03-26/basic/utilities/ping) 之外的其他请求。* 服务器 **不应** 在收到 `initialized` 通知之前发送除 [ping](/specification/2025-03-26/basic/utilities/ping) 和 [日志记录](/specification/2025-03-26/server/utilities/logging) 之外的其他请求。

#### Version Negotiation  #### 版本协商

In the `initialize` request, the client **MUST** send a protocol version it supports.
This **SHOULD** be the *latest* version supported by the client.
在 `initialize` 请求中，客户端 **必须** 发送它支持的协议版本。这 **应该是** 客户端支持的最新版本。

If the server supports the requested protocol version, it **MUST** respond with the same
version. Otherwise, the server **MUST** respond with another protocol version it
supports. This **SHOULD** be the *latest* version supported by the server.
如果服务器支持请求的协议版本，它**必须**以相同的版本响应。否则，服务器**必须**以它支持的另一个协议版本响应。这**应该**是服务器支持的*最新*版本。

If the client does not support the version in the server's response, it **SHOULD**
disconnect.
如果客户端不支持服务器响应中的版本，它**应该**断开连接。

#### Capability Negotiation
#### 能力协商

Client and server capabilities establish which optional protocol features will be
available during the session.
客户端和服务器的能力确定在会话期间将可用哪些可选协议功能。

Key capabilities include:
核心功能包括：

| Category | Capability     | Description                                                                         |
| -------- | -------------- | ----------------------------------------------------------------------------------- |
| Client   | `roots`        | Ability to provide filesystem [roots](/specification/2025-03-26/client/roots)       |
| Client   | `sampling`     | Support for LLM [sampling](/specification/2025-03-26/client/sampling) requests      |
| Client   | `experimental` | Describes support for non-standard experimental features                            |
| Server   | `prompts`      | Offers [prompt templates](/specification/2025-03-26/server/prompts)                 |
| Server   | `resources`    | Provides readable [resources](/specification/2025-03-26/server/resources)           |
| Server   | `tools`        | Exposes callable [tools](/specification/2025-03-26/server/tools)                    |
| Server   | `logging`      | Emits structured [log messages](/specification/2025-03-26/server/utilities/logging) |
| Server   | `experimental` | Describes support for non-standard experimental features                            |
| Category | 能力 | 描述 | | -------- | ------------------ | ----------------------------------------------------------------------------------- | | 客户端 | `roots` | 提供文件系统 [roots](/specification/2025-03-26/client/roots) 的能力 | | 客户端 | `sampling` | 支持 LLM [sampling](/specification/2025-03-26/client/sampling) 请求 | | 客户端 | `experimental` | 描述对非标准实验性功能的支持 | | 服务器 | `prompts` | 提供 [提示模板](/specification/2025-03-26/server/prompts) | | 服务器 | `resources` | 提供可读的 [资源](/specification/2025-03-26/server/resources) | | 服务器 | `tools` | 暴露可调用的 [工具](/specification/2025-03-26/server/tools) | | 服务器 | `logging` | 发出结构化的 [日志消息](/specification/2025-03-26/server/utilities/logging) | | 服务器 | `experimental` | 描述对非标准实验性功能的支持 |

Capability objects can describe sub-capabilities like:
能力对象可以描述子能力，例如：

* `listChanged`: Support for list change notifications (for prompts, resources, and
  tools)
* `subscribe`: Support for subscribing to individual items' changes (resources only)
* `listChanged`: 支持列表变更通知（用于提示、资源和工具） * `subscribe`: 支持订阅单个项目的变更（仅限资源）

### Operation  ### 操作

During the operation phase, the client and server exchange messages according to the
negotiated capabilities.
在操作阶段，客户端和服务器根据协商的能力交换消息。

Both parties **SHOULD**:  双方**应**：

* Respect the negotiated protocol version
* Only use capabilities that were successfully negotiated
* 尊重协商的协议版本 * 只使用成功协商的能力

### Shutdown  ### 关闭

During the shutdown phase, one side (usually the client) cleanly terminates the protocol
connection. No specific shutdown messages are defined—instead, the underlying transport
mechanism should be used to signal connection termination:
在关闭阶段，一方（通常是客户端）干净地终止协议连接。没有定义特定的关闭消息——相反，应使用底层传输机制来指示连接终止：

#### stdio  #### 标准输入输出

For the stdio [transport](/specification/2025-03-26/basic/transports), the client **SHOULD** initiate
shutdown by:
对于 stdio [传输](/specification/2025-03-26/basic/transports)，客户端 **应当** 通过以下方式启动关闭：

1. First, closing the input stream to the child process (the server)
2. Waiting for the server to exit, or sending `SIGTERM` if the server does not exit
   within a reasonable time
3. Sending `SIGKILL` if the server does not exit within a reasonable time after `SIGTERM`
1. 首先关闭子进程（服务器）的输入流 2. 等待服务器退出，或者在服务器在合理时间内未退出时发送 `SIGTERM` 3. 如果在发送 `SIGTERM` 后合理时间内服务器仍未退出，则发送 `SIGKILL`

The server **MAY** initiate shutdown by closing its output stream to the client and
exiting.
服务器 **可能** 通过关闭其输出流到客户端并退出来启动关闭。

#### HTTP

For HTTP [transports](/specification/2025-03-26/basic/transports), shutdown is indicated by closing the
associated HTTP connection(s).
对于 HTTP [传输](/specification/2025-03-26/basic/transports)，关闭是通过关闭相关的 HTTP 连接来表示的。

## Timeouts  ## 超时

Implementations **SHOULD** establish timeouts for all sent requests, to prevent hung
connections and resource exhaustion. When the request has not received a success or error
response within the timeout period, the sender **SHOULD** issue a [cancellation
notification](/specification/2025-03-26/basic/utilities/cancellation) for that request and stop waiting for
a response.
实现应为所有发送的请求建立超时，以防止连接挂起和资源耗尽。当请求在超时期间未收到成功或错误响应时，发送方应发出对该请求的[取消通知](/specification/2025-03-26/basic/utilities/cancellation)，并停止等待响应。

SDKs and other middleware **SHOULD** allow these timeouts to be configured on a
per-request basis.
SDK 和其他中间件应允许按请求配置这些超时。

Implementations **MAY** choose to reset the timeout clock when receiving a [progress
notification](/specification/2025-03-26/basic/utilities/progress) corresponding to the request, as this
implies that work is actually happening. However, implementations **SHOULD** always
enforce a maximum timeout, regardless of progress notifications, to limit the impact of a
misbehaving client or server.
实现可以选择在收到对应于请求的[进度通知](/specification/2025-03-26/basic/utilities/progress)时重置超时计时器，因为这表示实际正在工作。然而，实现应始终强制执行最大超时，无论进度通知如何，以限制恶意客户端或服务器的影响。

## Error Handling  错误处理

Implementations **SHOULD** be prepared to handle these error cases:
实现应准备好处理这些错误情况：

* Protocol version mismatch
* Failure to negotiate required capabilities
* Request [timeouts](#timeouts)
协议版本不匹配 * 无法协商所需功能 * 请求 [超时](#timeouts)

Example initialization error:
示例初始化错误：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Unsupported protocol version",
    "data": {
      "supported": ["2024-11-05"],
      "requested": "1.0.0"
    }
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "error": { "code": -32602, "message": "不支持的协议版本", "data": { "supported": ["2024-11-05"], "requested": "1.0.0" } } } ```


# Transports
Source: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports
# 传输源：https://modelcontextprotocol.io/specification/2025-03-26/basic/transports



<Info>**Protocol Revision**: 2025-03-26</Info>
<信息>**协议版本**: 2025-03-26

MCP uses JSON-RPC to encode messages. JSON-RPC messages **MUST** be UTF-8 encoded.
MCP 使用 JSON-RPC 进行消息编码。JSON-RPC 消息**必须**使用 UTF-8 编码。

The protocol currently defines two standard transport mechanisms for client-server
communication:
该协议目前定义了两种标准的客户端-服务器通信传输机制：

1. [stdio](#stdio), communication over standard in and standard out
2. [Streamable HTTP](#streamable-http)
1. [stdio](#stdio)，通过标准输入和标准输出进行通信 2. [可流式 HTTP](#streamable-http)

Clients **SHOULD** support stdio whenever possible.
客户端应尽可能支持 stdio。

It is also possible for clients and servers to implement
[custom transports](#custom-transports) in a pluggable fashion.
客户端和服务器也可以以可插拔的方式实现[自定义传输](#custom-transports)。

## stdio

In the **stdio** transport:
在 stdio 传输中：

* The client launches the MCP server as a subprocess.
* The server reads JSON-RPC messages from its standard input (`stdin`) and sends messages
  to its standard output (`stdout`).
* Messages may be JSON-RPC requests, notifications, responses—or a JSON-RPC
  [batch](https://www.jsonrpc.org/specification#batch) containing one or more requests
  and/or notifications.
* Messages are delimited by newlines, and **MUST NOT** contain embedded newlines.
* The server **MAY** write UTF-8 strings to its standard error (`stderr`) for logging
  purposes. Clients **MAY** capture, forward, or ignore this logging.
* The server **MUST NOT** write anything to its `stdout` that is not a valid MCP message.
* The client **MUST NOT** write anything to the server's `stdin` that is not a valid MCP
  message.
* 客户端以子进程的方式启动 MCP 服务器。 * 服务器从其标准输入（stdin）读取 JSON-RPC 消息，并将消息发送到其标准输出（stdout）。 * 消息可以是 JSON-RPC 请求、通知、响应，或者包含一个或多个请求和/或通知的 JSON-RPC [批处理](https://www.jsonrpc.org/specification#batch)。 * 消息由换行符分隔，**不得**包含嵌套的换行符。 * 服务器**可以**将其标准错误（stderr）写入 UTF-8 字符串以进行日志记录。客户端**可以**捕获、转发或忽略此日志。 * 服务器**不得**将其 stdout 写入任何非有效 MCP 消息。 * 客户端**不得**将其 stdin 写入任何非有效 MCP 消息。

```mermaid
sequenceDiagram
    participant Client
    participant Server Process
```mermaid sequenceDiagram participant 客户端 participant 服务器进程 Process

    Client->>+Server Process: Launch subprocess
    loop Message Exchange
        Client->>Server Process: Write to stdin
        Server Process->>Client: Write to stdout
        Server Process--)Client: Optional logs on stderr
    end
    Client->>Server Process: Close stdin, terminate subprocess
    deactivate Server Process
```
客户端->>+服务器进程: 启动子进程循环 客户端->>服务器进程: 写入 stdin 服务器进程->>客户端: 写入 stdout 服务器进程--)客户端: 可选的日志输出到 stderr end 客户端->>服务器进程: 关闭 stdin，终止子进程 deactivate 服务器进程 ```

## Streamable HTTP  ## 可流式 HTTP

<Info>This replaces the [HTTP+SSE
transport](/specification/2024-11-05/basic/transports#http-with-sse) from
protocol version 2024-11-05. See the [backwards compatibility](#backwards-compatibility)
guide below.</Info>
这取代了协议版本 2024-11-05 中的[HTTP+SSE 传输](/specification/2024-11-05/basic/transports#http-with-sse)。请参阅下面的[向后兼容性](#backwards-compatibility)指南。

In the **Streamable HTTP** transport, the server operates as an independent process that
can handle multiple client connections. This transport uses HTTP POST and GET requests.
Server can optionally make use of
[Server-Sent Events](https://en.wikipedia.org/wiki/Server-sent_events) (SSE) to stream
multiple server messages. This permits basic MCP servers, as well as more feature-rich
servers supporting streaming and server-to-client notifications and requests.
在**可流式 HTTP**传输中，服务器作为一个独立进程运行，可以处理多个客户端连接。此传输使用 HTTP POST 和 GET 请求。服务器可以选择使用[服务器发送事件](https://en.wikipedia.org/wiki/Server-sent_events) (SSE)来流式传输多个服务器消息。这允许基本的 MCP 服务器，以及支持流式传输和服务器到客户端通知及请求的更丰富功能的服务器。

The server **MUST** provide a single HTTP endpoint path (hereafter referred to as the
**MCP endpoint**) that supports both POST and GET methods. For example, this could be a
URL like `https://example.com/mcp`.
服务器**必须**提供一个支持 POST 和 GET 方法的单个 HTTP 端点路径（以下称为**MCP 端点**）。例如，这可能是一个 URL，如`https://example.com/mcp`。

#### Security Warning  #### 安全警告

When implementing Streamable HTTP transport:
当实现可流式 HTTP 传输时：

1. Servers **MUST** validate the `Origin` header on all incoming connections to prevent DNS rebinding attacks
2. When running locally, servers **SHOULD** bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)
3. Servers **SHOULD** implement proper authentication for all connections
1. 服务器 **必须** 验证所有传入连接的 `Origin` 标头，以防止 DNS 重绑定攻击 2. 当本地运行时，服务器 **应该** 仅绑定到 localhost（127.0.0.1），而不是所有网络接口（0.0.0.0） 3. 服务器 **应该** 为所有连接实现适当的身份验证

Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites.
如果没有这些保护措施，攻击者可能会使用 DNS 重绑定从远程网站与本地 MCP 服务器交互。

### Sending Messages to the Server
### 向服务器发送消息

Every JSON-RPC message sent from the client **MUST** be a new HTTP POST request to the
MCP endpoint.
客户端发送的每个 JSON-RPC 消息 **必须** 是一个新的 HTTP POST 请求到 MCP 端点。

1. The client **MUST** use HTTP POST to send JSON-RPC messages to the MCP endpoint.
2. The client **MUST** include an `Accept` header, listing both `application/json` and
   `text/event-stream` as supported content types.
3. The body of the POST request **MUST** be one of the following:
   * A single JSON-RPC *request*, *notification*, or *response*
   * An array [batching](https://www.jsonrpc.org/specification#batch) one or more
     *requests and/or notifications*
   * An array [batching](https://www.jsonrpc.org/specification#batch) one or more
     *responses*
4. If the input consists solely of (any number of) JSON-RPC *responses* or
   *notifications*:
   * If the server accepts the input, the server **MUST** return HTTP status code 202
     Accepted with no body.
   * If the server cannot accept the input, it **MUST** return an HTTP error status code
     (e.g., 400 Bad Request). The HTTP response body **MAY** comprise a JSON-RPC *error
     response* that has no `id`.
5. If the input contains any number of JSON-RPC *requests*, the server **MUST** either
   return `Content-Type: text/event-stream`, to initiate an SSE stream, or
   `Content-Type: application/json`, to return one JSON object. The client **MUST**
   support both these cases.
6. If the server initiates an SSE stream:
   * The SSE stream **SHOULD** eventually include one JSON-RPC *response* per each
     JSON-RPC *request* sent in the POST body. These *responses* **MAY** be
     [batched](https://www.jsonrpc.org/specification#batch).
   * The server **MAY** send JSON-RPC *requests* and *notifications* before sending a
     JSON-RPC *response*. These messages **SHOULD** relate to the originating client
     *request*. These *requests* and *notifications* **MAY** be
     [batched](https://www.jsonrpc.org/specification#batch).
   * The server **SHOULD NOT** close the SSE stream before sending a JSON-RPC *response*
     per each received JSON-RPC *request*, unless the [session](#session-management)
     expires.
   * After all JSON-RPC *responses* have been sent, the server **SHOULD** close the SSE
     stream.
   * Disconnection **MAY** occur at any time (e.g., due to network conditions).
     Therefore:
     * Disconnection **SHOULD NOT** be interpreted as the client cancelling its request.
     * To cancel, the client **SHOULD** explicitly send an MCP `CancelledNotification`.
     * To avoid message loss due to disconnection, the server **MAY** make the stream
       [resumable](#resumability-and-redelivery).
1. 客户端**必须**使用 HTTP POST 向 MCP 端点发送 JSON-RPC 消息。2. 客户端**必须**包含一个`Accept`头，列出支持的两种内容类型`application/json`和`text/event-stream`。3. POST 请求的正文**必须**是以下之一：* 一个单独的 JSON-RPC *请求*、*通知*或*响应* * 一个[批处理](https://www.jsonrpc.org/specification#batch)一个或多个*请求和/或通知* * 一个[批处理](https://www.jsonrpc.org/specification#batch)一个或多个*响应* 4. 如果输入仅由（任何数量的）JSON-RPC *响应*或*通知*组成：* 如果服务器接受输入，服务器**必须**返回 HTTP 状态码 202 已接受，且无正文。* 如果服务器无法接受输入，它**必须**返回一个 HTTP 错误状态码（例如，400 请求错误）。HTTP 响应正文**可能**包含一个没有`id`的 JSON-RPC *错误响应*。5. 如果输入包含任何数量的 JSON-RPC *请求*，服务器**必须**返回`Content-Type: text/event-stream`以启动 SSE 流，或返回`Content-Type: application/json`以返回一个 JSON 对象。 客户端**必须**支持这两种情况。6.如果服务器启动一个 SSE 流：*SSE 流**应该**最终包含每个在 POST 正文中发送的 JSON-RPC**请求**的一个 JSON-RPC**响应**。这些**响应****可以**[批量处理](https://www.jsonrpc.org/specification#batch)。*服务器**可以**在发送 JSON-RPC**响应**之前发送 JSON-RPC**请求**和**通知**。这些消息**应该**与原始客户端**请求**相关。这些**请求**和**通知****可以**[批量处理](https://www.jsonrpc.org/specification#batch)。*服务器**不应该**在发送每个接收到的 JSON-RPC**请求**的 JSON-RPC**响应**之前关闭 SSE 流，除非[会话](#session-management)过期。*在所有 JSON-RPC**响应**都已发送后，服务器**应该**关闭 SSE 流。*断开连接**可能**在任何时候发生（例如，由于网络条件）。因此：*断开连接**不应该**被解释为客户端取消其请求。*要取消，客户端**应该**明确发送一个 MCP `CancelledNotification`。 为避免因断开连接而造成消息丢失，服务器**可能**使流[可恢复](#可恢复性和重发)。

### Listening for Messages from the Server
### 监听来自服务器的消息

1. The client **MAY** issue an HTTP GET to the MCP endpoint. This can be used to open an
   SSE stream, allowing the server to communicate to the client, without the client first
   sending data via HTTP POST.
2. The client **MUST** include an `Accept` header, listing `text/event-stream` as a
   supported content type.
3. The server **MUST** either return `Content-Type: text/event-stream` in response to
   this HTTP GET, or else return HTTP 405 Method Not Allowed, indicating that the server
   does not offer an SSE stream at this endpoint.
4. If the server initiates an SSE stream:
   * The server **MAY** send JSON-RPC *requests* and *notifications* on the stream. These
     *requests* and *notifications* **MAY** be
     [batched](https://www.jsonrpc.org/specification#batch).
   * These messages **SHOULD** be unrelated to any concurrently-running JSON-RPC
     *request* from the client.
   * The server **MUST NOT** send a JSON-RPC *response* on the stream **unless**
     [resuming](#resumability-and-redelivery) a stream associated with a previous client
     request.
   * The server **MAY** close the SSE stream at any time.
   * The client **MAY** close the SSE stream at any time.
1. 客户端 **可以** 向 MCP 端点发起 HTTP GET 请求。这可以用来打开 SSE 流，允许服务器在不通过 HTTP POST 先发送数据的情况下与客户端通信。2. 客户端 **必须** 包含一个`Accept`头，列出`text/event-stream`作为支持的媒体类型。3. 服务器 **必须** 在对 HTTP GET 请求的响应中返回`Content-Type: text/event-stream`，或者返回 HTTP 405 方法禁止，表示服务器在此端点不提供 SSE 流。4. 如果服务器启动 SSE 流：* 服务器 **可以** 在流上发送 JSON-RPC 请求和通知。这些请求和通知 **可以** 是[批处理](https://www.jsonrpc.org/specification#batch)。* 这些消息 **应该** 与客户端正在运行的任何并发 JSON-RPC 请求无关。* 服务器 **不得** 在流上发送 JSON-RPC 响应，除非[恢复](#resumability-and-redelivery)与之前客户端请求关联的流。* 服务器 **可以** 在任何时候关闭 SSE 流。* 客户端 **可以** 在任何时候关闭 SSE 流。

### Multiple Connections  ### 多个连接

1. The client **MAY** remain connected to multiple SSE streams simultaneously.
2. The server **MUST** send each of its JSON-RPC messages on only one of the connected
   streams; that is, it **MUST NOT** broadcast the same message across multiple streams.
   * The risk of message loss **MAY** be mitigated by making the stream
     [resumable](#resumability-and-redelivery).
1. 客户 **可以** 同时连接到多个 SSE 流。2. 服务器 **必须** 在其连接的流中发送每条 JSON-RPC 消息；也就是说，它 **不得** 在多个流中广播相同的消息。* 通过使流 [可恢复](#resumability-and-redelivery) 可以降低消息丢失的风险。

### Resumability and Redelivery
### 可恢复性和重传

To support resuming broken connections, and redelivering messages that might otherwise be
lost:
为了支持恢复中断的连接，并重传可能丢失的消息：

1. Servers **MAY** attach an `id` field to their SSE events, as described in the
   [SSE standard](https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation).
   * If present, the ID **MUST** be globally unique across all streams within that
     [session](#session-management)—or all streams with that specific client, if session
     management is not in use.
2. If the client wishes to resume after a broken connection, it **SHOULD** issue an HTTP
   GET to the MCP endpoint, and include the
   [`Last-Event-ID`](https://html.spec.whatwg.org/multipage/server-sent-events.html#the-last-event-id-header)
   header to indicate the last event ID it received.
   * The server **MAY** use this header to replay messages that would have been sent
     after the last event ID, *on the stream that was disconnected*, and to resume the
     stream from that point.
   * The server **MUST NOT** replay messages that would have been delivered on a
     different stream.
1. 服务器 **可能** 在其 SSE 事件中附加一个 `id` 字段，如 [SSE 标准](https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation) 所述。* 如果存在，ID **必须** 在该 [会话](#session-management) 内的所有流中全局唯一——或者在没有使用会话管理的情况下，对于具有该特定客户端的所有流。2. 如果客户端希望在断开连接后恢复，它 **应该** 向 MCP 端点发出 HTTP GET 请求，并包含 `Last-Event-ID` [头](https://html.spec.whatwg.org/multipage/server-sent-events.html#the-last-event-id-header)，以指示它接收到的最后一个事件 ID。* 服务器 **可能** 使用此头来自动重放最后一个事件 ID 之后将发送的消息，*在断开连接的流上*，并从该点恢复流。* 服务器 **不得** 重放将发送到不同流的任何消息。

In other words, these event IDs should be assigned by servers on a *per-stream* basis, to
act as a cursor within that particular stream.
换句话说，这些事件 ID 应由服务器按 *流* 基础分配，作为该特定流中的游标。

### Session Management  ### 会话管理

An MCP "session" consists of logically related interactions between a client and a
server, beginning with the [initialization phase](/specification/2025-03-26/basic/lifecycle). To support
servers which want to establish stateful sessions:
一个 MCP "会话"由客户端和服务器之间逻辑相关的交互组成，始于[初始化阶段](/specification/2025-03-26/basic/lifecycle)。为了支持想要建立有状态会话的服务器：

1. A server using the Streamable HTTP transport **MAY** assign a session ID at
   initialization time, by including it in an `Mcp-Session-Id` header on the HTTP
   response containing the `InitializeResult`.
   * The session ID **SHOULD** be globally unique and cryptographically secure (e.g., a
     securely generated UUID, a JWT, or a cryptographic hash).
   * The session ID **MUST** only contain visible ASCII characters (ranging from 0x21 to
     0x7E).
2. If an `Mcp-Session-Id` is returned by the server during initialization, clients using
   the Streamable HTTP transport **MUST** include it in the `Mcp-Session-Id` header on
   all of their subsequent HTTP requests.
   * Servers that require a session ID **SHOULD** respond to requests without an
     `Mcp-Session-Id` header (other than initialization) with HTTP 400 Bad Request.
3. The server **MAY** terminate the session at any time, after which it **MUST** respond
   to requests containing that session ID with HTTP 404 Not Found.
4. When a client receives HTTP 404 in response to a request containing an
   `Mcp-Session-Id`, it **MUST** start a new session by sending a new `InitializeRequest`
   without a session ID attached.
5. Clients that no longer need a particular session (e.g., because the user is leaving
   the client application) **SHOULD** send an HTTP DELETE to the MCP endpoint with the
   `Mcp-Session-Id` header, to explicitly terminate the session.
   * The server **MAY** respond to this request with HTTP 405 Method Not Allowed,
     indicating that the server does not allow clients to terminate sessions.
1. 使用可流式 HTTP 传输的服务器**可以在**初始化时分配一个会话 ID，通过在包含`InitializeResult`的 HTTP 响应中包含`Mcp-Session-Id`头来实现。*会话 ID**应该**是全球唯一的且加密安全的（例如，安全生成的 UUID、JWT 或加密散列）。*会话 ID**必须**只包含可见 ASCII 字符（范围从 0x21 到 0x7E）。2. 如果服务器在初始化期间返回`Mcp-Session-Id`，则使用可流式 HTTP 传输的客户端**必须**在所有后续 HTTP 请求的`Mcp-Session-Id`头来包含它。*需要会话 ID 的服务器**应该**对没有`Mcp-Session-Id`头（除了初始化）的请求响应 HTTP 400 错误请求。3. 服务器**可以在**任何时间终止会话，之后它**必须**对包含该会话 ID 的请求响应 HTTP 404 未找到。4. 当客户端在包含`Mcp-Session-Id`的请求中收到 HTTP 404 响应时，它**必须**通过发送不带会话 ID 的新`InitializeRequest`来启动新会话。5. 客户端不再需要特定会话（例如，因为用户正在离开客户端应用程序）**应**向 MCP 端点发送带有`Mcp-Session-Id`头的 HTTP DELETE 请求，以显式终止会话。* 服务器**可能**会以 HTTP 405 方法不允许响应此请求，表示服务器不允许客户端终止会话。

### Sequence Diagram  序列图

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    note over Client, Server: initialization
客户端、服务器初始化

    Client->>+Server: POST InitializeRequest
    Server->>-Client: InitializeResponse<br>Mcp-Session-Id: 1868a90c...
客户端->>+服务器：POST InitializeRequest 服务器->>-客户端：InitializeResponse
Mcp-Session-Id：1868a90c...

    Client->>+Server: POST InitializedNotification<br>Mcp-Session-Id: 1868a90c...
    Server->>-Client: 202 Accepted
客户端->>+服务器：POST InitializedNotification
Mcp-Session-Id：1868a90c... 服务器->>-客户端：202 已接受

    note over Client, Server: client requests
    Client->>+Server: POST ... request ...<br>Mcp-Session-Id: 1868a90c...
客户端、服务器：客户端请求客户端->>+服务器：POST ... 请求 ...
Mcp-Session-Id：1868a90c...

    alt single HTTP response
      Server->>Client: ... response ...
    else server opens SSE stream
      loop while connection remains open
          Server-)Client: ... SSE messages from server ...
      end
      Server-)Client: SSE event: ... response ...
    end
    deactivate Server
alt 单个 HTTP 响应 服务器->>客户端：... 响应 ... 否则服务器在连接保持打开时打开 SSE 流循环 服务器-)客户端：... 服务器 SSE 消息 ... 结束 服务器-)客户端：SSE 事件：... 响应 ... 结束 关闭服务器

    note over Client, Server: client notifications/responses
    Client->>+Server: POST ... notification/response ...<br>Mcp-Session-Id: 1868a90c...
    Server->>-Client: 202 Accepted
注意客户端、服务器：客户端通知/响应 客户端->>+服务器：POST ... 通知/响应 ...
Mcp-Session-Id：1868a90c... 服务器->>-客户端：202 已接受

    note over Client, Server: server requests
    Client->>+Server: GET<br>Mcp-Session-Id: 1868a90c...
    loop while connection remains open
        Server-)Client: ... SSE messages from server ...
    end
    deactivate Server
注意客户端、服务器：服务器请求 客户端->>+服务器：GET
Mcp-Session-Id：1868a90c... 在连接保持打开时循环 服务器-)客户端：... 服务器 SSE 消息 ... 结束 关闭服务器

```

### Backwards Compatibility
### 向后兼容性

Clients and servers can maintain backwards compatibility with the deprecated [HTTP+SSE
transport](/specification/2024-11-05/basic/transports#http-with-sse) (from
protocol version 2024-11-05) as follows:
客户端和服务器可以通过以下方式与已弃用的[HTTP+SSE 传输](/specification/2024-11-05/basic/transports#http-with-sse)（自协议版本 2024-11-05 起）保持向后兼容：

**Servers** wanting to support older clients should:
**服务器**希望支持旧版客户端应：

* Continue to host both the SSE and POST endpoints of the old transport, alongside the
  new "MCP endpoint" defined for the Streamable HTTP transport.
  * It is also possible to combine the old POST endpoint and the new MCP endpoint, but
    this may introduce unneeded complexity.
* 继续托管旧传输的 SSE 和 POST 端点，以及为可流式 HTTP 传输定义的新“MCP 端点”。* 也可以将旧的 POST 端点和新的 MCP 端点合并，但这可能会引入不必要的复杂性。

**Clients** wanting to support older servers should:
**客户端**希望支持旧版服务器应：

1. Accept an MCP server URL from the user, which may point to either a server using the
   old transport or the new transport.
2. Attempt to POST an `InitializeRequest` to the server URL, with an `Accept` header as
   defined above:
   * If it succeeds, the client can assume this is a server supporting the new Streamable
     HTTP transport.
   * If it fails with an HTTP 4xx status code (e.g., 405 Method Not Allowed or 404 Not
     Found):
     * Issue a GET request to the server URL, expecting that this will open an SSE stream
       and return an `endpoint` event as the first event.
     * When the `endpoint` event arrives, the client can assume this is a server running
       the old HTTP+SSE transport, and should use that transport for all subsequent
       communication.
1. 从用户处接受 MCP 服务器 URL，该 URL 可能指向使用旧传输或新传输的服务器。2. 尝试将`InitializeRequest` POST 到服务器 URL，并带有上面定义的`Accept`头：* 如果成功，客户端可以假设这是一个支持可流式 HTTP 传输的服务器。* 如果失败并返回 HTTP 4xx 状态码（例如，405 方法不允许或 404 未找到）：* 向服务器 URL 发出 GET 请求，期望这将打开 SSE 流并返回第一个`endpoint`事件。* 当`endpoint`事件到达时，客户端可以假设这是一个运行旧 HTTP+SSE 传输的服务器，并且应该使用该传输进行所有后续通信。

## Custom Transports  ## 自定义传输

Clients and servers **MAY** implement additional custom transport mechanisms to suit
their specific needs. The protocol is transport-agnostic and can be implemented over any
communication channel that supports bidirectional message exchange.
客户端和服务器**可以**实现额外的自定义传输机制以满足其特定需求。该协议与传输无关，可以在支持双向消息交换的任何通信通道上实现。

Implementers who choose to support custom transports **MUST** ensure they preserve the
JSON-RPC message format and lifecycle requirements defined by MCP. Custom transports
**SHOULD** document their specific connection establishment and message exchange patterns
to aid interoperability.
选择支持自定义传输的实现者**必须**确保他们保留 MCP 定义的 JSON-RPC 消息格式和生命周期要求。自定义传输**应当**记录其特定的连接建立和消息交换模式，以帮助互操作性。


# Cancellation
Source: https://modelcontextprotocol.io/specification/2025-03-26/basic/utilities/cancellation
# 取消源：https://modelcontextprotocol.io/specification/2025-03-26/basic/utilities/cancellation



<Info>**Protocol Revision**: 2025-03-26</Info>
<信息>**协议修订版**：2025-03-26

The Model Context Protocol (MCP) supports optional cancellation of in-progress requests
through notification messages. Either side can send a cancellation notification to
indicate that a previously-issued request should be terminated.
模型上下文协议（MCP）支持通过通知消息取消正在进行的请求。任何一方都可以发送取消通知，以表明之前发出的请求应被终止。

## Cancellation Flow  ## 取消流程

When a party wants to cancel an in-progress request, it sends a `notifications/cancelled`
notification containing:
当一个党派想要取消一个正在进行的请求时，它发送一个包含以下内容的`notifications/cancelled`通知：

* The ID of the request to cancel
* An optional reason string that can be logged or displayed
*请求取消的 ID* 可选的日志或显示的取消原因字符串

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/cancelled",
  "params": {
    "requestId": "123",
    "reason": "User requested cancellation"
  }
}
```
```json { "jsonrpc": "2.0", "method": "notifications/cancelled", "params": { "requestId": "123", "reason": "用户请求取消" } } ```

## Behavior Requirements  ## 行为要求

1. Cancellation notifications **MUST** only reference requests that:
   * Were previously issued in the same direction
   * Are believed to still be in-progress
2. The `initialize` request **MUST NOT** be cancelled by clients
3. Receivers of cancellation notifications **SHOULD**:
   * Stop processing the cancelled request
   * Free associated resources
   * Not send a response for the cancelled request
4. Receivers **MAY** ignore cancellation notifications if:
   * The referenced request is unknown
   * Processing has already completed
   * The request cannot be cancelled
5. The sender of the cancellation notification **SHOULD** ignore any response to the
   request that arrives afterward
1. 取消通知**必须**仅引用以下请求：*之前已在同一方向发出的请求*认为仍在进行中的请求 2. 客户**不得**取消`initialize`请求 3. 接收取消通知的接收者**应该**：*停止处理已取消的请求*释放相关资源*不发送对已取消请求的响应 4. 接收者**可以**忽略以下取消通知：*引用的请求未知*处理已完成*请求无法取消 5. 取消通知的发送者**应该**忽略之后到达的任何对请求的响应

## Timing Considerations  时间考虑因素

Due to network latency, cancellation notifications may arrive after request processing
has completed, and potentially after a response has already been sent.
由于网络延迟，取消通知可能会在请求处理完成后到达，甚至可能在响应已经发送之后。

Both parties **MUST** handle these race conditions gracefully:
双方**必须**优雅地处理这些竞态条件：

```mermaid
sequenceDiagram
   participant Client
   participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

   Client->>Server: Request (ID: 123)
   Note over Server: Processing starts
   Client--)Server: notifications/cancelled (ID: 123)
   alt
      Note over Server: Processing may have<br/>completed before<br/>cancellation arrives
   else If not completed
      Note over Server: Stop processing
   end
```
客户端->服务器：请求（ID：123）备注在服务器上：处理开始 客户端--)服务器：通知/已取消（ID：123）备选备注在服务器上：处理可能已完成，在取消到达之前
否则如果未完成 备注在服务器上：停止处理 end

## Implementation Notes  实现说明

* Both parties **SHOULD** log cancellation reasons for debugging
* Application UIs **SHOULD** indicate when cancellation is requested
* 双方 **应** 记录取消原因以供调试 * 应用程序用户界面 **应** 显示已请求取消

## Error Handling  错误处理

Invalid cancellation notifications **SHOULD** be ignored:
无效的取消通知 **应** 被忽略：

* Unknown request IDs
* Already completed requests
* Malformed notifications
未知请求 ID * 已完成的请求 * 格式错误的通知

This maintains the "fire and forget" nature of notifications while allowing for race
conditions in asynchronous communication.
这保持了通知的“点火即走”特性，同时允许异步通信中的竞态条件。


# Ping
Source: https://modelcontextprotocol.io/specification/2025-03-26/basic/utilities/ping
# Ping 源：https://modelcontextprotocol.io/specification/2025-03-26/basic/utilities/ping



<Info>**Protocol Revision**: 2025-03-26</Info>
**协议版本**: 2025-03-26

The Model Context Protocol includes an optional ping mechanism that allows either party
to verify that their counterpart is still responsive and the connection is alive.
模型上下文协议包含一个可选的 ping 机制，允许任何一方验证对方是否仍然响应并且连接是活跃的。

## Overview  ## 概述

The ping functionality is implemented through a simple request/response pattern. Either
the client or server can initiate a ping by sending a `ping` request.
ping 功能通过简单的请求/响应模式实现。客户端或服务器都可以通过发送`ping`请求来发起 ping。

## Message Format  消息格式

A ping request is a standard JSON-RPC request with no parameters:
ping 请求是一个没有参数的标准 JSON-RPC 请求：

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "method": "ping"
}
```

## Behavior Requirements  ## 行为要求

1. The receiver **MUST** respond promptly with an empty response:
1. 接收方 **必须** 及时响应，返回空响应：

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {}
}
```

2. If no response is received within a reasonable timeout period, the sender **MAY**:
   * Consider the connection stale
   * Terminate the connection
   * Attempt reconnection procedures
2. 如果在合理的时间内未收到响应，发送方 **可以**： * 考虑连接已失效 * 终止连接 * 尝试重新连接

## Usage Patterns  使用模式

```mermaid
sequenceDiagram
    participant Sender
    participant Receiver
```mermaid sequenceDiagram participant 发送者 participant 接收者

    Sender->>Receiver: ping request
    Receiver->>Sender: empty response
```
发送者->>接收者：ping 请求 接收者->>发送者：空响应

## Implementation Considerations
## 实施注意事项

* Implementations **SHOULD** periodically issue pings to detect connection health
* The frequency of pings **SHOULD** be configurable
* Timeouts **SHOULD** be appropriate for the network environment
* Excessive pinging **SHOULD** be avoided to reduce network overhead
* 实现应定期发送 ping 以检测连接健康 * ping 的频率**应**可配置 * 超时**应**适合网络环境 * 应避免过度 ping 以减少网络开销

## Error Handling  错误处理

* Timeouts **SHOULD** be treated as connection failures
* Multiple failed pings **MAY** trigger connection reset
* Implementations **SHOULD** log ping failures for diagnostics
* 超时**应**被视为连接故障 * 多次失败的 ping**可能**触发连接重置 * 实现应记录 ping 故障以供诊断


# Progress
Source: https://modelcontextprotocol.io/specification/2025-03-26/basic/utilities/progress
# 进度来源：https://modelcontextprotocol.io/specification/2025-03-26/basic/utilities/progress



<Info>**Protocol Revision**: 2025-03-26</Info>
**协议版本**: 2025-03-26

The Model Context Protocol (MCP) supports optional progress tracking for long-running
operations through notification messages. Either side can send progress notifications to
provide updates about operation status.
模型上下文协议（MCP）支持通过通知消息进行可选的进度跟踪，以支持长时间运行的操作。任何一方都可以发送进度通知，以提供操作状态的更新。

## Progress Flow  ## 进度流程

When a party wants to *receive* progress updates for a request, it includes a
`progressToken` in the request metadata.
当一方希望接收请求的进度更新时，它会在请求元数据中包含一个 `progressToken`。

* Progress tokens **MUST** be a string or integer value
* Progress tokens can be chosen by the sender using any means, but **MUST** be unique
  across all active requests.
* 进度令牌 **必须** 是字符串或整数值 * 发送方可以使用任何方式选择进度令牌，但 **必须** 在所有活动请求中保持唯一。

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "some_method",
  "params": {
    "_meta": {
      "progressToken": "abc123"
    }
  }
}
```

The receiver **MAY** then send progress notifications containing:
接收方 **可以** 然后发送进度通知，包括：

* The original progress token
* The current progress value so far
* An optional "total" value
* An optional "message" value
* 原始进度令牌 * 到目前为止的当前进度值 * 可选的 "总" 值 * 可选的 "消息" 值

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "abc123",
    "progress": 50,
    "total": 100,
    "message": "Reticulating splines..."
  }
}
```

* The `progress` value **MUST** increase with each notification, even if the total is
  unknown.
* The `progress` and the `total` values **MAY** be floating point.
* The `message` field **SHOULD** provide relevant human readable progress information.
* `progress` 值 **必须** 随每个通知递增，即使总数量未知。* `progress` 和 `total` 值 **可能** 是浮点数。* `message` 字段 **应该** 提供相关的可读进度信息。

## Behavior Requirements  行为需求

1. Progress notifications **MUST** only reference tokens that:
1. 进度通知 **必须** 仅引用以下令牌：

   * Were provided in an active request
   * Are associated with an in-progress operation
* 在活动请求中提供的 * 与正在进行的操作相关联

2. Receivers of progress requests **MAY**:
   * Choose not to send any progress notifications
   * Send notifications at whatever frequency they deem appropriate
   * Omit the total value if unknown
接收进度请求的人 **可以**：* 选择不发送任何进度通知 * 按照他们认为合适的频率发送通知 * 如果不知道，可以省略总价值

```mermaid
sequenceDiagram
    participant Sender
    participant Receiver
```mermaid sequenceDiagram participant 发送者 participant 接收者

    Note over Sender,Receiver: Request with progress token
    Sender->>Receiver: Method request with progressToken
在发送者，接收者上方注明：带有进度令牌的请求 发送者->>接收者：带有进度令牌的方法请求

    Note over Sender,Receiver: Progress updates
    loop Progress Updates
        Receiver-->>Sender: Progress notification (0.2/1.0)
        Receiver-->>Sender: Progress notification (0.6/1.0)
        Receiver-->>Sender: Progress notification (1.0/1.0)
    end
在发送者，接收者上方注明：进度更新循环 进度更新 接收者-->>发送者：进度通知（0.2/1.0） 接收者-->>发送者：进度通知（0.6/1.0） 接收者-->>发送者：进度通知（1.0/1.0） 结束

    Note over Sender,Receiver: Operation complete
    Receiver->>Sender: Method response
```
在发送者，接收者上方注明：操作完成 接收者->>发送者：方法响应 ```

## Implementation Notes  实现说明

* Senders and receivers **SHOULD** track active progress tokens
* Both parties **SHOULD** implement rate limiting to prevent flooding
* Progress notifications **MUST** stop after completion
发送者和接收者**应**跟踪活动进度令牌 双方**应**实施速率限制以防止洪水攻击 进度通知**必须**在完成后停止


# Key Changes
Source: https://modelcontextprotocol.io/specification/2025-03-26/changelog
# 关键变更来源：https://modelcontextprotocol.io/specification/2025-03-26/changelog



This document lists changes made to the Model Context Protocol (MCP) specification since
the previous revision, [2024-11-05](/specification/2024-11-05).
本文档列出了自上次修订以来对模型上下文协议（MCP）规范所做的更改，[2024-11-05](/specification/2024-11-05)。

## Major changes  ## 主要更改

1. Added a comprehensive **[authorization framework](/specification/2025-03-26/basic/authorization)**
   based on OAuth 2.1 (PR
   [#133](https://github.com/modelcontextprotocol/specification/pull/133))
2. Replaced the previous HTTP+SSE transport with a more flexible **[Streamable HTTP
   transport](/specification/2025-03-26/basic/transports#streamable-http)** (PR
   [#206](https://github.com/modelcontextprotocol/specification/pull/206))
3. Added support for JSON-RPC **[batching](https://www.jsonrpc.org/specification#batch)**
   (PR [#228](https://github.com/modelcontextprotocol/specification/pull/228))
4. Added comprehensive **tool annotations** for better describing tool behavior, like
   whether it is read-only or destructive (PR
   [#185](https://github.com/modelcontextprotocol/specification/pull/185))
1. 添加了基于 OAuth 2.1 的全面**[授权框架](/specification/2025-03-26/basic/authorization**)（PR [#133](https://github.com/modelcontextprotocol/specification/pull/133)）2. 将之前的 HTTP+SSE 传输替换为更灵活的**[可流式 HTTP 传输](/specification/2025-03-26/basic/transports#streamable-http**)（PR [#206](https://github.com/modelcontextprotocol/specification/pull/206)）3. 添加了对 JSON-RPC **[批处理](https://www.jsonrpc.org/specification#batch**)的支持（PR [#228](https://github.com/modelcontextprotocol/specification/pull/228)）4. 添加了全面的**工具注释**，以更好地描述工具行为，例如是否为只读或破坏性（PR [#185](https://github.com/modelcontextprotocol/specification/pull/185)）

## Other schema changes  ## 其他架构变更

* Added `message` field to `ProgressNotification` to provide descriptive status updates
* Added support for audio data, joining the existing text and image content types
* Added `completions` capability to explicitly indicate support for argument
  autocompletion suggestions
* 将 `message` 字段添加到 `ProgressNotification` 以提供描述性状态更新 * 添加了对音频数据的支持，与现有的文本和图像内容类型相结合 * 添加了 `completions` 功能，以明确表示对参数自动完成建议的支持

See
[the updated schema](http://github.com/modelcontextprotocol/specification/tree/main/schema/2025-03-26/schema.ts)
for more details.
查看更新后的架构[详情](http://github.com/modelcontextprotocol/specification/tree/main/schema/2025-03-26/schema.ts)

## Full changelog  ## 完整变更日志

For a complete list of all changes that have been made since the last protocol revision,
[see GitHub](https://github.com/modelcontextprotocol/specification/compare/2024-11-05...2025-03-26).
查看自上次协议修订以来所有变更的完整列表，请参阅[GitHub](https://github.com/modelcontextprotocol/specification/compare/2024-11-05...2025-03-26)。


# Roots
Source: https://modelcontextprotocol.io/specification/2025-03-26/client/roots
# 根源来源：https://modelcontextprotocol.io/specification/2025-03-26/client/roots



<Info>**Protocol Revision**: 2025-03-26</Info>
<信息>**协议版本**: 2025-03-26

The Model Context Protocol (MCP) provides a standardized way for clients to expose
filesystem "roots" to servers. Roots define the boundaries of where servers can operate
within the filesystem, allowing them to understand which directories and files they have
access to. Servers can request the list of roots from supporting clients and receive
notifications when that list changes.
模型上下文协议（MCP）为客户端提供了一种标准化的方式，以便将文件系统“根目录”暴露给服务器。根目录定义了服务器在文件系统中可以操作的范围，使它们能够了解哪些目录和文件它们可以访问。服务器可以从支持客户端请求根目录列表，并在该列表发生变化时接收通知。

## User Interaction Model
## 用户交互模型

Roots in MCP are typically exposed through workspace or project configuration interfaces.
在 MCP 中，根目录通常通过工作区或项目配置界面进行暴露。

For example, implementations could offer a workspace/project picker that allows users to
select directories and files the server should have access to. This can be combined with
automatic workspace detection from version control systems or project files.
例如，实现可以提供工作区/项目选择器，允许用户选择服务器应有权访问的目录和文件。这可以与来自版本控制系统或项目文件的自动工作区检测相结合。

However, implementations are free to expose roots through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.
然而，实现可以自由选择任何适合其需求的接口模式来暴露根节点——协议本身并不强制任何特定的用户交互模型。

## Capabilities  ## 功能

Clients that support roots **MUST** declare the `roots` capability during
[initialization](/specification/2025-03-26/basic/lifecycle#initialization):
客户端在[初始化](/specification/2025-03-26/basic/lifecycle#initialization)期间**必须**声明`roots`功能

```json
{
  "capabilities": {
    "roots": {
      "listChanged": true
    }
  }
}
```
```json { "能力": { "根": { "列表已更改": true } } } ```

`listChanged` indicates whether the client will emit notifications when the list of roots
changes.
`listChanged` 表示客户端是否会在根列表发生变化时发出通知。

## Protocol Messages  ## 协议消息

### Listing Roots  ### 根列表

To retrieve roots, servers send a `roots/list` request:
要检索根，服务器发送 `roots/list` 请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "roots/list"
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "roots": [
      {
        "uri": "file:///home/user/projects/myproject",
        "name": "My Project"
      }
    ]
  }
}
```

### Root List Changes  ### 根列表变更

When roots change, clients that support `listChanged` **MUST** send a notification:
当根列表发生变化时，支持 `listChanged` 的客户端 **必须** 发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/roots/list_changed"
}
```

## Message Flow  消息流程

```mermaid
sequenceDiagram
    participant Server
    participant Client
```mermaid sequenceDiagram participant 服务器 participant 客户端

    Note over Server,Client: Discovery
    Server->>Client: roots/list
    Client-->>Server: Available roots
注释在 服务器,客户端 上: 服务器->>客户端: roots/list 客户端-->>服务器: 可用根

    Note over Server,Client: Changes
    Client--)Server: notifications/roots/list_changed
    Server->>Client: roots/list
    Client-->>Server: Updated roots
```
注意：服务器、客户端：客户端更改--服务器：通知/roots/list_changed 服务器>>>客户端：roots/list 客户端-->>服务器：已更新 roots

## Data Types  数据类型

### Root  ### 根

A root definition includes:
根定义包括：

* `uri`: Unique identifier for the root. This **MUST** be a `file://` URI in the current
  specification.
* `name`: Optional human-readable name for display purposes.
* `uri`：根的唯一标识符。根据当前规范，此 **必须** 是 `file://` URI。* `name`：可选的用于显示的易读名称。

Example roots for different use cases:
不同用例的示例根

#### Project Directory  #### 项目目录

```json
{
  "uri": "file:///home/user/projects/myproject",
  "name": "My Project"
}
```

#### Multiple Repositories
#### 多个仓库

```json
[
  {
    "uri": "file:///home/user/repos/frontend",
    "name": "Frontend Repository"
  },
  {
    "uri": "file:///home/user/repos/backend",
    "name": "Backend Repository"
  }
]
```
```json [{ "uri": "file:///home/user/repos/frontend", "name": "前端仓库" }, { "uri": "file:///home/user/repos/backend", "name": "后端仓库" }] ```

## Error Handling  错误处理

Clients **SHOULD** return standard JSON-RPC errors for common failure cases:
客户端 **应** 返回标准 JSON-RPC 错误以处理常见失败情况：

* Client does not support roots: `-32601` (Method not found)
* Internal errors: `-32603`
* 客户端不支持根节点：`-32601`（方法未找到） * 内部错误：`-32603`

Example error:  示例错误：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32601,
    "message": "Roots not supported",
    "data": {
      "reason": "Client does not have roots capability"
    }
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "error": { "code": -32601, "message": "不支持根", "data": { "reason": "客户端没有根能力" } } } ```

## Security Considerations
安全注意事项

1. Clients **MUST**:  1. 客户端 **必须**：

   * Only expose roots with appropriate permissions
   * Validate all root URIs to prevent path traversal
   * Implement proper access controls
   * Monitor root accessibility
* 仅暴露具有适当权限的根 * 验证所有根 URI 以防止路径遍历 * 实现适当的访问控制 * 监控根的可访问性

2. Servers **SHOULD**:
   * Handle cases where roots become unavailable
   * Respect root boundaries during operations
   * Validate all paths against provided roots
2. 服务器 **应当**：* 处理根不可用的情况 * 在操作期间尊重根边界 * 验证所有路径与提供的根

## Implementation Guidelines
## 实施指南

1. Clients **SHOULD**:  1. 客户端 **应当**：

   * Prompt users for consent before exposing roots to servers
   * Provide clear user interfaces for root management
   * Validate root accessibility before exposing
   * Monitor for root changes
* 在向服务器暴露根之前提示用户同意 * 提供清晰的用户界面进行根管理 * 在暴露之前验证根的可访问性 * 监控根的变化

2. Servers **SHOULD**:
   * Check for roots capability before usage
   * Handle root list changes gracefully
   * Respect root boundaries in operations
   * Cache root information appropriately
2. 服务器 **应当**：* 在使用前检查根的能力 * 优雅地处理根列表的变化 * 在操作中尊重根边界 * 适当地缓存根信息


# Sampling
Source: https://modelcontextprotocol.io/specification/2025-03-26/client/sampling
# 样本来源: https://modelcontextprotocol.io/specification/2025-03-26/client/sampling



<Info>**Protocol Revision**: 2025-03-26</Info>
<信息>**协议版本**: 2025-03-26

The Model Context Protocol (MCP) provides a standardized way for servers to request LLM
sampling ("completions" or "generations") from language models via clients. This flow
allows clients to maintain control over model access, selection, and permissions while
enabling servers to leverage AI capabilities—with no server API keys necessary.
Servers can request text, audio, or image-based interactions and optionally include
context from MCP servers in their prompts.
模型上下文协议（MCP）为服务器通过客户端请求 LLM 样本（“完成”或“生成”）提供了一种标准化方式。这种流程允许客户端在服务器利用 AI 能力的同时，保持对模型访问、选择和权限的控制，无需服务器 API 密钥。服务器可以请求文本、音频或基于图像的交互，并可选择在提示中包含来自 MCP 服务器的上下文。

## User Interaction Model
## 用户交互模型

Sampling in MCP allows servers to implement agentic behaviors, by enabling LLM calls to
occur *nested* inside other MCP server features.
MCP 中的采样允许服务器通过启用LLM调用在其他 MCP 服务器功能内部发生*嵌套*来实现代理行为。

Implementations are free to expose sampling through any interface pattern that suits
their needs—the protocol itself does not mandate any specific user interaction
model.
实现可以自由选择任何适合其需求的接口模式来暴露采样——协议本身并不强制任何特定的用户交互模型。

<Warning>
  For trust & safety and security, there **SHOULD** always
  be a human in the loop with the ability to deny sampling requests.
<警告> 为了信任与安全，以及安全起见，始终应该有人工智能在循环中，并具有拒绝采样请求的能力。

  Applications **SHOULD**:
应用程序 **应当**：

  * Provide UI that makes it easy and intuitive to review sampling requests
  * Allow users to view and edit prompts before sending
  * Present generated responses for review before delivery
</Warning>
* 提供易于直观审查采样请求的用户界面 * 允许用户在发送前查看和编辑提示 * 在交付前展示生成的响应以供审查 

## Capabilities  ## 功能

Clients that support sampling **MUST** declare the `sampling` capability during
[initialization](/specification/2025-03-26/basic/lifecycle#initialization):
支持采样的客户端必须在[初始化](/specification/2025-03-26/basic/lifecycle#initialization)期间声明`sampling`能力：

```json
{
  "capabilities": {
    "sampling": {}
  }
}
```

## Protocol Messages  ## 协议消息

### Creating Messages  ### 创建消息

To request a language model generation, servers send a `sampling/createMessage` request:
请求语言模型生成时，服务器发送`sampling/createMessage`请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What is the capital of France?"
        }
      }
    ],
    "modelPreferences": {
      "hints": [
        {
          "name": "claude-3-sonnet"
        }
      ],
      "intelligencePriority": 0.8,
      "speedPriority": 0.5
    },
    "systemPrompt": "You are a helpful assistant.",
    "maxTokens": 100
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "role": "assistant",
    "content": {
      "type": "text",
      "text": "The capital of France is Paris."
    },
    "model": "claude-3-sonnet-20240307",
    "stopReason": "endTurn"
  }
}
```

## Message Flow  # 消息流程

```mermaid
sequenceDiagram
    participant Server
    participant Client
    participant User
    participant LLM
```mermaid sequenceDiagram participant 服务器 participant 客户端 participant 用户 participant LLM

    Note over Server,Client: Server initiates sampling
    Server->>Client: sampling/createMessage
服务器端，客户端：服务器启动采样 服务器->>客户端：创建采样消息

    Note over Client,User: Human-in-the-loop review
    Client->>User: Present request for approval
    User-->>Client: Review and approve/modify
客户端，用户：人工审核  客户端->>用户：提交审批请求 用户-->>客户端：审核并修改

    Note over Client,LLM: Model interaction
    Client->>LLM: Forward approved request
    LLM-->>Client: Return generation
客户端，LLM：模型交互 客户端->>LLM：转发已批准的请求 LLM-->>客户端：返回生成结果

    Note over Client,User: Response review
    Client->>User: Present response for approval
    User-->>Client: Review and approve/modify
客户端，用户：响应审核 客户端->>用户：提交响应供审批 用户-->>客户端：审核并修改

    Note over Server,Client: Complete request
    Client-->>Server: Return approved response
```
服务器端，客户端：完成请求 客户端-->>服务器：返回批准的响应 ```

## Data Types  数据类型

### Messages  ### 消息

Sampling messages can contain:
抽样消息可能包含：

#### Text Content  #### 文本内容

```json
{
  "type": "text",
  "text": "The message content"
}
```
```json { "type": "text", "text": "消息内容" } ```

#### Image Content  图像内容

```json
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/jpeg"
}
```
```json { "type": "image", "data": "base64 编码的图像数据", "mimeType": "image/jpeg" } ```

#### Audio Content  #### 音频内容

```json
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}
```

### Model Preferences  ### 模型偏好

Model selection in MCP requires careful abstraction since servers and clients may use
different AI providers with distinct model offerings. A server cannot simply request a
specific model by name since the client may not have access to that exact model or may
prefer to use a different provider's equivalent model.
在 MCP 中进行模型选择需要仔细的抽象，因为服务器和客户端可能使用不同的 AI 提供商和不同的模型提供。服务器不能简单地通过名称请求特定的模型，因为客户端可能没有访问该特定模型或可能希望使用不同提供商的等效模型。

To solve this, MCP implements a preference system that combines abstract capability
priorities with optional model hints:
为了解决这个问题，MCP 实现了一个结合抽象能力优先级和可选模型提示的偏好系统：

#### Capability Priorities
#### 能力优先级

Servers express their needs through three normalized priority values (0-1):
服务器通过三个标准化优先级值（0-1）表达其需求：

* `costPriority`: How important is minimizing costs? Higher values prefer cheaper models.
* `speedPriority`: How important is low latency? Higher values prefer faster models.
* `intelligencePriority`: How important are advanced capabilities? Higher values prefer
  more capable models.
* `costPriority`: 成本最小化有多重要？更高的值偏好更便宜的模型。 * `speedPriority`: 低延迟有多重要？更高的值偏好更快的模型。 * `intelligencePriority`: 先进功能有多重要？更高的值偏好更强大的模型。

#### Model Hints  模型提示

While priorities help select models based on characteristics, `hints` allow servers to
suggest specific models or model families:
当优先级有助于根据特征选择模型时，`提示`允许服务器建议特定模型或模型系列：

* Hints are treated as substrings that can match model names flexibly
* Multiple hints are evaluated in order of preference
* Clients **MAY** map hints to equivalent models from different providers
* Hints are advisory—clients make final model selection
提示被视为可以灵活匹配模型名称的子字符串 * 按优先级顺序评估多个提示 * 客户**可能**将提示映射到不同提供商的等效模型 * 提示仅供参考——客户做出最终模型选择

For example:  例如：

```json
{
  "hints": [
    { "name": "claude-3-sonnet" }, // Prefer Sonnet-class models
    { "name": "claude" } // Fall back to any Claude model
  ],
  "costPriority": 0.3, // Cost is less important
  "speedPriority": 0.8, // Speed is very important
  "intelligencePriority": 0.5 // Moderate capability needs
}
```
```json { "hints": [ { "name": "claude-3-sonnet" }, // 优先选择 Sonnet 类模型 { "name": "claude" } // 作为备选的任何 Claude 模型 ], "costPriority": 0.3, // 成本的重要性较低 "speedPriority": 0.8, // 速度非常重要 "intelligencePriority": 0.5 // 需要中等能力 } ```

The client processes these preferences to select an appropriate model from its available
options. For instance, if the client doesn't have access to Claude models but has Gemini,
it might map the sonnet hint to `gemini-1.5-pro` based on similar capabilities.
客户端会处理这些偏好以从其可用选项中选择合适的模型。例如，如果客户端没有 Claude 模型的访问权限但拥有 Gemini，它可能会根据类似的功能将 sonnet 提示映射到`gemini-1.5-pro`。

## Error Handling  错误处理

Clients **SHOULD** return errors for common failure cases:
客户端 **应当** 返回常见故障情况下的错误：

Example error:  示例错误：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -1,
    "message": "User rejected sampling request"
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "error": { "code": -1, "message": "用户拒绝采样请求" } } ```

## Security Considerations
安全注意事项

1. Clients **SHOULD** implement user approval controls
2. Both parties **SHOULD** validate message content
3. Clients **SHOULD** respect model preference hints
4. Clients **SHOULD** implement rate limiting
5. Both parties **MUST** handle sensitive data appropriately
1. 客户 **应** 实现用户批准控制
2. 双方 **应** 验证消息内容
3. 客户 **应** 尊重模型偏好提示
4. 客户 **应** 实现速率限制
5. 双方 **必须** 适当处理敏感数据


# Specification
Source: https://modelcontextprotocol.io/specification/2025-03-26/index
规范来源：https://modelcontextprotocol.io/specification/2025-03-26/index



[Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open protocol that
enables seamless integration between LLM applications and external data sources and
tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating
custom AI workflows, MCP provides a standardized way to connect LLMs with the context
they need.
[模型上下文协议](https://modelcontextprotocol.io) (MCP) 是一种开放协议，它使得应用程序和外部数据源及工具之间能够无缝集成。无论您是在构建一个 AI 驱动的集成开发环境、增强聊天界面，还是创建定制的 AI 工作流程，MCP 都提供了一种标准化的方式来连接所需上下文。

This specification defines the authoritative protocol requirements, based on the
TypeScript schema in
[schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts).
本规范定义了基于[schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts)中 TypeScript 模式的权威协议要求。

For implementation guides and examples, visit
[modelcontextprotocol.io](https://modelcontextprotocol.io).
关于实现指南和示例，请访问 [modelcontextprotocol.io](https://modelcontextprotocol.io)。

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD
NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14)
\[[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)]
\[[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)] when, and only when, they
appear in all capitals, as shown here.
本文件中关键词“MUST”、“MUST NOT”、“REQUIRED”、“SHALL”、“SHALL NOT”、“SHOULD”、“SHOULD NOT”、“RECOMMENDED”、“NOT RECOMMENDED”、“MAY”和“OPTIONAL”的解释，应按照[BCP 14](https://datatracker.ietf.org/doc/html/bcp14) \[[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)] \[[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)]所述，仅在全部大写时适用，如本例所示。

## Overview  ## 概述

MCP provides a standardized way for applications to:
MCP 为应用程序提供了一种标准化的方式来：

* Share contextual information with language models
* Expose tools and capabilities to AI systems
* Build composable integrations and workflows
* 与语言模型共享上下文信息 * 向 AI 系统暴露工具和能力 * 构建可组合的集成和工作流程

The protocol uses [JSON-RPC](https://www.jsonrpc.org/) 2.0 messages to establish
communication between:
该协议使用[JSON-RPC](https://www.jsonrpc.org/) 2.0 消息来建立以下实体之间的通信：

* **Hosts**: LLM applications that initiate connections
* **Clients**: Connectors within the host application
* **Servers**: Services that provide context and capabilities
* **主机**：LLM 初始化连接的应用程序 * **客户端**：主机应用程序内的连接器 * **服务器**：提供上下文和能力的服务

MCP takes some inspiration from the
[Language Server Protocol](https://microsoft.github.io/language-server-protocol/), which
standardizes how to add support for programming languages across a whole ecosystem of
development tools. In a similar way, MCP standardizes how to integrate additional context
and tools into the ecosystem of AI applications.
MCP 从 [语言服务器协议](https://microsoft.github.io/language-server-protocol/) 中汲取了一些灵感，该协议标准化了如何在整个开发工具生态系统中添加对编程语言的支持。以类似的方式，MCP 标准化了如何将额外的上下文和工具集成到人工智能应用生态系统中。

## Key Details  ## 关键细节

### Base Protocol  ### 基础协议

* [JSON-RPC](https://www.jsonrpc.org/) message format
* Stateful connections
* Server and client capability negotiation
* [JSON-RPC](https://www.jsonrpc.org/) 消息格式 * 有状态连接 * 服务器和客户端能力协商

### Features  ### 功能

Servers offer any of the following features to clients:
服务器向客户提供以下功能：

* **Resources**: Context and data, for the user or the AI model to use
* **Prompts**: Templated messages and workflows for users
* **Tools**: Functions for the AI model to execute
* **资源**：用户或 AI 模型使用的上下文和数据 * **提示**：为用户提供的模板消息和工作流程 * **工具**：AI 模型可以执行的功能

Clients may offer the following feature to servers:
客户可以向服务器提供以下功能：

* **Sampling**: Server-initiated agentic behaviors and recursive LLM interactions
* **采样**: 服务器触发的代理行为和递归 LLM 交互

### Additional Utilities  ### 其他工具

* Configuration
* Progress tracking
* Cancellation
* Error reporting
* Logging
* 配置 * 进度跟踪 * 取消 * 错误报告 * 记录

## Security and Trust & Safety
## 安全与信任安全

The Model Context Protocol enables powerful capabilities through arbitrary data access
and code execution paths. With this power comes important security and trust
considerations that all implementors must carefully address.
模型上下文协议通过任意数据访问和代码执行路径，实现了强大的功能。这种能力伴随着重要的安全和信任考虑，所有实现者都必须谨慎处理。

### Key Principles  ### 核心原则

1. **User Consent and Control**
1. **用户同意与控制**

   * Users must explicitly consent to and understand all data access and operations
   * Users must retain control over what data is shared and what actions are taken
   * Implementors should provide clear UIs for reviewing and authorizing activities
用户必须明确同意并理解所有数据访问和操作 * 用户必须保留控制权，决定共享哪些数据和采取哪些行动 * 实施者应提供清晰的用户界面，以便审查和授权活动

2. **Data Privacy**  2. **数据隐私**

   * Hosts must obtain explicit user consent before exposing user data to servers
   * Hosts must not transmit resource data elsewhere without user consent
   * User data should be protected with appropriate access controls
* 主机必须在向服务器暴露用户数据之前获得用户的明确同意 * 主机不得在未经用户同意的情况下将资源数据传输到其他地方 * 应使用适当的访问控制保护用户数据

3. **Tool Safety**  3. **工具安全**

   * Tools represent arbitrary code execution and must be treated with appropriate
     caution.
     * In particular, descriptions of tool behavior such as annotations should be
       considered untrusted, unless obtained from a trusted server.
   * Hosts must obtain explicit user consent before invoking any tool
   * Users should understand what each tool does before authorizing its use
* 工具代表任意代码执行，必须谨慎对待。* 特别地，工具行为描述（如注释）应视为不可信，除非从受信任的服务器获取。* 主机在调用任何工具之前必须获得明确用户同意。* 用户在授权使用工具之前应了解每个工具的功能。

4. **LLM Sampling Controls**
   * Users must explicitly approve any LLM sampling requests
   * Users should control:
     * Whether sampling occurs at all
     * The actual prompt that will be sent
     * What results the server can see
   * The protocol intentionally limits server visibility into prompts
4. **LLM 样本控制** * 用户必须明确批准任何 LLM 样本请求 * 用户应控制： * 是否进行采样 * 实际发送的提示 * 服务器可以看到的结果 * 协议有意限制服务器对提示的可见性

### Implementation Guidelines
### 实施指南

While MCP itself cannot enforce these security principles at the protocol level,
implementors **SHOULD**:
虽然 MCP 本身无法在协议级别强制执行这些安全原则，实现者 **应**：

1. Build robust consent and authorization flows into their applications
2. Provide clear documentation of security implications
3. Implement appropriate access controls and data protections
4. Follow security best practices in their integrations
5. Consider privacy implications in their feature designs
1. 在其应用程序中构建稳健的同意和授权流程 2. 提供安全影响清晰的文档 3. 实施适当的访问控制和数据保护 4. 在其集成中遵循安全最佳实践 5. 在其功能设计中考虑隐私影响

## Learn More  了解更多

Explore the detailed specification for each protocol component:
查看每个协议组件的详细规格说明：

<CardGroup cols={5}>
  <Card title="Architecture" icon="sitemap" href="architecture" />
 

  <Card title="Base Protocol" icon="code" href="basic" />


  <Card title="Server Features" icon="server" href="server" />


  <Card title="Client Features" icon="user" href="client" />


  <Card title="Contributing" icon="pencil" href="contributing" />
</CardGroup>



# Overview
Source: https://modelcontextprotocol.io/specification/2025-03-26/server/index
# 概述来源：https://modelcontextprotocol.io/specification/2025-03-26/server/index



<Info>**Protocol Revision**: 2025-03-26</Info>
**协议版本**: 2025-03-26

Servers provide the fundamental building blocks for adding context to language models via
MCP. These primitives enable rich interactions between clients, servers, and language
models:
服务器提供了通过 MCP 为语言模型添加上下文的基本构建块。这些原语使客户端、服务器和语言模型之间能够进行丰富的交互：

* **Prompts**: Pre-defined templates or instructions that guide language model
  interactions
* **Resources**: Structured data or content that provides additional context to the model
* **Tools**: Executable functions that allow models to perform actions or retrieve
  information
* **提示**：引导语言模型交互的预定义模板或指令 * **资源**：为模型提供额外上下文的有序数据或内容 * **工具**：允许模型执行操作或检索信息的可执行函数

Each primitive can be summarized in the following control hierarchy:
每个原语可以总结如下控制层次结构：

| Primitive | Control                | Description                                        | Example                         |
| --------- | ---------------------- | -------------------------------------------------- | ------------------------------- |
| Prompts   | User-controlled        | Interactive templates invoked by user choice       | Slash commands, menu options    |
| Resources | Application-controlled | Contextual data attached and managed by the client | File contents, git history      |
| Tools     | Model-controlled       | Functions exposed to the LLM to take actions       | API POST requests, file writing |
| 原始 | 控制 | 描述 | 示例 | | --------- | ---------------------- | -------------------------------------------------- | ------------------------------- | | 提示 | 用户控制 | 用户选择触发的交互式模板 | 划分命令、菜单选项 | | 资源 | 应用控制 | 客户端附加和管理上下文数据 | 文件内容、git 历史 | | 工具 | 模型控制 | 暴露给 LLM 以执行操作的函数 | API POST 请求、文件写入 |

Explore these key primitives in more detail below:
在下面更详细地探索这些关键原始操作：

<CardGroup cols={3}>
  <Card title="Prompts" icon="message" href="prompts" />
 

  <Card title="Resources" icon="file-lines" href="resources" />


  <Card title="Tools" icon="wrench" href="tools" />
</CardGroup>
 


# Prompts
Source: https://modelcontextprotocol.io/specification/2025-03-26/server/prompts
# 提示来源：https://modelcontextprotocol.io/specification/2025-03-26/server/prompts



<Info>**Protocol Revision**: 2025-03-26</Info>
**协议版本**: 2025-03-26

The Model Context Protocol (MCP) provides a standardized way for servers to expose prompt
templates to clients. Prompts allow servers to provide structured messages and
instructions for interacting with language models. Clients can discover available
prompts, retrieve their contents, and provide arguments to customize them.
模型上下文协议（MCP）为服务器向客户端暴露提示模板提供了一种标准化方式。提示允许服务器提供结构化消息和指令，以便与语言模型交互。客户端可以发现可用的提示，检索其内容，并提供参数以自定义它们。

## User Interaction Model
用户交互模型

Prompts are designed to be **user-controlled**, meaning they are exposed from servers to
clients with the intention of the user being able to explicitly select them for use.
提示被设计为**用户可控**，这意味着它们从服务器暴露给客户端，目的是让用户能够明确选择它们进行使用。

Typically, prompts would be triggered through user-initiated commands in the user
interface, which allows users to naturally discover and invoke available prompts.
通常，提示将通过用户界面中的用户发起的命令来触发，这使用户能够自然地发现和调用可用的提示。

For example, as slash commands:
例如，作为斜杠命令：

![Example of prompt exposed as slash command](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2025-03-26/server/slash-command.png)
![作为斜杠命令暴露的提示示例](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2025-03-26/server/slash-command.png)

However, implementors are free to expose prompts through any interface pattern that suits
their needs—the protocol itself does not mandate any specific user interaction
model.
然而，实现者可以根据自己的需求自由选择任何接口模式来暴露提示——协议本身并不强制规定任何特定的用户交互模型。

## Capabilities  ## 功能

Servers that support prompts **MUST** declare the `prompts` capability during
[initialization](/specification/2025-03-26/basic/lifecycle#initialization):
支持提示的服务器 **必须** 在 [初始化](/specification/2025-03-26/basic/lifecycle#initialization) 时声明 `prompts` 功能：

```json
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the server will emit notifications when the list of
available prompts changes.
`listChanged` 表示服务器是否会在可用提示列表更改时发出通知。

## Protocol Messages  ## 协议消息

### Listing Prompts  ### 列表提示

To retrieve available prompts, clients send a `prompts/list` request. This operation
supports [pagination](/specification/2025-03-26/server/utilities/pagination).
要获取可用的提示，客户端发送 `prompts/list` 请求。此操作支持[分页](/specification/2025-03-26/server/utilities/pagination)。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "prompts/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "prompts": [
      {
        "name": "code_review",
        "description": "Asks the LLM to analyze code quality and suggest improvements",
        "arguments": [
          {
            "name": "code",
            "description": "The code to review",
            "required": true
          }
        ]
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### Getting a Prompt  获取提示

To retrieve a specific prompt, clients send a `prompts/get` request. Arguments may be
auto-completed through [the completion API](/specification/2025-03-26/server/utilities/completion).
要检索特定提示，客户端发送 `prompts/get` 请求。参数可以通过 [完成 API](/specification/2025-03-26/server/utilities/completion) 自动补全。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "prompts/get",
  "params": {
    "name": "code_review",
    "arguments": {
      "code": "def hello():\n    print('world')"
    }
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "description": "Code review prompt",
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "Please review this Python code:\ndef hello():\n    print('world')"
        }
      }
    ]
  }
}
```
```json { "jsonrpc": "2.0", "id": 2, "result": { "description": "代码审查提示", "messages": [ { "role": "user", "content": { "type": "text", "text": "请审查以下 Python 代码：\ndef hello():\n print('world')" } } ] } } ```

### List Changed Notification
### 列表变更通知

When the list of available prompts changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:
当可用的提示列表发生变化时，声明了 `listChanged` 功能的服务器 **应当** 发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}
```

## Message Flow  消息流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client,Server: Discovery
    Client->>Server: prompts/list
    Server-->>Client: List of prompts
注意：客户端、服务器：发现客户端->>服务器：提示/列表服务器-->>客户端：提示列表

    Note over Client,Server: Usage
    Client->>Server: prompts/get
    Server-->>Client: Prompt content
注意：客户端、服务器：使用客户端->>服务器：获取提示服务器-->>客户端：提示内容

    opt listChanged
      Note over Client,Server: Changes
      Server--)Client: prompts/list_changed
      Client->>Server: prompts/list
      Server-->>Client: Updated prompts
    end
```
opt listChanged 注意：客户端、服务器：变更服务器--)客户端：prompts/list_changed 客户端->>服务器：prompts/list 服务器-->>客户端：更新后的提示列表

## Data Types  数据类型

### Prompt  ### 提示

A prompt definition includes:
提示定义包括：

* `name`: Unique identifier for the prompt
* `description`: Optional human-readable description
* `arguments`: Optional list of arguments for customization
* `name`: 提示的唯一标识符 * `description`: 可选的人类可读描述 * `arguments`: 可选的自定义参数列表

### PromptMessage  ### 提示消息

Messages in a prompt can contain:
提示中的消息可以包含：

* `role`: Either "user" or "assistant" to indicate the speaker
* `content`: One of the following content types:
* `角色`: 表示说话者的 "user" 或 "assistant" * `内容`: 以下内容类型之一：

#### Text Content  #### 文本内容

Text content represents plain text messages:
文本内容表示纯文本消息：

```json
{
  "type": "text",
  "text": "The text content of the message"
}
```
```json { "type": "text", "text": "消息的文本内容" } ```

This is the most common content type used for natural language interactions.
这是最常用的自然语言交互内容类型。

#### Image Content  图像内容

Image content allows including visual information in messages:
图片内容允许在消息中包含视觉信息：

```json
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/png"
}
```

The image data **MUST** be base64-encoded and include a valid MIME type. This enables
multi-modal interactions where visual context is important.
图片数据**必须**是 base64 编码的，并包含有效的 MIME 类型。这可以支持多模态交互，其中视觉上下文很重要。

#### Audio Content  音频内容

Audio content allows including audio information in messages:
音频内容允许在消息中包含音频信息：

```json
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}
```
```json { "类型": "音频", "数据": "base64 编码的音频数据", "MIME 类型": "audio/wav" } ```

The audio data MUST be base64-encoded and include a valid MIME type. This enables
multi-modal interactions where audio context is important.
音频数据必须进行 base64 编码，并包含有效的 MIME 类型。这使多模态交互成为可能，其中音频上下文很重要。

#### Embedded Resources  嵌入式资源

Embedded resources allow referencing server-side resources directly in messages:
嵌入式资源允许在消息中直接引用服务器端资源：

```json
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "Resource content"
  }
}
```
```json { "type": "资源", "resource": { "uri": "资源://example", "mimeType": "text/plain", "text": "资源内容" } } ```

Resources can contain either text or binary (blob) data and **MUST** include:
资源可以包含文本或二进制（blob）数据，**必须**包括：

* A valid resource URI
* The appropriate MIME type
* Either text content or base64-encoded blob data
一个有效的资源 URI * 适当的 MIME 类型 * 文本内容或 base64 编码的 blob 数据

Embedded resources enable prompts to seamlessly incorporate server-managed content like
documentation, code samples, or other reference materials directly into the conversation
flow.
嵌入式资源能够无缝地将服务器管理的文档、代码示例或其他参考资料直接集成到对话流程中。

## Error Handling  错误处理

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:
服务器 **应**返回标准 JSON-RPC 错误以处理常见失败情况：

* Invalid prompt name: `-32602` (Invalid params)
* Missing required arguments: `-32602` (Invalid params)
* Internal errors: `-32603` (Internal error)
* 无效的提示名称：`-32602`（无效参数）* 缺少必需的参数：`-32602`（无效参数）* 内部错误：`-32603`（内部错误）

## Implementation Considerations
## 实施注意事项

1. Servers **SHOULD** validate prompt arguments before processing
2. Clients **SHOULD** handle pagination for large prompt lists
3. Both parties **SHOULD** respect capability negotiation
1. 服务器 **应当** 在处理之前验证提示参数 2. 客户端 **应当** 处理大量提示列表的分页 3. 双方 **应当** 尊重能力协商

## Security  ## 安全

Implementations **MUST** carefully validate all prompt inputs and outputs to prevent
injection attacks or unauthorized access to resources.
实现必须仔细验证所有提示输入和输出，以防止注入攻击或未经授权访问资源。


# Resources
Source: https://modelcontextprotocol.io/specification/2025-03-26/server/resources
# 资源来源：https://modelcontextprotocol.io/specification/2025-03-26/server/resources



<Info>**Protocol Revision**: 2025-03-26</Info>
**协议版本**: 2025-03-26

The Model Context Protocol (MCP) provides a standardized way for servers to expose
resources to clients. Resources allow servers to share data that provides context to
language models, such as files, database schemas, or application-specific information.
Each resource is uniquely identified by a
[URI](https://datatracker.ietf.org/doc/html/rfc3986).
模型上下文协议（MCP）为服务器向客户端暴露资源提供了一种标准化的方式。资源允许服务器共享为语言模型提供上下文的数据，例如文件、数据库模式或特定于应用程序的信息。每个资源都由一个[URI](https://datatracker.ietf.org/doc/html/rfc3986)唯一标识。

## User Interaction Model
## 用户交互模型

Resources in MCP are designed to be **application-driven**, with host applications
determining how to incorporate context based on their needs.
MCP 中的资源设计为**应用驱动**，主机应用程序根据其需求确定如何根据上下文进行整合。

For example, applications could:
例如，应用程序可以：

* Expose resources through UI elements for explicit selection, in a tree or list view
* Allow the user to search through and filter available resources
* Implement automatic context inclusion, based on heuristics or the AI model's selection
* 通过 UI 元素显式选择资源，以树形或列表视图呈现 * 允许用户搜索和筛选可用资源 * 根据启发式方法或 AI 模型的选取实现自动上下文包含

![Example of resource context picker](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2025-03-26/server/resource-picker.png)
![资源上下文选择器示例](https://mintlify.s3.us-west-1.amazonaws.com/mcp/specification/2025-03-26/server/resource-picker.png)

However, implementations are free to expose resources through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.
然而，实现者可以根据自己的需求自由选择任何接口模式来公开资源——协议本身并不强制规定任何特定的用户交互模型。

## Capabilities  ## 功能

Servers that support resources **MUST** declare the `resources` capability:
支持资源的服务器 **必须** 声明 `resources` 功能：

```json
{
  "capabilities": {
    "resources": {
      "subscribe": true,
      "listChanged": true
    }
  }
}
```

The capability supports two optional features:
该功能支持两个可选特性：

* `subscribe`: whether the client can subscribe to be notified of changes to individual
  resources.
* `listChanged`: whether the server will emit notifications when the list of available
  resources changes.
* `订阅`：客户端是否可以订阅以接收对单个资源的变更通知。 * `列表变更通知`：服务器是否会在可用资源列表发生变化时发出通知。

Both `subscribe` and `listChanged` are optional—servers can support neither,
either, or both:
`subscribe` 和 `listChanged` 都是可选的——服务器可以支持其中之一、两者或都不支持：

```json
{
  "capabilities": {
    "resources": {} // Neither feature supported
  }
}
```
```json { "capabilities": { "resources": {} // 两种功能均不支持 } } ```

```json
{
  "capabilities": {
    "resources": {
      "subscribe": true // Only subscriptions supported
    }
  }
}
```
```json { "capabilities": { "resources": { "subscribe": true // 仅支持订阅 } } } ```

```json
{
  "capabilities": {
    "resources": {
      "listChanged": true // Only list change notifications supported
    }
  }
}
```
```json { "capabilities": { "resources": { "listChanged": true // 仅支持列表变更通知 } } } ```

## Protocol Messages  ## 协议消息

### Listing Resources  ### 资源列表

To discover available resources, clients send a `resources/list` request. This operation
supports [pagination](/specification/2025-03-26/server/utilities/pagination).
要发现可用资源，客户端发送 `resources/list` 请求。此操作支持[分页](/specification/2025-03-26/server/utilities/pagination)。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "method": "资源/列表", "params": { "游标": "可选游标值" } } ```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resources": [
      {
        "uri": "file:///project/src/main.rs",
        "name": "main.rs",
        "description": "Primary application entry point",
        "mimeType": "text/x-rust"
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### Reading Resources  ### 读取资源

To retrieve resource contents, clients send a `resources/read` request:
为了获取资源内容，客户端发送 `resources/read` 请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "resources/read",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "contents": [
      {
        "uri": "file:///project/src/main.rs",
        "mimeType": "text/x-rust",
        "text": "fn main() {\n    println!(\"Hello world!\");\n}"
      }
    ]
  }
}
```

### Resource Templates  ### 资源模板

Resource templates allow servers to expose parameterized resources using
[URI templates](https://datatracker.ietf.org/doc/html/rfc6570). Arguments may be
auto-completed through [the completion API](/specification/2025-03-26/server/utilities/completion).
资源模板允许服务器通过[URI 模板](https://datatracker.ietf.org/doc/html/rfc6570)公开参数化资源。参数可以通过[完成 API](/specification/2025-03-26/server/utilities/completion)自动补全。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/templates/list"
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "resourceTemplates": [
      {
        "uriTemplate": "file:///{path}",
        "name": "Project Files",
        "description": "Access files in the project directory",
        "mimeType": "application/octet-stream"
      }
    ]
  }
}
```

### List Changed Notification
### 列表变更通知

When the list of available resources changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:
当可用资源列表发生变化时，声明了`listChanged`能力的服务器**应当**发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/list_changed"
}
```

### Subscriptions  ### 订阅

The protocol supports optional subscriptions to resource changes. Clients can subscribe
to specific resources and receive notifications when they change:
该协议支持可选的资源变更订阅。客户端可以订阅特定资源，并在资源发生变化时接收通知：

**Subscribe Request:**  **订阅请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**Update Notification:**  **更新通知：**

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

## Message Flow  消息流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client,Server: Resource Discovery
    Client->>Server: resources/list
    Server-->>Client: List of resources
客户端，服务器：资源发现客户端->>服务器：resources/list 服务器-->>客户端：资源列表

    Note over Client,Server: Resource Access
    Client->>Server: resources/read
    Server-->>Client: Resource contents
客户端，服务器：资源访问客户端>>>服务器：资源/读取服务器-->>客户端：资源内容

    Note over Client,Server: Subscriptions
    Client->>Server: resources/subscribe
    Server-->>Client: Subscription confirmed
客户端，服务器：订阅 客户端->>服务器：resources/subscribe 服务器-->>客户端：订阅确认

    Note over Client,Server: Updates
    Server--)Client: notifications/resources/updated
    Client->>Server: resources/read
    Server-->>Client: Updated contents
```
客户端，服务器：更新 服务器--)客户端：notifications/resources/updated 客户端->>服务器：resources/read 服务器-->>客户端：更新内容

## Data Types  数据类型

### Resource  ### 资源

A resource definition includes:
资源定义包括：

* `uri`: Unique identifier for the resource
* `name`: Human-readable name
* `description`: Optional description
* `mimeType`: Optional MIME type
* `size`: Optional size in bytes
* `uri`: 资源的唯一标识符 * `name`: 可读性名称 * `description`: 可选描述 * `mimeType`: 可选 MIME 类型 * `size`: 可选字节数大小

### Resource Contents  ### 资源内容

Resources can contain either text or binary data:
资源可以包含文本或二进制数据：

#### Text Content  #### 文本内容

```json
{
  "uri": "file:///example.txt",
  "mimeType": "text/plain",
  "text": "Resource content"
}
```
```json { "uri": "file:///example.txt", "mimeType": "text/plain", "text": "资源内容" } ```

#### Binary Content  二进制内容

```json
{
  "uri": "file:///example.png",
  "mimeType": "image/png",
  "blob": "base64-encoded-data"
}
```

## Common URI Schemes  常见 URI 方案

The protocol defines several standard URI schemes. This list not
exhaustive—implementations are always free to use additional, custom URI schemes.
协议定义了多个标准 URI 方案。此列表非详尽——实现者始终可以自由使用额外的、自定义的 URI 方案。

### https\://  ### https://

Used to represent a resource available on the web.
用于表示网络上可用的资源。

Servers **SHOULD** use this scheme only when the client is able to fetch and load the
resource directly from the web on its own—that is, it doesn’t need to read the resource
via the MCP server.
服务器**应**仅当客户端能够独立从网络获取并加载资源时才使用此方案——也就是说，它不需要通过 MCP 服务器读取资源。

For other use cases, servers **SHOULD** prefer to use another URI scheme, or define a
custom one, even if the server will itself be downloading resource contents over the
internet.
对于其他用例，服务器**应**优先使用其他 URI 方案，或者定义一个自定义方案，即使服务器本身会从互联网下载资源内容。

### file://  文件://

Used to identify resources that behave like a filesystem. However, the resources do not
need to map to an actual physical filesystem.
用于标识类似文件系统的资源。然而，这些资源不需要映射到实际的物理文件系统。

MCP servers **MAY** identify file:// resources with an
[XDG MIME type](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14),
like `inode/directory`, to represent non-regular files (such as directories) that don’t
otherwise have a standard MIME type.
MCP 服务器**可能**使用[XDG MIME 类型](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14)来标识 file://资源，例如`inode/directory`，以表示那些没有标准 MIME 类型的非常规文件（如目录）。

### git://

Git version control integration.
Git 版本控制集成。

## Error Handling  错误处理

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:
服务器 **应当** 返回标准 JSON-RPC 错误以处理常见失败情况：

* Resource not found: `-32002`
* Internal errors: `-32603`
* 资源未找到：`-32002` * 内部错误：`-32603`

Example error:  示例错误：

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "error": {
    "code": -32002,
    "message": "Resource not found",
    "data": {
      "uri": "file:///nonexistent.txt"
    }
  }
}
```

## Security Considerations
安全注意事项

1. Servers **MUST** validate all resource URIs
2. Access controls **SHOULD** be implemented for sensitive resources
3. Binary data **MUST** be properly encoded
4. Resource permissions **SHOULD** be checked before operations
1. 服务器 **必须** 验证所有资源 URI 2. 对于敏感资源，**应当** 实施访问控制 3. 二进制数据 **必须** 正确编码 4. 在操作之前，**应当** 检查资源权限


# Tools
Source: https://modelcontextprotocol.io/specification/2025-03-26/server/tools
# 工具来源：https://modelcontextprotocol.io/specification/2025-03-26/server/tools



<Info>**Protocol Revision**: 2025-03-26</Info>
<信息>**协议版本**: 2025-03-26

The Model Context Protocol (MCP) allows servers to expose tools that can be invoked by
language models. Tools enable models to interact with external systems, such as querying
databases, calling APIs, or performing computations. Each tool is uniquely identified by
a name and includes metadata describing its schema.
模型上下文协议（MCP）允许服务器暴露可以被语言模型调用的工具。工具使模型能够与外部系统交互，例如查询数据库、调用 API 或执行计算。每个工具都由一个名称唯一标识，并包括描述其模式的元数据。

## User Interaction Model
## 用户交互模型

Tools in MCP are designed to be **model-controlled**, meaning that the language model can
discover and invoke tools automatically based on its contextual understanding and the
user's prompts.
MCP 中的工具设计为**模型控制**，这意味着语言模型可以根据其上下文理解和用户的提示自动发现和调用工具。

However, implementations are free to expose tools through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.
然而，实现者可以自由选择任何适合他们需求的接口模式来公开工具——协议本身并不强制任何特定的用户交互模型。

<Warning>
  For trust & safety and security, there **SHOULD** always
  be a human in the loop with the ability to deny tool invocations.
<警告>为了信任与安全以及安全起见，**应当**始终有人在场，并具有拒绝工具调用的能力。

  Applications **SHOULD**:
应用程序 **应当**：

  * Provide UI that makes clear which tools are being exposed to the AI model
  * Insert clear visual indicators when tools are invoked
  * Present confirmation prompts to the user for operations, to ensure a human is in the
    loop
</Warning>
提供清晰的 UI，以明确展示哪些工具被暴露给 AI 模型；在调用工具时插入清晰的视觉指示；向用户呈现确认提示，以确保人类参与其中

## Capabilities  ## 功能

Servers that support tools **MUST** declare the `tools` capability:
服务器支持工具**必须**声明`tools`功能：

```json
{
  "capabilities": {
    "tools": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the server will emit notifications when the list of
available tools changes.
`listChanged` 表示服务器是否会在可用工具列表发生变化时发出通知。

## Protocol Messages  ## 协议消息

### Listing Tools  ### 工具列表

To discover available tools, clients send a `tools/list` request. This operation supports
[pagination](/specification/2025-03-26/server/utilities/pagination).
为了发现可用的工具，客户端发送一个 `tools/list` 请求。此操作支持[分页](/specification/2025-03-26/server/utilities/pagination)。

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "description": "Get current weather information for a location",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "City name or zip code"
            }
          },
          "required": ["location"]
        }
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "result": { "tools": [ { "name": "get_weather", "description": "获取当前位置的天气信息", "inputSchema": { "type": "object", "properties": { "location": { "type": "string", "description": "城市名称或邮编" } }, "required": ["location"] } } ], "nextCursor": "next-page-cursor" } } ```

### Calling Tools  ### 调用工具

To invoke a tool, clients send a `tools/call` request:
要调用工具，客户端发送 `tools/call` 请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "New York"
    }
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Current weather in New York:\nTemperature: 72°F\nConditions: Partly cloudy"
      }
    ],
    "isError": false
  }
}
```

### List Changed Notification
### 列表变更通知

When the list of available tools changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:
当可用工具列表发生变化时，声明了 `listChanged` 功能的服务器 **应当** 发送通知：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}
```

## Message Flow  消息流程

```mermaid
sequenceDiagram
    participant LLM
    participant Client
    participant Server
参与者 LLM 参与者 客户端 参与者 服务器

    Note over Client,Server: Discovery
    Client->>Server: tools/list
    Server-->>Client: List of tools
客户端、服务器：发现 客户端->>服务器：工具列表 服务器-->>客户端：工具列表

    Note over Client,LLM: Tool Selection
    LLM->>Client: Select tool to use
客户端，LLM：工具选择 LLM->>客户端：选择要使用的工具

    Note over Client,Server: Invocation
    Client->>Server: tools/call
    Server-->>Client: Tool result
    Client->>LLM: Process result
客户端、服务器：调用 客户端->>服务器：工具调用 服务器-->>客户端：工具结果 客户端->>LLM：处理结果

    Note over Client,Server: Updates
    Server--)Client: tools/list_changed
    Client->>Server: tools/list
    Server-->>Client: Updated tools
```
客户端、服务器：更新 服务器--)客户端：工具变更列表 客户端->>服务器：工具列表 服务器-->>客户端：更新后的工具列表

## Data Types  数据类型

### Tool  工具

A tool definition includes:
工具定义包括：

* `name`: Unique identifier for the tool
* `description`: Human-readable description of functionality
* `inputSchema`: JSON Schema defining expected parameters
* `annotations`: optional properties describing tool behavior
* `name`: 工具的唯一标识符 * `description`: 功能的可读描述 * `inputSchema`: 定义预期参数的 JSON Schema * `annotations`: 描述工具行为的可选属性

<Warning>For trust & safety and security, clients **MUST** consider
tool annotations to be untrusted unless they come from trusted servers.</Warning>
<警告>为了信任与安全以及安全性，客户端 **必须** 将工具注释视为不可信，除非它们来自受信任的服务器。

### Tool Result  ### 工具结果

Tool results can contain multiple content items of different types:
工具结果可以包含多种类型的内容项：

#### Text Content  #### 文本内容

```json
{
  "type": "text",
  "text": "Tool result text"
}
```
```json { "type": "text", "text": "工具结果文本" } ```

#### Image Content  图像内容

```json
{
  "type": "image",
  "data": "base64-encoded-data",
  "mimeType": "image/png"
}
```

#### Audio Content  #### 音频内容

```json
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}
```

#### Embedded Resources  #### 嵌入式资源

[Resources](/specification/2025-03-26/server/resources) **MAY** be embedded, to provide additional context
or data, behind a URI that can be subscribed to or fetched again by the client later:
[资源](/specification/2025-03-26/server/resources) **可以** 嵌入，以提供额外的上下文或数据，在客户端可以订阅或稍后再次获取的 URI 后面：

```json
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "Resource content"
  }
}
```
```json { "type": "resource", "resource": { "uri": "resource://example", "mimeType": "text/plain", "text": "资源内容" } } ```

## Error Handling  错误处理

Tools use two error reporting mechanisms:
工具使用两种错误报告机制：

1. **Protocol Errors**: Standard JSON-RPC errors for issues like:
1. **协议错误**：标准 JSON-RPC 错误，例如：

   * Unknown tools
   * Invalid arguments
   * Server errors
* 未知工具 * 无效参数 * 服务器错误

2. **Tool Execution Errors**: Reported in tool results with `isError: true`:
   * API failures
   * Invalid input data
   * Business logic errors
**工具执行错误**：在工具结果中报告，`isError: true`：* API 故障 * 无效输入数据 * 业务逻辑错误

Example protocol error:  示例协议错误：

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "error": {
    "code": -32602,
    "message": "Unknown tool: invalid_tool_name"
  }
}
```
```json { "jsonrpc": "2.0", "id": 3, "error": { "code": -32602, "message": "未知工具：invalid_tool_name" } } ```

Example tool execution error:
示例工具执行错误：

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Failed to fetch weather data: API rate limit exceeded"
      }
    ],
    "isError": true
  }
}
```

## Security Considerations
安全注意事项

1. Servers **MUST**:  1. 服务器 **必须**：

   * Validate all tool inputs
   * Implement proper access controls
   * Rate limit tool invocations
   * Sanitize tool outputs
* 验证所有工具输入 * 实施适当的访问控制 * 限制工具调用频率 * 清理工具输出

2. Clients **SHOULD**:
   * Prompt for user confirmation on sensitive operations
   * Show tool inputs to the user before calling the server, to avoid malicious or
     accidental data exfiltration
   * Validate tool results before passing to LLM
   * Implement timeouts for tool calls
   * Log tool usage for audit purposes
2. 客户端 **应该**： * 在敏感操作前提示用户确认 * 在调用服务器前向用户展示工具输入，以避免恶意或意外数据泄露 * 在传递给 LLM 之前验证工具结果 * 实施工具调用的超时机制 * 记录工具使用情况以供审计


# Completion
Source: https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/completion
# 完成源：https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/completion



<Info>**Protocol Revision**: 2025-03-26</Info>
<信息>**协议版本**: 2025-03-26

The Model Context Protocol (MCP) provides a standardized way for servers to offer
argument autocompletion suggestions for prompts and resource URIs. This enables rich,
IDE-like experiences where users receive contextual suggestions while entering argument
values.
模型上下文协议（MCP）为服务器提供了一种标准化的方式，以便为提示和资源 URI 提供参数自动补全建议。这使用户在输入参数值时能够获得丰富的、类似 IDE 的体验。

## User Interaction Model
## 用户交互模型

Completion in MCP is designed to support interactive user experiences similar to IDE code
completion.
MCP 中的完成功能旨在支持类似于 IDE 代码补全的交互式用户体验。

For example, applications may show completion suggestions in a dropdown or popup menu as
users type, with the ability to filter and select from available options.
例如，应用程序可以在用户输入时显示下拉菜单或弹出菜单中的完成建议，并能够过滤和选择可用选项。

However, implementations are free to expose completion through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.
然而，实现者可以自由选择任何适合他们需求的用户界面模式来展示完成功能——协议本身并不强制任何特定的用户交互模型。

## Capabilities  ## 功能

Servers that support completions **MUST** declare the `completions` capability:
支持补全的服务器 **必须** 声明 `completions` 能力：

```json
{
  "capabilities": {
    "completions": {}
  }
}
```

## Protocol Messages  ## 协议消息

### Requesting Completions
### 请求补全

To get completion suggestions, clients send a `completion/complete` request specifying
what is being completed through a reference type:
要获取补全建议，客户端发送一个指定通过引用类型进行补全的 `completion/complete` 请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "completion/complete",
  "params": {
    "ref": {
      "type": "ref/prompt",
      "name": "code_review"
    },
    "argument": {
      "name": "language",
      "value": "py"
    }
  }
}
```

**Response:**  **响应：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "completion": {
      "values": ["python", "pytorch", "pyside"],
      "total": 10,
      "hasMore": true
    }
  }
}
```
```json { "jsonrpc": "2.0", "id": 1, "result": { "completion": { "values": ["python", "pytorch", "pyside"], "total": 10, "hasMore": true } } } ``` 
翻译结果：
```json { "jsonrpc": "2.0", "id": 1, "result": { "completion": { "values": ["python", "pytorch", "pyside"], "total": 10, "hasMore": true } } } ```

### Reference Types  ### 参考类型

The protocol supports two types of completion references:
该协议支持两种完成引用类型：

| Type           | Description                 | Example                                             |
| -------------- | --------------------------- | --------------------------------------------------- |
| `ref/prompt`   | References a prompt by name | `{"type": "ref/prompt", "name": "code_review"}`     |
| `ref/resource` | References a resource URI   | `{"type": "ref/resource", "uri": "file:///{path}"}` |
| Type | 描述 | 示例 | | -------------- | --------------------------- | --------------------------------------------------- | | `ref/prompt` | 通过名称引用提示 | `{"type": "ref/prompt", "name": "code_review"}` | | `ref/resource` | 引用资源 URI | `{"type": "ref/resource", "uri": "file:///{path}"}` |

### Completion Results  ### 完成结果

Servers return an array of completion values ranked by relevance, with:
服务器返回一个按相关性排序的完成值数组，包括：

* Maximum 100 items per response
* Optional total number of available matches
* Boolean indicating if additional results exist
* 每个响应最多 100 个项目 * 可选的总匹配数 * 表示是否存在更多结果的布尔值

## Message Flow  消息流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client: User types argument
    Client->>Server: completion/complete
    Server-->>Client: Completion suggestions
客户端备注：用户输入参数 客户端->>服务器：完成/complete 服务器-->>客户端：完成建议

    Note over Client: User continues typing
    Client->>Server: completion/complete
    Server-->>Client: Refined suggestions
```
客户端备注：用户继续输入 客户端->>服务器：完成/complete 服务器-->>客户端：细化建议 ```

## Data Types  数据类型

### CompleteRequest  ### 完成请求

* `ref`: A `PromptReference` or `ResourceReference`
* `argument`: Object containing:
  * `name`: Argument name
  * `value`: Current value
* `ref`: 一个 `提示引用` 或 `资源引用` * `argument`: 包含以下内容的对象: * `name`: 参数名称 * `value`: 当前值

### CompleteResult  ### 完成结果

* `completion`: Object containing:
  * `values`: Array of suggestions (max 100)
  * `total`: Optional total matches
  * `hasMore`: Additional results flag
* `completion`: 包含以下内容的对象: * `values`: 最大 100 个建议的数组 * `total`: 可选的总匹配数 * `hasMore`: 额外结果标志

## Error Handling  错误处理

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:
服务器 **应当** 返回标准 JSON-RPC 错误以处理常见失败情况：

* Method not found: `-32601` (Capability not supported)
* Invalid prompt name: `-32602` (Invalid params)
* Missing required arguments: `-32602` (Invalid params)
* Internal errors: `-32603` (Internal error)
* 方法未找到：`-32601`（功能不支持） * 无效提示名称：`-32602`（无效参数） * 缺少必需参数：`-32602`（无效参数） * 内部错误：`-32603`（内部错误）

## Implementation Considerations
## 实施注意事项

1. Servers **SHOULD**:  1. 服务器 **应当**：

   * Return suggestions sorted by relevance
   * Implement fuzzy matching where appropriate
   * Rate limit completion requests
   * Validate all inputs
*按相关性排序建议* 在适当的地方实现模糊匹配 *限制完成请求的速率* 验证所有输入

2. Clients **SHOULD**:
   * Debounce rapid completion requests
   * Cache completion results where appropriate
   * Handle missing or partial results gracefully
2. 客户 **应**： *防抖快速完成请求* 在适当的地方缓存完成结果 *优雅地处理缺失或部分结果

## Security  ## 安全

Implementations **MUST**:
实现必须：

* Validate all completion inputs
* Implement appropriate rate limiting
* Control access to sensitive suggestions
* Prevent completion-based information disclosure
*验证所有完成输入* 实施适当的速率限制*控制对敏感建议的访问*防止基于完成的情报泄露


# Logging
Source: https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/logging
# 日志来源：https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/logging



<Info>**Protocol Revision**: 2025-03-26</Info>
<信息>**协议版本**: 2025-03-26

The Model Context Protocol (MCP) provides a standardized way for servers to send
structured log messages to clients. Clients can control logging verbosity by setting
minimum log levels, with servers sending notifications containing severity levels,
optional logger names, and arbitrary JSON-serializable data.
模型上下文协议（MCP）为服务器向客户端发送结构化日志消息提供了一种标准化方式。客户端可以通过设置最小日志级别来控制日志详细程度，服务器发送包含严重级别、可选的记录器名称和任意可序列化为 JSON 的数据的通知。

## User Interaction Model
## 用户交互模型

Implementations are free to expose logging through any interface pattern that suits their
needs—the protocol itself does not mandate any specific user interaction model.
实现可以自由选择通过任何适合其需求的接口模式来公开日志记录——协议本身并不强制任何特定的用户交互模型。

## Capabilities  ## 功能

Servers that emit log message notifications **MUST** declare the `logging` capability:
发出日志消息通知的服务器 **必须** 声明 `logging` 功能：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

## Log Levels  ## 日志级别

The protocol follows the standard syslog severity levels specified in
[RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1):
协议遵循[RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1)中指定的标准 syslog 严重性级别：

| Level     | Description                      | Example Use Case           |
| --------- | -------------------------------- | -------------------------- |
| debug     | Detailed debugging information   | Function entry/exit points |
| info      | General informational messages   | Operation progress updates |
| notice    | Normal but significant events    | Configuration changes      |
| warning   | Warning conditions               | Deprecated feature usage   |
| error     | Error conditions                 | Operation failures         |
| critical  | Critical conditions              | System component failures  |
| alert     | Action must be taken immediately | Data corruption detected   |
| emergency | System is unusable               | Complete system failure    |
| 级别 | 描述 | 示例用例 | | --------- | -------------------------------- | -------------------------- | | debug | 详细调试信息 | 函数入口/退出点 | | info | 一般信息性消息 | 操作进度更新 | | notice | 正常但重要的事件 | 配置更改 | | warning | 警告条件 | 已弃用功能使用 | | error | 错误条件 | 操作失败 | | critical | 临界条件 | 系统组件故障 | | alert | 立即采取行动 | 数据损坏检测 | | emergency | 系统不可用 | 完全系统故障 |

## Protocol Messages  ## 协议消息

### Setting Log Level  ### 设置日志级别

To configure the minimum log level, clients **MAY** send a `logging/setLevel` request:
要配置最小日志级别，客户端**可以**发送`logging/setLevel`请求：

**Request:**  **请求：**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "logging/setLevel",
  "params": {
    "level": "info"
  }
}
```

### Log Message Notifications
### 日志消息通知

Servers send log messages using `notifications/message` notifications:
服务器使用 `notifications/message` 通知发送日志消息：

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/message",
  "params": {
    "level": "error",
    "logger": "database",
    "data": {
      "error": "Connection failed",
      "details": {
        "host": "localhost",
        "port": 5432
      }
    }
  }
}
```
```json { "jsonrpc": "2.0", "method": "notifications/message", "params": { "level": "error", "logger": "database", "data": { "error": "连接失败", "details": { "host": "localhost", "port": 5432 } } } } ```

## Message Flow  消息流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Note over Client,Server: Configure Logging
    Client->>Server: logging/setLevel (info)
    Server-->>Client: Empty Result
客户端，服务器：配置日志 客户端->>服务器：logging/setLevel (info) 服务器-->>客户端：空结果

    Note over Client,Server: Server Activity
    Server--)Client: notifications/message (info)
    Server--)Client: notifications/message (warning)
    Server--)Client: notifications/message (error)
客户端，服务器：服务器活动 服务器--)客户端：notifications/message (info) 服务器--)客户端：notifications/message (warning) 服务器--)客户端：notifications/message (error)

    Note over Client,Server: Level Change
    Client->>Server: logging/setLevel (error)
    Server-->>Client: Empty Result
    Note over Server: Only sends error level<br/>and above
```
客户端，服务器：级别变更 客户端->>服务器：logging/setLevel (error) 服务器-->>客户端：空结果 服务器：仅发送错误级别及以上 ```

## Error Handling  错误处理

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:
服务器 **应当** 返回标准 JSON-RPC 错误以处理常见失败情况：

* Invalid log level: `-32602` (Invalid params)
* Configuration errors: `-32603` (Internal error)
* 无效日志级别：`-32602`（无效参数）* 配置错误：`-32603`（内部错误）

## Implementation Considerations
## 实施注意事项

1. Servers **SHOULD**:  1. 服务器 **应当**：

   * Rate limit log messages
   * Include relevant context in data field
   * Use consistent logger names
   * Remove sensitive information
* 限制速率的日志消息 * 在数据字段中包含相关上下文 * 使用一致的日志记录器名称 * 删除敏感信息

2. Clients **MAY**:
   * Present log messages in the UI
   * Implement log filtering/search
   * Display severity visually
   * Persist log messages
2. 客户**可以**：* 在 UI 中显示日志消息 * 实现日志过滤/搜索 * 可视化显示严重性 * 持久化日志消息

## Security  ## 安全

1. Log messages **MUST NOT** contain:
1. 日志消息**不得**包含：

   * Credentials or secrets
   * Personal identifying information
   * Internal system details that could aid attacks
凭证或机密 * 个人身份信息 * 可能帮助攻击的内部系统细节

2. Implementations **SHOULD**:
   * Rate limit messages
   * Validate all data fields
   * Control log access
   * Monitor for sensitive content
应当：* 限制消息速率 * 验证所有数据字段 * 控制日志访问 * 监测敏感内容


# Pagination
Source: https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/pagination
分页来源：https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/pagination



<Info>**Protocol Revision**: 2025-03-26</Info>
<信息>**协议版本**: 2025-03-26

The Model Context Protocol (MCP) supports paginating list operations that may return
large result sets. Pagination allows servers to yield results in smaller chunks rather
than all at once.
模型上下文协议（MCP）支持分页列表操作，可能返回大量结果集。分页允许服务器分批次返回结果，而不是一次性返回所有结果。

Pagination is especially important when connecting to external services over the
internet, but also useful for local integrations to avoid performance issues with large
data sets.
分页在连接互联网上的外部服务时尤为重要，但对于避免大型数据集的性能问题，在本地集成中也非常有用。

## Pagination Model  

Pagination in MCP uses an opaque cursor-based approach, instead of numbered pages.
MCP 中的分页使用基于不可见游标的策略，而不是编号的页面。

* The **cursor** is an opaque string token, representing a position in the result set
* **Page size** is determined by the server, and clients **MUST NOT** assume a fixed page
  size
* **游标**是一个不可见的字符串令牌，表示结果集中的位置 * **页面大小**由服务器确定，客户端**不得**假设页面大小固定

## Response Format  响应格式

Pagination starts when the server sends a **response** that includes:  

* The current page of results
* An optional `nextCursor` field if more results exist  

```json
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {
    "resources": [...],
    "nextCursor": "eyJwYWdlIjogM30="
  }
}
```

## Request Format  请求格式

After receiving a cursor, the client can *continue* paginating by issuing a request
including that cursor:
接收到游标后，客户端可以通过发送包含该游标的请求来 *继续* 分页：

```json
{
  "jsonrpc": "2.0",
  "method": "resources/list",
  "params": {
    "cursor": "eyJwYWdlIjogMn0="
  }
}
```  

## Pagination Flow  ## 分页流程

```mermaid
sequenceDiagram
    participant Client
    participant Server
```mermaid sequenceDiagram participant 客户端 participant 服务器

    Client->>Server: List Request (no cursor)
    loop Pagination Loop
      Server-->>Client: Page of results + nextCursor
      Client->>Server: List Request (with cursor)
    end
```
客户端->服务器：列表请求（无游标）循环 分页循环 服务器-->>客户端：结果页 + 下一个游标 客户端->服务器：列表请求（带有游标）结束 ```

## Operations Supporting Pagination
支持分页操作

The following MCP operations support pagination:
以下 MCP 操作支持分页：

* `resources/list` - List available resources
* `resources/templates/list` - List resource templates
* `prompts/list` - List available prompts
* `tools/list` - List available tools
* `resources/list` - 列出可用资源 * `resources/templates/list` - 列出资源模板 * `prompts/list` - 列出可用提示 * `tools/list` - 列出可用工具

## Implementation Guidelines
实施指南

1. Servers **SHOULD**:  1. 服务器 **应当**：

   * Provide stable cursors
   * Handle invalid cursors gracefully  

2. Clients **SHOULD**:  2. 客户端 **应当**：

   * Treat a missing `nextCursor` as the end of results
   * Support both paginated and non-paginated flows  

3. Clients **MUST** treat cursors as opaque tokens:
   * Don't make assumptions about cursor format
   * Don't attempt to parse or modify cursors
   * Don't persist cursors across sessions
客户 **必须** 将游标视为不透明令牌：* 不要对游标格式做出假设 * 不要尝试解析或修改游标 * 不要在会话之间持久化游标

## Error Handling  错误处理

Invalid cursors **SHOULD** result in an error with code -32602 (Invalid params).
无效的游标 **应** 导致代码为 -32602 的错误（无效参数）。


# Contributions
Source: https://modelcontextprotocol.io/specification/contributing  



We welcome contributions from the community! Please review our
[contributing guidelines](https://github.com/modelcontextprotocol/specification/blob/main/CONTRIBUTING.md)
for details on how to submit changes.  

All contributors must adhere to our
[Code of Conduct](https://github.com/modelcontextprotocol/specification/blob/main/CODE_OF_CONDUCT.md).  

For questions and discussions, please use
[GitHub Discussions](https://github.com/modelcontextprotocol/specification/discussions).  


# Versioning
Source: https://modelcontextprotocol.io/specification/versioning  



The Model Context Protocol uses string-based version identifiers following the format
`YYYY-MM-DD`, to indicate the last date backwards incompatible changes were made.  

<Info>The protocol version will *not* be incremented when the
protocol is updated, as long as the changes maintain backwards compatibility. This allows
for incremental improvements while preserving interoperability.</Info>  

## Revisions  

Revisions may be marked as:  

* **Draft**: in-progress specifications, not yet ready for consumption.
* **Current**: the current protocol version, which is ready for use and may continue to
  receive backwards compatible changes.
* **Final**: past, complete specifications that will not be changed.  

The **current** protocol version is [**2025-03-26**](/specification/2025-03-26/).  

## Negotiation  

Version negotiation happens during
[initialization](/specification/2025-03-26/basic/lifecycle#initialization). Clients and
servers **MAY** support multiple protocol versions simultaneously, but they **MUST**
agree on a single version to use for the session.  

The protocol provides appropriate error handling if version negotiation fails, allowing
clients to gracefully terminate connections when they cannot find a version compatible
with the server.  


# Building MCP with LLMs
Source: https://modelcontextprotocol.io/tutorials/building-mcp-with-llms  

Speed up your MCP development using LLMs such as Claude!  

This guide will help you use LLMs to help you build custom Model Context Protocol (MCP) servers and clients. We'll be focusing on Claude for this tutorial, but you can do this with any frontier LLM.  

## Preparing the documentation  

Before starting, gather the necessary documentation to help Claude understand MCP:  

1. Visit [https://modelcontextprotocol.io/llms-full.txt](https://modelcontextprotocol.io/llms-full.txt) and copy the full documentation text
2. Navigate to either the [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) or [Python SDK repository](https://github.com/modelcontextprotocol/python-sdk)
3. Copy the README files and other relevant documentation
4. Paste these documents into your conversation with Claude  

## Describing your server  

Once you've provided the documentation, clearly describe to Claude what kind of server you want to build. Be specific about:  

* What resources your server will expose
* What tools it will provide
* Any prompts it should offer
* What external systems it needs to interact with  

For example:  例如：

```
Build an MCP server that:
- Connects to my company's PostgreSQL database
- Exposes table schemas as resources
- Provides tools for running read-only SQL queries
- Includes prompts for common data analysis tasks
```  

## Working with Claude  

When working with Claude on MCP servers:  

1. Start with the core functionality first, then iterate to add more features
2. Ask Claude to explain any parts of the code you don't understand
3. Request modifications or improvements as needed
4. Have Claude help you test the server and handle edge cases  

Claude can help implement all the key MCP features:  

* Resource management and exposure
* Tool definitions and implementations
* Prompt templates and handlers
* Error handling and logging
* Connection and transport setup  

## Best practices  

When building MCP servers with Claude:  

* Break down complex servers into smaller pieces
* Test each component thoroughly before moving on
* Keep security in mind - validate inputs and limit access appropriately
* Document your code well for future maintenance
* Follow MCP protocol specifications carefully  

## Next steps  

After Claude helps you build your server:  

1. Review the generated code carefully
2. Test the server with the MCP Inspector tool
3. Connect it to Claude.app or other MCP clients
4. Iterate based on real usage and feedback  

Remember that Claude can help you modify and improve your server as requirements change over time.  

Need more guidance? Just ask Claude specific questions about implementing MCP features or troubleshooting issues that arise.  


