#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-17 16:07:58

import sys

from rich import print


def main(args: list) -> None:
    print(f"{args}")


if __name__ == "__main__":
    main(sys.argv[1:])

import httpx
from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Static


class WeatherApp(App):
    """App to display the current weather."""

    CSS_PATH = "weather.tcss"

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter a City")
        with VerticalScroll(id="weather-container"):
            yield Static(id="weather")

    async def on_input_changed(self, message: Input.Changed) -> None:
        """Called when the input changes"""
        await self.update_weather(message.value)

    async def update_weather(self, city: str) -> None:
        """Update the weather for the given city."""
        weather_widget = self.query_one("#weather", Static)
        if city:
            # Query the network API
            url = f"https://wttr.in/{city}"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                weather = Text.from_ansi(response.text)
                weather_widget.update(weather)
        else:
            # No city, so just blank out the weather
            weather_widget.update("")


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
