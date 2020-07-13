class ScreenUtil:
    @staticmethod
    def get_positioned_text(text, x, x_offset, y, y_offset):
        X, Y = ScreenUtil.__calculate_text_coordinates_with_offset(x, x_offset, y, y_offset)

        text_rect = text.get_rect()
        text_rect.center = (X // 2, Y // 2)

        return text_rect

    @staticmethod
    def __calculate_text_coordinates_with_offset(x, x_offset, y, y_offset):
        return x - x_offset, y + y_offset
