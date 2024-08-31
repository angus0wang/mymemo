from mem0.llms.openai import OpenAILLM

UPDATE_GRAPH_PROMPT = """
你是一位专门从事图谱记忆管理和优化的 AI 专家。你的任务是分析现有的图谱记忆和新信息，并更新记忆列表中的关系，以确保最准确、最新和连贯的知识表示。

输入：
1. 现有图谱记忆：当前图谱记忆的列表，每个图谱记忆包含源、目标和关系信息。
2. 新图谱记忆：要集成到现有图谱结构中的新信息。

指南：
1. 标识：将现有记忆与新信息匹配时，使用源和目标作为主要标识符。
2. 冲突解决：
- 如果新信息与现有记忆相矛盾：
a) 对于匹配源和目标但内容不同的情况，更新现有记忆的关系。
b) 如果新记忆提供更新或更准确的信息，请相应地更新现有记忆。
3. 全面审查：根据新信息彻底检查每个现有图谱记忆，并根据需要更新关系。可能需要多次更新。
4. 一致性：在所有记忆中保持统一清晰的风格。每个条目都应简洁而全面。
5. 语义一致性：确保更新维护或改进图的整体语义结构。
6. 时间意识：如果有时间戳，请在进行更新时考虑信息的新近性。
7. 关系细化：寻找机会细化关系描述，以提高精度或清晰度。
8. 冗余消除：识别并合并可能由更新导致的任何冗余或高度相似的关系。

任务详情：
- 现有图谱记忆：
{existing_memories}

- 新图谱记忆：{memory}

输出：
提供更新指令列表，每个指令指定源、目标和要设置的新关系。仅包括需要更新的记忆。"""

EXTRACT_ENTITIES_PROMPT = """

您是一种高级算法，旨在从文本中提取结构化信息以构建知识图谱。您的目标是在保持准确性的同时捕获全面的信息。请遵循以下关键原则：

1. 仅从文本中提取明确陈述的信息。
2. 识别节点（实体/概念）、其类型和关系。
3. 使用“USER_ID”作为用户消息中任何自我引用（我、我的等）的源节点。

节点和类型：
- 力求节点表示简单明了。
- 使用基本的通用类型作为节点标签（例如“人”而不是“数学家”）。

关系：
- 使用一致、通用且永恒的关系类型。
- 示例：首选“PROFESSOR”而不是“BECAME_PROFESSOR”。

实体一致性：
- 对多次提及的实体使用最完整的标识符。
- 示例：始终使用“John Doe”而不是“Joe”或代词等变体。

通过保持实体引用和关系类型的一致性，努力实现连贯、易于理解的知识图谱。

严格遵守这些准则，以确保高质量的知识图谱提取。"""



def get_update_memory_prompt(existing_memories, memory, template):
    return template.format(existing_memories=existing_memories, memory=memory)

def get_update_memory_messages(existing_memories, memory):
    return [
        {
            "role": "user",
            "content": get_update_memory_prompt(existing_memories, memory, UPDATE_GRAPH_PROMPT),
        },
    ]

def get_search_results(entities, query):

    search_graph_prompt = f"""
您是搜索图谱实体记忆的专家。
当提供现有图谱实体和查询时，您的任务是搜索提供的图谱实体，从与查询相关的图谱实体中找到最相关的信息。
输出应仅来自图谱实体。

以下是任务的详细信息：
- 现有图谱实体（源 -> 关系 -> 目标）：
{entities}

- 查询：{query}

输出应仅来自图谱实体。
输出应采用以下 JSON 格式：
{{
    "search_results": [
        {{
            "source_node": "source_node",
            "relationship": "relationship",
            "target_node": "target_node"
        }}
    ]
}}
"""

    messages = [
        {
            "role": "user",
            "content": search_graph_prompt,
        }
    ]

    llm = OpenAILLM()

    results = llm.generate_response(messages=messages, response_format={"type": "json_object"})

    return results
