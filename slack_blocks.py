from dataclasses import dataclass
from typing import Any

@dataclass
class BaseBlock:

    def reset_value(self) -> None:
        raise NotImplementedError("Subclasses should implement this method")
    
    def change_value(self, *args: list[Any], **kwargs: dict[str,Any]) -> None:
        raise NotImplementedError("Subclasses should implement this method")

    def append(self, *args: list[Any], **kwargs: dict[str,Any]) -> None:
        raise NotImplementedError("Subclasses should implement this method")

    def value(self) -> dict[str,Any]:
        raise NotImplementedError("Subclasses should implement this method")
    
@dataclass
class DividerBlock(BaseBlock):

    def value(self) -> dict[str,Any]:
        return {
			"type": "divider"
		}
    
@dataclass
class HeaderBlock(BaseBlock):
    title: str = ""

    def reset_value(self) -> None:
        self.title = ""

    def change_value(self, *args: list[Any], **kwargs: dict[str,Any]) -> None:
        self.title = str(kwargs.get("title", self.title))
    
    def append(self, *args: list[Any], **kwargs: dict[str,Any]) -> None:
        new_data: str = str(kwargs.get("title", ""))
        self.title = f"{self.title} {new_data}"

    def value(self) -> dict[str,Any]:
        return {
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": self.title,
				"emoji": True
			}
		}


@dataclass
class ImageBlock(BaseBlock):
    image_url: str
    title: str | None =  None
    alt_text: str = ""
    is_markdown: bool = False

    def reset_value(self) -> None:
        self.title = None
        self.alt_text = ""
        self.is_markdown = False

    def change_value(self, *args: list[Any], **kwargs: dict[str,Any]) -> None:
        self.image_url = str(kwargs.get("image_url", self.image_url))
        self.title = kwargs.get("title", self.title) # type: ignore
        self.alt_text = str(kwargs.get("alt_text", self.alt_text))
        self.is_markdown = bool(kwargs.get("is_markdown", self.is_markdown))

    def value(self) -> dict[str,Any]:
        if self.title is not None:
            return {
                "type": "image",
                "title": {
                    "type": "mrkdwn" if self.is_markdown else "plain_text",
                    "text": self.title
                },
                "image_url": self.image_url,
                "alt_text": self.alt_text
            }
        else:
            return {
                "type": "image",
                "image_url": self.image_url,
                "alt_text": self.alt_text
            }


@dataclass
class RichTextBlock(BaseBlock):
    sections: list[dict[str,Any]]
    element: list[dict[str,Any]]


@dataclass
class SlackBlock:
    blocks: list[Any]


def main():
    print(ImageBlock(image_url="").value())

main()