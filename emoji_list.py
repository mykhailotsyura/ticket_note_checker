#!/usr/bin/python
#
emoji_list = [ ':thinking_face:',':table_tennis_paddle_and_ball:',':eyes:',':thumbsup:',':crab:',':rice_cracker:',':upside_down_face:',':pray:',':ok_hand:',':face_with_rolling_eyes:',':grimacing:',
':heavy_check_mark:',':no_mouth:',':hugging_face:',':unamused:',':sweat_smile:',':scream:',':laughing:',':smoking:',':point_down:',':clap:',
':heartbeat:',':muscle:',':smirk:',':jack_o_lantern:',':disappointed_relieved:',':disappointed:',':sweat:',':fire:',':grinning:',':grin:',
':rolling_on_the_floor_laughing:',':smiley:',':smile:',':sweat_smile:',':laughing:',':wink:',':blush:',':sunglasses:',':heart_eyes:',':kissing_heart:',
':kissing:',':kissing_smiling_eyes:',':kissing_closed_eyes:',':relaxed:',':slightly_smiling_face:',':hugging_face:',':star-struck:',':thinking_face:',':face_with_raised_eyebrow:',':neutral_face:',
':expressionless:',':no_mouth:',':face_with_rolling_eyes:',':smirk:',':persevere:',':disappointed_relieved:',':open_mouth:',':zipper_mouth_face:',':hushed:',':sleepy:',
':tired_face:',':sleeping:',':relieved:',':stuck_out_tongue:',':stuck_out_tongue_winking_eye:',':stuck_out_tongue_closed_eyes:',':drooling_face:',':unamused:',':sweat:',':pensive:',
':confused:',':upside_down_face:',':astonished:',':white_frowning_face:',':slightly_frowning_face:',':confounded:',':disappointed:',':worried:',':triumph:',':frowning:',
':anguished:',':fearful:',':weary:',':exploding_head:',':grimacing:',':cold_sweat:',':scream:',':flushed:',':zany_face:',':dizzy_face:',
':rage:',':angry:',':face_with_symbols_on_mouth:',':mask:',':face_with_thermometer:',':face_with_head_bandage:',':nauseated_face:',':face_vomiting:',':sneezing_face:',':innocent:',
':face_with_cowboy_hat:',':clown_face:',':lying_face:',':shushing_face:',':face_with_hand_over_mouth:',':face_with_monocle:',':nerd_face:',':smiling_imp:',':japanese_ogre:',':japanese_goblin:',
':skull:',':ghost:',':alien:',':space_invader:',':robot_face:',':hankey:',':smiley_cat:',':smile_cat:',':joy_cat:',':heart_eyes_cat:',
':smirk_cat:',':kissing_cat:',':scream_cat:',':crying_cat_face:',':pouting_cat:',':see_no_evil:',':hear_no_evil:',':speak_no_evil:',':baby:',':child:',
':girl:',':adult:',':older_adult:',':prince:',':princess:',':person_with_headscarf:',':bearded_person:',':bride_with_veil:',':breast-feeding:',':angel:',
':santa:',':mrs_claus:',':mermaid:',':dancer:',':bath:',':sleeping_accommodation:',':speaking_head_in_silhouette:',':bust_in_silhouette:',':busts_in_silhouette:',':fencer:',
':horse_racing:',':skier:',':snowboarder:',':racing_car:',':racing_motorcycle:',':couple:',':selfie:',':muscle:',':point_left:',':point_right:',
':point_up:',':middle_finger:',':point_down:',':crossed_fingers:',':spock-hand:',':the_horns:',':call_me_hand:',':raised_hand_with_fingers_splayed:',':hand:',':ok_hand:',
':thumbsup:',':thumbsdown:',':fist:',':facepunch:',':left-facing_fist:',':right-facing_fist:',':raised_back_of_hand:',':wave:',':i_love_you_hand_sign:',':writing_hand:',
':clap:',':open_hands:',':raised_hands:',':palms_up_together:',':pray:',':handshake:',':nail_care:',':nose:',':footprints:',':eyes:',
':eye-in-speech-bubble:',':brain:',':tongue:',':lips:',':kiss:',':cupid:',':heart:',':heartbeat:',':broken_heart:',':sparkling_heart:',
':heartpulse:',':blue_heart:',':green_heart:',':yellow_heart:',':orange_heart:',':purple_heart:',':black_heart:',':gift_heart:',':revolving_hearts:',':heart_decoration:',
':heavy_heart_exclamation_mark_ornament:',':love_letter:',':anger:',':bomb:',':boom:',':sweat_drops:',':dash:',':dizzy:',':speech_balloon:',':left_speech_bubble:',
':right_anger_bubble:',':thought_balloon:',':hole:',':eyeglasses:',':dark_sunglasses:',':necktie:',':shirt:',':jeans:',':scarf:',':gloves:',
':coat:',':socks:',':dress:',':kimono:',':bikini:',':purse:',':handbag:',':pouch:',':shopping_bags:',':school_satchel:',
':athletic_shoe:',':high_heel:',':sandal:',':boot:',':crown:',':tophat:',':mortar_board:',':billed_cap:',':helmet_with_white_cross:',':prayer_beads:',
':lipstick:',':ring:',':monkey_face:',':monkey:',':gorilla:',':poodle:',':wolf:',':fox_face:',':lion_face:',':tiger:',
':leopard:',':horse:',':racehorse:',':unicorn_face:',':zebra_face:',':deer:',':water_buffalo:',':boar:',':pig_nose:',':sheep:',
':goat:',':dromedary_camel:',':camel:',':giraffe_face:',':elephant:',':rhinoceros:',':mouse:',':hamster:',':rabbit:',':chipmunk:',
':hedgehog:',':bear:',':koala:',':panda_face:',':feet:',':turkey:',':chicken:',':rooster:',':hatching_chick:',':baby_chick:',
':hatched_chick:',':bird:',':penguin:',':dove_of_peace:',':eagle:',':duck:',':frog:',':crocodile:',':turtle:',':lizard:',
':snake:',':dragon_face:',':dragon:',':sauropod:',':t-rex:',':whale:',':dolphin:',':fish:',':tropical_fish:',':blowfish:',
':shark:',':octopus:',':shell:',':crab:',':shrimp:',':squid:',':snail:',':butterfly:',':beetle:',':cricket:',
':spider:',':spider_web:',':scorpion:',':bouquet:',':cherry_blossom:',':white_flower:',':rosette:',':rose:',':wilted_flower:',':hibiscus:',
':sunflower:',':blossom:',':tulip:',':seedling:',':evergreen_tree:',':deciduous_tree:',':palm_tree:',':cactus:',':ear_of_rice:',':herb:',
':shamrock:',':maple_leaf:',':fallen_leaf:',':leaves:',':grapes:',':melon:',':watermelon:',':tangerine:',':lemon:',':banana:',
':pineapple:',':apple:',':green_apple:',':pear:',':peach:',':cherries:',':strawberry:',':kiwifruit:',':tomato:',':coconut:',
':avocado:',':eggplant:',':potato:',':carrot:',':corn:',':hot_pepper:',':cucumber:',':broccoli:',':mushroom:',':peanuts:',
':chestnut:',':bread:',':croissant:',':baguette_bread:',':pretzel:',':pancakes:',':cheese_wedge:',':poultry_leg:',':cut_of_meat:',':bacon:',
':hamburger:',':fries:',':pizza:',':hotdog:',':sandwich:',':taco:',':burrito:',':stuffed_flatbread:',':fried_egg:',':shallow_pan_of_food:',
':stew:',':bowl_with_spoon:',':green_salad:',':popcorn:',':canned_food:',':bento:',':rice_cracker:',':rice_ball:',':rice:',':curry:',
':ramen:',':spaghetti:',':sweet_potato:',':oden:',':sushi:',':fried_shrimp:',':fish_cake:',':dango:',':dumpling:',':fortune_cookie:',
':takeout_box:',':icecream:',':shaved_ice:',':ice_cream:',':doughnut:',':cookie:',':birthday:',':cake:',':chocolate_bar:',':candy:',
':lollipop:',':custard:',':baby_bottle:',':glass_of_milk:',':coffee:',':sake:',':champagne:',':wine_glass:',':cocktail:',':tropical_drink:',
':beer:',':beers:',':clinking_glasses:',':tumbler_glass:',':cup_with_straw:',':chopsticks:',':knife_fork_plate:',':fork_and_knife:',':spoon:',':hocho:',
':amphora:',':jack_o_lantern:',':christmas_tree:',':fireworks:',':sparkler:',':sparkles:',':balloon:',':tada:',':confetti_ball:',':tanabata_tree:',
':bamboo:',':dolls:',':wind_chime:',':rice_scene:',':ribbon:',':gift:',':reminder_ribbon:',':admission_tickets:',':ticket:',':medal:',
':trophy:',':sports_medal:',':first_place_medal:',':second_place_medal:',':third_place_medal:',':soccer:',':baseball:',':basketball:',':volleyball:',':football:',
':rugby_football:',':tennis:',':bowling:',':cricket_bat_and_ball:',':field_hockey_stick_and_ball:',':ice_hockey_stick_and_puck:',':table_tennis_paddle_and_ball:',':badminton_racquet_and_shuttlecock:',':boxing_glove:',':martial_arts_uniform:',
':goal_net:',':dart:',':golf:',':ice_skate:',':fishing_pole_and_fish:',':running_shirt_with_sash:',':sled:',':video_game:',':joystick:',':game_die:',
':spades:',':hearts:',':clubs:',':black_joker:',':mahjong:',':flower_playing_cards:',':earth_africa:',':earth_americas:',':earth_asia:',':globe_with_meridians:',
':world_map:',':japan:',':snow_capped_mountain:',':mountain:',':volcano:',':mount_fuji:',':camping:',':beach_with_umbrella:',':desert:',':desert_island:',
':national_park:',':stadium:',':classical_building:',':building_construction:',':house_buildings:',':cityscape:',':derelict_house_building:',':house:',':house_with_garden:',':office:',
':post_office:',':european_post_office:',':hospital:',':bank:',':hotel:',':love_hotel:',':convenience_store:',':school:',':department_store:',':factory:',
':japanese_castle:',':european_castle:',':wedding:',':tokyo_tower:',':statue_of_liberty:',':church:',':mosque:',':synagogue:',':shinto_shrine:',':kaaba:',
':fountain:',':tent:',':foggy:',':night_with_stars:',':sunrise_over_mountains:',':sunrise:',':city_sunset:',':city_sunrise:',':bridge_at_night:',':hotsprings:',
':milky_way:',':carousel_horse:',':ferris_wheel:',':roller_coaster:',':barber:',':circus_tent:',':performing_arts:',':frame_with_picture:',':slot_machine:',':steam_locomotive:',
':railway_car:',':bullettrain_side:',':bullettrain_front:',':metro:',':light_rail:',':station:',':tram:',':monorail:',':mountain_railway:',':train:',
':oncoming_bus:',':trolleybus:',':minibus:',':ambulance:',':fire_engine:',':police_car:',':oncoming_police_car:',':taxi:',':oncoming_taxi:',':oncoming_automobile:',
':blue_car:',':truck:',':articulated_lorry:',':tractor:',':bike:',':scooter:',':motor_scooter:',':busstop:',':motorway:',':railway_track:',
':fuelpump:',':rotating_light:',':traffic_light:',':vertical_traffic_light:',':construction:',':octagonal_sign:',':anchor:',':boat:',':canoe:',':speedboat:',
':passenger_ship:',':ferry:',':motor_boat:',':ship:',':airplane:',':small_airplane:',':airplane_departure:',':airplane_arriving:',':seat:',':helicopter:',
':suspension_railway:',':mountain_cableway:',':aerial_tramway:',':satellite:',':rocket:',':flying_saucer:',':bellhop_bell:',':door:',':couch_and_lamp:',':toilet:',
':shower:',':bathtub:',':hourglass:',':hourglass_flowing_sand:',':watch:',':alarm_clock:',':stopwatch:',':timer_clock:',':new_moon:',':waxing_crescent_moon:',
':first_quarter_moon:',':moon:',':full_moon:',':waning_gibbous_moon:',':last_quarter_moon:',':waning_crescent_moon:',':crescent_moon:',':new_moon_with_face:',':first_quarter_moon_with_face:',':last_quarter_moon_with_face:',
':thermometer:',':sunny:',':full_moon_with_face:',':sun_with_face:',':star:',':stars:',':cloud:',':partly_sunny:',':thunder_cloud_and_rain:',':mostly_sunny:',
':barely_sunny:',':partly_sunny_rain:',':rain_cloud:',':snow_cloud:',':lightning:',':tornado:',':wind_blowing_face:',':rainbow:',':closed_umbrella:',':umbrella:',
':umbrella_with_rain_drops:',':umbrella_on_ground:',':snowflake:',':comet:',':fire:',':droplet:',':ocean:',':mute:',':speaker:',':sound:',
':loud_sound:',':loudspeaker:',':mega:',':postal_horn:',':bell:',':no_bell:',':musical_score:',':musical_note:',':notes:',':level_slider:',
':control_knobs:',':radio:',':guitar:',':musical_keyboard:',':trumpet:',':violin:',':drum_with_drumsticks:',':calling:',':pager:',':battery:',
':electric_plug:',':computer:',':desktop_computer:',':printer:',':keyboard:',':trackball:',':minidisc:',':floppy_disk:',':movie_camera:',':film_frames:',
':film_projector:',':clapper:',':camera:',':camera_with_flash:',':video_camera:',':mag_right:',':microscope:',':telescope:',':satellite_antenna:',':candle:',
':bulb:',':flashlight:',':izakaya_lantern:',':notebook_with_decorative_cover:',':closed_book:',':book:',':green_book:',':blue_book:',':orange_book:',':books:',
':notebook:',':ledger:',':page_with_curl:',':scroll:',':page_facing_up:',':newspaper:',':rolled_up_newspaper:',':bookmark_tabs:',':bookmark:',':label:',
':dollar:',':euro:',':pound:',':credit_card:',':chart:',':currency_exchange:',':heavy_dollar_sign:',':email:',':e-mail:',':incoming_envelope:',
':outbox_tray:',':inbox_tray:',':package:',':mailbox:',':mailbox_closed:',':mailbox_with_mail:',':mailbox_with_no_mail:',':postbox:',':ballot_box_with_ballot:',':black_nib:',
':lower_left_fountain_pen:',':lower_left_ballpoint_pen:',':lower_left_paintbrush:',':lower_left_crayon:',':memo:',':briefcase:',':file_folder:',':open_file_folder:',':card_index_dividers:',':date:',
':calendar:',':spiral_note_pad:',':spiral_calendar_pad:',':card_index:',':chart_with_upwards_trend:',':chart_with_downwards_trend:',':bar_chart:',':clipboard:',':pushpin:',':round_pushpin:',
':paperclip:',':linked_paperclips:',':straight_ruler:',':triangular_ruler:',':scissors:',':card_file_box:',':file_cabinet:',':wastebasket:',':lock:',':unlock:',
':lock_with_ink_pen:',':closed_lock_with_key:',':old_key:',':hammer:',':pick:',':hammer_and_pick:',':hammer_and_wrench:',':dagger_knife:',':crossed_swords:',':shield:',
':wrench:',':nut_and_bolt:',':gear:',':compression:',':alembic:',':scales:',':link:',':chains:',':syringe:',':pill:',
':smoking:',':coffin:',':funeral_urn:',':moyai:',':oil_drum:',':crystal_ball:',':shopping_trolley:',':put_litter_in_its_place:',':potable_water:',':wheelchair:',
':mens:',':womens:',':restroom:',':baby_symbol:',':passport_control:',':customs:',':baggage_claim:',':left_luggage:',':warning:',':children_crossing:',
':no_entry:',':no_entry_sign:',':no_bicycles:',':no_smoking:',':do_not_litter:',':non-potable_water:',':no_pedestrians:',':underage:',':radioactive_sign:',':biohazard_sign:',
':back:',':soon:',':place_of_worship:',':atom_symbol:',':om_symbol:',':star_of_david:',':wheel_of_dharma:',':yin_yang:',':latin_cross:',':orthodox_cross:',
':star_and_crescent:',':peace_symbol:',':aries:',':taurus:',':gemini:',':cancer:',':virgo:',':libra:',':scorpius:',':sagittarius:',
':capricorn:',':aquarius:',':pisces:',':ophiuchus:',':repeat:',':fast_forward:',':rewind:',':double_vertical_bar:',':black_circle_for_record:',':eject:',
':cinema:',':low_brightness:',':high_brightness:',':signal_strength:',':vibration_mode:',':medical_symbol:',':recycle:',':fleur_de_lis:',':trident:',':name_badge:',
':beginner:',':white_check_mark:',':ballot_box_with_check:',':heavy_check_mark:',':heavy_multiplication_x:',':heavy_plus_sign:',':heavy_minus_sign:',':heavy_division_sign:',':curly_loop:',':loop:',
':part_alternation_mark:',':eight_spoked_asterisk:',':eight_pointed_black_star:',':sparkle:',':bangbang:',':interrobang:',':question:',':grey_question:',':grey_exclamation:',':exclamation:',
':wavy_dash:',':copyright:',':registered:',':hash:',':keycap_star:',':zero:',':eight:',':keycap_ten:',':capital_abcd:',':abcd:',
':symbols:',':cool:',':free:',':information_source:',':parking:',':koko:',':ideograph_advantage:',':accept:',':congratulations:',':secret:']
