from channels.generic.websocket import AsyncWebsocketConsumer
import json
 
class TokenAuthConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.send(text_data=json.loads({
            "message": "Connection established."
        }))
 
    async def disconnect(self, close_code):
        await self.close()
 
    async def receive(self, text_data):
        text_data = json.dumps(text_data)
        await self.send(text_data=json.loads({
            "message": "This is being sent back",
            "text_data": text_data
        }))