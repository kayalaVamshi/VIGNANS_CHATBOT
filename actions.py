from datetime import datetime
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTimeBasedGreet(Action):
    def name(self) -> Text:
        return "action_time_based_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_hour = datetime.now().hour
        buttons = [
            {"title": "🎓 Student", "payload": "/identify_student"},
            {"title": "👨‍🏫 Faculty", "payload": "/identify_faculty"},
            {"title": "👪 Parent", "payload": "/identify_parent"},
            {"title": "🏢 Administration", "payload": "/identify_admin"},
            {"title": "👋 Guest", "payload": "/identify_guest"}
        ]

        if 5 <= current_hour < 12:
            message = "Good morning! ☀️ Welcome to Vignan's Institute Chatbot."
        elif 12 <= current_hour < 17:
            message = "Good afternoon! 🌞 Welcome to Vignan's Institute Chatbot."
        elif 17 <= current_hour < 22:
            message = "Good evening! 🌙 Welcome to Vignan's Institute Chatbot."
        else:
            message = "Welcome to Vignan's Institute Chatbot!"

        dispatcher.utter_message(text=message, buttons=buttons)
        return []

class ActionFestivalGreet(Action):
    def name(self) -> Text:
        return "action_festival_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = datetime.now().date()
        buttons = [{"title": "Continue to Services", "payload": "/continue"}]

        # January
        if today.month == 1:
            if today.day == 1:
                message = "Happy New Year! 🎊 Welcome to Vignan's Institute Chatbot."
            elif 13 <= today.day <= 16:
                message = "Happy Sankranti/Pongal! 🪁 Welcome to Vignan's Institute Chatbot."
            elif today.day == 26:
                message = "Happy Republic Day! 🇮🇳 Welcome to Vignan's Institute Chatbot."
            else:
                message = "Welcome to Vignan's Institute Chatbot!"
        else:
            message = "Welcome to Vignan's Institute Chatbot!"

        dispatcher.utter_message(text=message, buttons=buttons)
        return []