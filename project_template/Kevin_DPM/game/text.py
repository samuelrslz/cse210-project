import arcade

class Text():
    

    def __init__(self):
        
        self.text = ""
        self.display_text = ""
        self.display_text_count = 0
        self.intro_text = "Hello Kevin. Your task wether you choose to accept is to find all of the professors and complete their tasks. If you look around you may be able to find some drinks to restore your stamina as well a TA who will help you increase your stamina. Best of luck! (Press 'ENTER' to continue)"
        self.simplify_text()
        
    def simplify_text(self):
        text = self.intro_text.split(" ")
        
        current_length = 0
        final_text = ""
        new_text = ""

        for word in text:
            current_length = len(new_text)
            new_length = current_length + len(word)
            if word == "continue)":
                new_text += word + " "
                final_text += new_text
            elif new_length < 35:
                new_text += word + " "

            else:
                final_text += new_text + "\n"
                new_text = ""
                new_text += word + " "


        self.intro_text = final_text
            
            

        
    def print_text(self, text, show_has_finished = False):
        # print(text)
        text_list = self.group_by_words(text)

        if self.display_text == "":
            self.display_text_count = 0
        if self.display_text.replace("\n", "") != text:
            self.display_text += text[self.display_text_count]
            # self.display_text += text_list[self.display_text_count]
            # if len(text_list[self.display_text_count]) + len(self.display_text) % 35 >= 0 and len(self.display_text) < 35 - len(text_list[self.display_text_count]):
            if self.display_text_count % 35 == 0 and self.display_text_count > 0:
                self.display_text += "\n"
            self.display_text_count += 1
        if show_has_finished:
            return self.display_text, self.display_text.replace("\n", "") == text
        else:
            return self.display_text

    def meet_prof_text(self, prof_name, show_has_finished = False):
        text = f"Professor {prof_name} wants to battle you! Press 'ENTER' to battle"
        return self.print_text(text,show_has_finished)

    def must_be_higher_level_to_battle(self, player_level, required_level, show_has_finished = False):
        text = f"You must be level {required_level} to battle me. You are at level {player_level}"
        return self.print_text(text, show_has_finished)

    def battle_prof_text(self, prof_name, prof_move, player_move, show_has_finished = False):
        text = f"Professor {prof_name} used {prof_move}. You used {player_move}."
        return self.print_text(text,show_has_finished)

    def battle_lost_text(self, show_has_finished = False):
        text = "You are out of stamina, you can't continue."
        return self.print_text(text,show_has_finished)
        
    def battle_won_text(self, additional_text, show_has_finished = False):
        text = f"Congratulations! {additional_text}"
        return self.print_text(text,show_has_finished)

    def group_by_words(self, text):
        return text.split()

    def clear_text(self):
        self.display_text = ""
        self.display_text_count = 0

# text = Text()

# text.simplify_text()
# print(text.intro_text)