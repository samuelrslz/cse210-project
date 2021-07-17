import arcade

class Text():
    

    def __init__(self):
        
        self.text = ""
        self.display_text = ""
        self.display_text_count = 0

        

        
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