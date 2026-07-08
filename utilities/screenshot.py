from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver):
        current_time = datetime.now()

        file_name = f"Login_{current_time.strftime('%Y%m%d_%H%M%S')}.png"

        path = f"screenshot/{file_name}"

        driver.save_screenshot(path)

        return path