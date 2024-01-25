from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
from colorama import init, Fore

init()



ascii_art = '''
         _,.---,---.._
     ,-';     `.      ''-.
   ,' -<        )         `.
  ;    |`.     '|     .     :
 ,     |  \     |      `._,' .
,'.    |        u      -'|  .',
; ;    U .           .   |  ; |
| ;    _____       _____ u  ; |
|  ',""     "" . ""     "".'  |
'. ~  ,-~~~^~, | ,~^~~~-,  ~ .'
 |   |._,-.'  }:{  `,-.  |   |
 |   l  `-'. / | \ ,`-'_,!   |
 .~  (__,|--" .^. "--|,__)  ~.
 |    ---+;' / . \ `;+--+    |
  \__.   U   \/^\/   |  |.__/
   V| \         |    u  | |V
    | |T"-..____U__..-"T| |
    | |`IIII_I_I_I_IIII'U |
    | |   (  ( U )  )   | |
    | |    `_ _ _ _'    | |
    |  \,III I I I III,/  |
     \   `~~~~,~~~~~'|   /
      `.   .  |    . | ,'
        `-._  |^   _.+'
            '"|^'"'  |        -tele: @y9_77
              u      |        -by Github: Expiq0
                     U
'''
COLOR_SUCCESS = Fore.GREEN
COLOR_ERROR = Fore.RED
COLOR_INFO = Fore.YELLOW
try:
    sleep_time = int(sys.argv[1])
except IndexError:
    print(COLOR_ERROR + "الرجاء تحديد السليب كوسيط عند تشغيل البرنامج من 10 الى 100.")
    print(COLOR_ERROR + "Please specify sleep as the parameter when running the program.")
    print(COLOR_INFO + 'python see_story.py from 10 to 100')
    sys.exit(1)
except ValueError:
    print(COLOR_ERROR + "السليب يجب أن يكون رقمًا صحيحًا من 10 الى 100.")
    print(COLOR_ERROR + "The sleep must be an integer.")
    print(COLOR_INFO + 'python see_story.py from 10 to 100')
    sys.exit(1)

# طباعة ASCII Art
print(COLOR_ERROR + ascii_art)

print(COLOR_SUCCESS + "start")

# قراءة اليوزرات من ملف النصي
with open("usernames.txt", "r") as file:
    usernames_to_deliver = file.read().splitlines()


def remove_username_from_file(username):
    with open("usernames.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.strip() != username:
                file.write(line)
        file.truncate()





options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "platformVersion": "13",  # put your platform version here
    "deviceName": "emulator-5554",  # put your device name here
    "autoGrantPermissions": True,
    "noReset": True,
    "fullReset": False,
    "disableIdLocatorAutocompletion": True,
})
# تكوين عنوان خادم Appium
appium_server_url = "http://127.0.0.1:4723/wd/hub"
# إنشاء مثيل لسائق Appium
driver = webdriver.Remote(appium_server_url, options=options)


# دالة للنقر
def click_element(driver, element_id, by_type=AppiumBy.ID):
    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((by_type, element_id))
    )
    element.click()


# دالة تقوم بكتابة اسم المستخدم في البحث
def type_username(driver, element_id, username):
    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((AppiumBy.ID, element_id))
    )
    element.clear()  # لتأكيد الحذف من النص السابق
    element.send_keys(username)


conn = 1


def send_like(driver):
    while True:
        try:
            element3 = WebDriverWait(driver, 7).until(
                EC.visibility_of_element_located(
                    (AppiumBy.ID, 'com.instagram.android:id/toolbar_like_button'))
            )
            element3.click()
            print(".")
            conn = + 1
            print(COLOR_SUCCESS + f" تم مشاهدة ستوري و اعطاء لايك : {str(conn)}.")
            print(COLOR_SUCCESS + f" My story was watched and a like was given: {str(conn)}.")
        except:
            print(".")

        try:
            element4 = WebDriverWait(driver, 7).until(
                EC.visibility_of_element_located(
                    (AppiumBy.ID, 'com.instagram.android:id/reel_viewer_progress_bar'))
            )
            element4.click()
            print('..')
        except:
            print('.')
            break


# دالة مشاهدة الستوري و تاكد اذا كان الستوري غير مشاهدة للمستخدم و تاكد اذا كان يحتوي على ستوري
def watch_story(driver, username):
    try:
        element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (AppiumBy.XPATH, f'//android.widget.ImageView[@content-desc="{username}\'s unseen story"]'))
        )
        element.click()



        send_like(driver)
    except:
        print(COLOR_ERROR + "لا يوجد ستوري غير مشاهد.")
        print(COLOR_ERROR + "There is no unwatched story.")


for username_text in usernames_to_deliver:
    # الضغط على زر البحث في واجهه الرئيسية
    click_element(driver, '//android.widget.FrameLayout[@content-desc="Search and explore"]/android.widget.ImageView',
                  by_type=AppiumBy.XPATH)

    # الضغط على زر البحث
    click_element(driver, 'com.instagram.android:id/action_bar_search_edit_text')

    # كتابة اسم المستخدم
    type_username(driver, 'com.instagram.android:id/action_bar_search_edit_text', username_text)

    # الضغط على الحساب المستخدم
    click_element(driver,
                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout",
                  AppiumBy.XPATH)

    # مشاهدة الستوري
    watch_story(driver, username_text)

    # حذف اسم المستخدم من ملف اسماء المستخدمين بعد الانتهاء من مشاهدة الستوري الخاص بيه
    remove_username_from_file(username_text)

    sleep(sleep_time)
print("DIN")
