from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import webbrowser

KV = '''
BoxLayout:
    orientation: "vertical"
    padding: 12
    spacing: 8

    canvas.before:
        Color:
            rgba: 0.95, 0.97, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "🤖 CareerPath AI"
        font_size: "24sp"
        bold: True
        color: 0.1, 0.2, 0.6, 1
        size_hint_y: None
        height: "50dp"

    Spinner:
        id: interest
        text: "Select Interest"
        values: ["Technology", "Design", "Business", "Medical", "Arts"]
        size_hint_y: None
        height: "38dp"

    Spinner:
        id: skill
        text: "Select Skill"
        values: ["Coding", "Creativity", "Communication", "Biology", "Writing"]
        size_hint_y: None
        height: "38dp"

    Spinner:
        id: education
        text: "Select Education"
        values: ["12th Pass", "Graduate", "Post Graduate"]
        size_hint_y: None
        height: "38dp"

    Button:
        text: "🎯 Get Suggestion"
        size_hint_y: None
        height: "40dp"
        background_color: 0.2, 0.6, 1, 1
        on_press: app.get_career()

    BoxLayout:
        size_hint_y: None
        height: "38dp"
        spacing: 6

        Button:
            text: "🔄 Reset"
            on_press: app.reset_all()

        Button:
            id: open_btn
            text: "🌐 Website"
            disabled: True
            on_press: app.open_site()

    ScrollView:
        bar_width: 8

        Label:
            id: result
            text: ""
            markup: True
            font_size: "19sp"
            color: 0.1, 0.1, 0.1, 1
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1] + 30

    BoxLayout:
        size_hint_y: None
        height: "42dp"
        spacing: 10
        padding: 5

        Button:
            text: "▶️"
            on_press: app.open_youtube()

        Button:
            text: "📸"
            on_press: app.open_instagram()

        Button:
            text: "📘"
            on_press: app.open_facebook()

        Button:
            text: "❌"
            background_color: 1, 0.3, 0.3, 1
            on_press: app.stop()
'''

# -------- LINKS --------
TECH_LINK = "https://sites.google.com/view/career-adda/technology-career"
DESIGN_LINK = "https://sites.google.com/view/career-adda/design-career"
BUSINESS_LINK = "https://sites.google.com/view/career-adda/business-career"
MEDICAL_LINK = "https://sites.google.com/view/career-adda/medical-career"
ARTS_LINK = "https://sites.google.com/view/career-adda/arts-career"

YOUTUBE = "https://youtube.com/@careerbyvaibhav"
INSTAGRAM = "https://www.instagram.com/careeraddaai"
FACEBOOK = "https://www.facebook.com/share/17kQ1rBd9d/"

current_link = ""


class CareerPathAI(App):

    def build(self):
        return Builder.load_string(KV)

    def get_career(self):
        global current_link

        i = self.root.ids.interest.text
        s = self.root.ids.skill.text
        e = self.root.ids.education.text

        if "Select" in (i, s, e):
            self.popup("⚠️ Error", "Please select all fields")
            return

        if i == "Technology" and s == "Coding":
            career = "Software Developer / AI Engineer"
            required = "Python, AI, Machine Learning"
            current_link = TECH_LINK

        elif i == "Design":
            career = "UI / UX Designer"
            required = "Figma, Design Principles"
            current_link = DESIGN_LINK

        elif i == "Business":
            career = "Marketing / Management"
            required = "Communication, Strategy"
            current_link = BUSINESS_LINK

        elif i == "Medical":
            career = "Nursing / Lab Technician"
            required = "Biology, Practical Training"
            current_link = MEDICAL_LINK

        else:
            career = "Content Writer / Journalist"
            required = "Writing, Research"
            current_link = ARTS_LINK

        self.root.ids.result.text = (
            f"🎯 [b]Career Suggestion[/b]\n{career}\n\n"
            f"🧠 [b]Required Skills[/b]\n{required}\n\n"
            f"🎓 [b]Education Level[/b]\n{e}"
        )

        self.root.ids.open_btn.disabled = False

    def reset_all(self):
        self.root.ids.interest.text = "Select Interest"
        self.root.ids.skill.text = "Select Skill"
        self.root.ids.education.text = "Select Education"
        self.root.ids.result.text = ""
        self.root.ids.open_btn.disabled = True

    def open_site(self):
        webbrowser.open(current_link)

    def popup(self, title, msg):
        Popup(
            title=title,
            content=Label(text=msg),
            size_hint=(0.7, 0.4)
        ).open()

    def open_youtube(self):
        webbrowser.open(YOUTUBE)

    def open_instagram(self):
        webbrowser.open(INSTAGRAM)

    def open_facebook(self):
        webbrowser.open(FACEBOOK)


if __name__ == "__main__":
    CareerPathAI().run()
