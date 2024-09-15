from django import template
from store.models import Accesstoken  # Adjust the import according to your app structure

register = template.Library()

@register.simple_tag
def get_stack_balance(player_id, players, player_count, access_id):
        
        if player_count == 1:
            try:
                access_token = Accesstoken.objects.get(access_cookie=access_id)
                return access_token.bank_balance
            except Accesstoken.DoesNotExist:
                return 0  # Return zero on error (access token not found)
            except Exception as e:
                # Handle other exceptions if needed
                return 0  # Return zero on any other error

        else:
            if players is None:
                return None  # Handle the case gracefully based on your application logic
            for player in players:
                if player.player_id == player_id:
                    return int(player.token_balance)
            return None  # Handle case where player is not found

@register.simple_tag
def get_stack_balance_by_wallet(player_id, players, player_count, wallet_address):
        
        if player_count == 1:
            try:
                access_token = Accesstoken.objects.get(public_wallet_address=wallet_address)
                return access_token.bank_balance
            except Accesstoken.DoesNotExist:
                return 0  # Return zero on error (access token not found)
            except Exception as e:
                # Handle other exceptions if needed
                return 0  # Return zero on any other error

        else:
            if players is None:
                return None  # Handle the case gracefully based on your application logic
            for player in players:
                if player.player_id == player_id:
                    return int(player.token_balance)
            return None  # Handle case where player is not found

@register.simple_tag
def get_stack_player_type_by_wallet(player_id, players, player_count, wallet_address):
        
        if player_count == 1:
            print('Me')
        else:
            if players is None:
                return None  # Handle the case gracefully based on your application logic
            for player in players:
                if player.player_id == player_id:
                    return  player.player_type
            return None  # Handle case where player is not found