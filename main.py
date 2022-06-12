from Booking import Booking

with Booking() as bot:
    bot.get_page()
    bot.select_place_to_go('Katowice')
    bot.select_dates('2022-06-16', '2022-07-16')
    bot.num_of_people()
    bot.paste_options_into_notepad()
