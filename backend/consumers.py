import json
import os
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
class SocketConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name="test"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({
            "type": "websocket.connect",
            "status": "connected",
            "message": "WebSocket connection established"
        })) 

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        print("WebSocket connection closed")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(f"Received message: {message}")
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message
            }
        )
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "type":"chat",
            "message": message}))