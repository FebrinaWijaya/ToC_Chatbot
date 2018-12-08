from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url
from utils import send_button_message
from data import data

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
    def user_sent_something(self, event):
        return True

    def is_travelling_for_adventure(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'adventure' or text.lower() == '1'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'adventure' or text.lower() == '1'
        return False

    def is_travelling_for_historical(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'historical buildings'  or text.lower() == '2'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'historical buildings' or text.lower() == '2'
        return False

    def is_travelling_for_naturals(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'naturals' or text.lower() == '3'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'naturals'  or text.lower() == '3'
        return False

    def is_travelling_for_local_food(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'local food' or text.lower() == '4'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'local food' or text.lower() == '4'
        return False

    def on_enter_purpose(self, event):
        print("I'm entering purpose")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, data['text'])
        response = send_image_url(sender_id, "./fsm.png", 'png')
        # send_button_message(sender_id, "select one", data['buttons'])

    # def on_exit_purpose(self):
    #     print('Leaving purpose')

    def on_enter_adventure(self, event):
        print("I'm entering adventure")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Adventure']['text_to_send'])
        send_button_message(sender_id, data['Adventure']['text_button'], data['Adventure']['buttons'])

    # def on_exit_adventure(self):
    #     print('Leaving adventure')

    def on_enter_historical(self, event):
        print("I'm entering historical")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Historical Buildings']['text_to_send'])
        send_button_message(sender_id, data['Historical Buildings']['text_button'], data['Historical Buildings']['buttons'])

    # def on_exit_historical(self):
    #     print('Leaving historical')

    def on_enter_naturals(self, event):
        print("I'm entering naturals")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Naturals']['text_to_send'])
        send_button_message(sender_id, data['Naturals']['text_button'], data['Naturals']['buttons'])

    # def on_exit_naturals(self):
    #     print('Leaving naturals')

    def on_enter_local_food(self, event):
        print("I'm entering local food")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Local Food']['text_to_send'])
        send_button_message(sender_id, data['Local Food']['text_button'], data['Local Food']['buttons'])

    # def on_exit_local_food(self):
    #     print('Leaving local food')
#########################################################################

    def is_adventure_to_raja_ampat(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'raja ampat islands, west papua'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'raja ampat islands, west papua'
        return False

    def is_adventure_to_gili_island(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'gili islands, lombok'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'gili islands, lombok'
        return False

    def is_adventure_to_mount_bromo(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'mount bromo, east java'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'mount bromo, east java'
        return False

    def on_enter_raja_ampat(self, event):
        print("I'm entering raja ampat")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Adventure']['Raja Ampat Islands, West Papua']['text'])
        send_image_url(sender_id, data['Adventure']['Raja Ampat Islands, West Papua']['image'], data['Adventure']['Raja Ampat Islands, West Papua']['image_type'])
        send_button_message(sender_id, "quick options:", data['Adventure']['Raja Ampat Islands, West Papua']['buttons'])

    def on_enter_gili_island(self, event):
        print("I'm entering gili island")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Adventure']['Gili Islands, Lombok']['text'])
        send_image_url(sender_id, data['Adventure']['Gili Islands, Lombok']['image'], data['Adventure']['Gili Islands, Lombok']['image_type'])
        send_button_message(sender_id, "quick options:", data['Adventure']['Gili Islands, Lombok']['buttons'])

    def on_enter_mount_bromo(self, event):
        print("I'm entering mount_bromo")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Adventure']['Mount Bromo, East Java']['text'])
        send_image_url(sender_id, data['Adventure']['Mount Bromo, East Java']['image'], data['Adventure']['Mount Bromo, East Java']['image_type'])
        send_button_message(sender_id, "quick options:", data['Adventure']['Mount Bromo, East Java']['buttons'])

#########################################################################

    def is_historical_to_borobudur(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'borobudur temple, magelang'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'borobudur temple, magelang'
        return False

    def is_historical_to_prambanan(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'prambanan temple, yogyakarta'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'prambanan temple, yogyakarta'
        return False

    def is_historical_to_old_town(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'kota tua (old town), jakarta'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'kota tua (old town), jakarta'
        return False

    def on_enter_borobudur(self, event):
        print("I'm entering borobudur")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Historical Buildings']['Borobudur Temple, Magelang']['text'])
        send_image_url(sender_id, data['Historical Buildings']['Borobudur Temple, Magelang']['image'], data['Historical Buildings']['Borobudur Temple, Magelang']['image_type'])
        send_button_message(sender_id, "quick options:", data['Historical Buildings']['Borobudur Temple, Magelang']['buttons'])

    def on_enter_prambanan(self, event):
        print("I'm entering prambanan")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Historical Buildings']['Prambanan Temple, Yogyakarta']['text'])
        send_image_url(sender_id, data['Historical Buildings']['Prambanan Temple, Yogyakarta']['image'], data['Historical Buildings']['Prambanan Temple, Yogyakarta']['image_type'])
        send_button_message(sender_id, "quick options:", data['Historical Buildings']['Prambanan Temple, Yogyakarta']['buttons'])

    def on_enter_old_town(self, event):
        print("I'm entering old town")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Historical Buildings']['Kota Tua (Old Town), Jakarta']['text'])
        send_image_url(sender_id, data['Historical Buildings']['Kota Tua (Old Town), Jakarta']['image'], data['Historical Buildings']['Kota Tua (Old Town), Jakarta']['image_type'])
        send_button_message(sender_id, "quick options:", data['Historical Buildings']['Kota Tua (Old Town), Jakarta']['buttons'])

#########################################################################

    def is_naturals_in_bali(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'bali, the island of gods'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'bali, the island of gods'
        return False

    def is_naturals_in_lake_toba(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'lake toba, north sumatra'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'lake toba, north sumatra'
        return False

    def is_naturals_in_dieng_plateau(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'dieng plateau'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'dieng plateau'
        return False

    def on_enter_bali(self, event):
        print("I'm entering bali")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Naturals']['Bali, the Island of Gods']['text'])
        send_image_url(sender_id, data['Naturals']['Bali, the Island of Gods']['image'], data['Naturals']['Bali, the Island of Gods']['image_type'])
        send_button_message(sender_id, "quick options:", data['Naturals']['Bali, the Island of Gods']['buttons'])

    def on_enter_lake_toba(self, event):
        print("I'm entering lake toba")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Naturals']['Lake Toba, North Sumatra']['text'])
        send_image_url(sender_id, data['Naturals']['Lake Toba, North Sumatra']['image'], data['Naturals']['Lake Toba, North Sumatra']['image_type'])
        send_button_message(sender_id, "quick options:", data['Naturals']['Lake Toba, North Sumatra']['buttons'])

    def on_enter_dieng_plateau(self, event):
        print("I'm entering dieng plateau")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Naturals']['Dieng Plateau']['text'])
        send_image_url(sender_id, data['Naturals']['Dieng Plateau']['image'], data['Naturals']['Dieng Plateau']['image_type'])
        send_button_message(sender_id, "quick options:", data['Naturals']['Dieng Plateau']['buttons'])

#########################################################################

    def is_local_food_satay(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'satay'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'satay'
        return False

    def is_local_food_rendang(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'rendang'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'rendang'
        return False

    def is_local_food_fried_rice(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'fried rice'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'fried rice'
        return False

    def on_enter_satay(self, event):
        print("I'm entering satay")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Local Food']['Satay']['text'])
        send_image_url(sender_id, data['Local Food']['Satay']['image'], data['Local Food']['Satay']['image_type'])
        send_button_message(sender_id, "quick options:", data['Local Food']['Satay']['buttons'])

    def on_enter_rendang(self, event):
        print("I'm entering rendang")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Local Food']['Rendang']['text'])
        send_image_url(sender_id, data['Local Food']['Rendang']['image'], data['Local Food']['Rendang']['image_type'])
        send_button_message(sender_id, "quick options:", data['Local Food']['Rendang']['buttons'])

    def on_enter_fried_rice(self, event):
        print("I'm entering fried rice")

        sender_id = event['sender']['id']
        send_text_message(sender_id, data['Local Food']['Fried Rice']['text'])
        send_image_url(sender_id, data['Local Food']['Fried Rice']['image'], data['Local Food']['Fried Rice']['image_type'])
        send_button_message(sender_id, "quick options:", data['Local Food']['Fried Rice']['buttons'])

############################################################
    def is_next(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'see next recommended place'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'see next recommended place'
        return False

    def is_select_another_place(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'select another place'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'select another place'
        return False

    def is_change_travel_purpose(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'change my travel purpose'
        elif (event.get("postback")):
            text = event['postback']['payload']
            return text.lower() == 'change my travel purpose'
        return False