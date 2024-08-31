from typing import Optional

from embedchain.config.base_config import BaseConfig

ANSWER_RELEVANCY_PROMPT = """
请从提供的答案中提供 $num_gen_questions 个问题。
您必须提供完整的问题，如果无法提供完整的问题，则返回空字符串 ("")。
每行请仅提供一个问题，无需数字或项目符号来区分它们。
您必须仅提供问题，而无需提供其他文本。

$answer
"""  # noqa:E501


CONTEXT_RELEVANCY_PROMPT = """
请从提供的上下文中提取回答给定问题所需的相关句子。
如果未找到相关句子，或者您认为无法从给定的上下文中回答问题，则返回空字符串 ("")。
提取候选句子时，您不得对给定上下文中的句子进行任何更改或编造任何句子。
您只能提供给定上下文中的句子，而不能提供其他任何内容。

上下文：$context
问题：$question
"""  # noqa:E501

GROUNDEDNESS_ANSWER_CLAIMS_PROMPT = """
请从所提供答案的每个句子中提供一个或多个陈述。
您必须为答案的每个句子提供语义等效的陈述。
您必须提供完整的陈述，如果无法提供完整的陈述，则返回空字符串（""）。
每行请仅提供一个陈述，不带数字或项目符号。
如果提供的答案未回答所提供问题，则返回空字符串（""）。
您必须仅提供陈述，而不能提供其他文本。

$question
$answer
"""  # noqa:E501

GROUNDEDNESS_CLAIMS_INFERENCE_PROMPT = """
给定上下文和提供的声明，请为每个声明提供一个判定，无论是否可以根据给定的上下文完全推断出来。
仅使用"1"（是）、"0"（否）和"-1"（空）分别表示"是"、"否"或"空"。
您必须每行提供一个判定，仅使用"1"、"0"或"-1"作为对给定声明的判定，不能使用其他任何内容。
您必须按照声明的顺序提供判定。

上下文：
$context

声明：
$claim_statements
"""  # noqa:E501


class GroundednessConfig(BaseConfig):
    def __init__(
        self,
        model: str = "gpt-4",
        api_key: Optional[str] = None,
        answer_claims_prompt: str = GROUNDEDNESS_ANSWER_CLAIMS_PROMPT,
        claims_inference_prompt: str = GROUNDEDNESS_CLAIMS_INFERENCE_PROMPT,
    ):
        self.model = model
        self.api_key = api_key
        self.answer_claims_prompt = answer_claims_prompt
        self.claims_inference_prompt = claims_inference_prompt


class AnswerRelevanceConfig(BaseConfig):
    def __init__(
        self,
        model: str = "gpt-4",
        embedder: str = "text-embedding-ada-002",
        api_key: Optional[str] = None,
        num_gen_questions: int = 1,
        prompt: str = ANSWER_RELEVANCY_PROMPT,
    ):
        self.model = model
        self.embedder = embedder
        self.api_key = api_key
        self.num_gen_questions = num_gen_questions
        self.prompt = prompt


class ContextRelevanceConfig(BaseConfig):
    def __init__(
        self,
        model: str = "gpt-4",
        api_key: Optional[str] = None,
        language: str = "en",
        prompt: str = CONTEXT_RELEVANCY_PROMPT,
    ):
        self.model = model
        self.api_key = api_key
        self.language = language
        self.prompt = prompt
