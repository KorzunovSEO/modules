import asyncio
import logging
from requests import get
from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class ValitesMod(loader.Module):
	"""Valute converter"""
	strings = {"name": "Valutes"}

	@loader.unrestricted
	async def valutecmd(self, message):
		""".valute <Valute char code (optional)>"""
		valutes = get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").json()			
		text = []
		temp = "<b>{}</b>\n{} <code>{}</code>: {}₴ ({}{}₴)"
		for val in valutes.values():
			name = val["txt"]
			code = val["cc"]
			nom = int(val["rate"])
		if not text:
			return await utils.answer(message, "<b>Запрос неверен - ответ пуст!</b>")
		await utils.answer(message, "\n".join(text))
