import reflex as rx


class State(rx.State):
    counter = 0

    def Increment_Count(self):
        self.counter += 1

    def Decrement_Count(self):
        self.counter -= 1


def index() -> rx.Component:
    return rx.flex(
            rx.text('Counter App', font_size=48),
            rx.text('Built Using ',
                    rx.link('Reflex', href='https://reflex.dev/'),
                    font_size=36
                    ),

            rx.flex(
                rx.button(
                    rx.icon('minus', size=36),
                    on_click=State.Decrement_Count,
                    ),
                rx.text(State.counter, font_size=32),
                rx.button(
                    rx.icon("plus", size=36),
                    on_click=State.Increment_Count,
                    ),
                spacing="4",
                align='center',
                justify='between',
                ),
                          rx.link('Made By dshaw0004', href='https://github.com/dshaw0004', font_size=24, color='grey'),
            height="100vh",
            align='center',
            justify='center',
            direction='column',
            spacing="9",
            )


app = rx.App()
app.add_page(index)

