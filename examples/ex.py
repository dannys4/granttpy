# %%
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import grantt

grantt.set_default_markersize(80)
grantt.set_default_linewidth(10)
grantt.set_luminance_threshold(0.8)

neg15day = timedelta(days=-15)
pos15day = timedelta(days=15)
pos20day = timedelta(days=20)
L = 'left'
C = 'center'
R = 'right'
red = "#C00000"
green = "#4EA72E"
blue = "#0070C0"
orange = "#E97132"
gray = "#4D4D4D"

fontsize = 10
local_lw = fontsize + 1  # Increase this with font size to ensure Periods cover text

# %%

milestone_data = [
    grantt.Span(
        text='Milestones',
        start=datetime(2025, 1, 1),
        end=datetime(2028, 1, 1),
        color='k',
        level_increment=0.75),

    grantt.Event(
        text='MS1',
        date=datetime(2026, 1, 1),
        color='k',
        level_increment=0,
        offset=neg15day,
        textalignment=L),

    grantt.Event(
        text='MS2',
        date=datetime(2026, 5, 1),
        color='k',
        level_increment=0,
        offset=neg15day,
        textalignment=L),

    grantt.Event(
        text='MS3',
        date=datetime(2026, 7, 1),
        color='k',
        offset=pos15day,
        textalignment=R),

    grantt.Event(
        text='MS6',
        date=datetime(2027, 3, 1),
        color='k',
        level_increment=0,
        offset=neg15day,
        textalignment=L),

    grantt.Event(
        text='MS8',
        date=datetime(2027, 5, 1),
        color='k',
        level_increment=0,
        offset=pos15day,
        textalignment=R),

    grantt.Event(
        text='MS9',
        date=datetime(2027, 9, 1),
        color='k',
        offset=pos15day,
        textalignment=R),

    grantt.Event(
        text='MS4',
        date=datetime(2026, 7, 1),
        color='k',
        level_increment=0,
        offset=neg15day,
        textalignment=L),

    grantt.Event(
        date=datetime(2026, 9, 1),
        text='MS5',
        color='k',
        level_increment=0,
        offset=pos15day,
        textalignment=R),

    grantt.Event(
        date=datetime(2027, 4, 1),
        text='MS7',
        color='k',
        level_increment=0.75,
        offset=pos15day,
        textalignment=R),
]

wp1_data = [
    grantt.Span(
        text="WP1: Lorem Ipsum",
        start=datetime(2025, 1, 1),
        end=datetime(2028, 1, 1),
        color=red,
        level_increment=0.75),

    grantt.Period(
        text="Task 1: Dolor Sit Amet",
        start=datetime(2025, 1, 1),
        end=datetime(2026, 7, 1),
        color=red,
        textalignment=R,
        offset=pos20day,
        lw=local_lw),

    grantt.Period(
        text="Task 2: consectetur adipiscing elit",
        start=datetime(2025, 7, 1),
        end=datetime(2026, 8, 1),
        color=red,
        textalignment=R,
        offset=pos20day,
        lw=local_lw),

    grantt.Period(
        text="Task 3: sed do eiusmod tempor",
        start=datetime(2025, 4, 1),
        end=datetime(2026, 9, 1),
        color=red,
        textalignment=R,
        offset=pos20day,
        lw=local_lw),

    grantt.Period(
        text="Task 4: incididunt ut labore",
        start=datetime(2025, 7, 1),
        end=datetime(2028, 1, 1),
        color=red,
        textalignment=C,
        lw=local_lw),

    grantt.Period(
        text="Task 5: et dolore magna aliqua",
        start=datetime(2025, 4, 1),
        end=datetime(2026, 4, 1),
        color=red,
        textalignment=R,
        offset=pos20day,
        lw=local_lw),

    grantt.Event(
        text='D1.1',
        date=datetime(2026, 3, 1),
        color=red,
        level_increment=0,
        offset=neg15day,
        textalignment=L,
        marker='.'),

    grantt.Event(
        text='D1.2',
        date=datetime(2026, 7, 1),
        color=red,
        level_increment=0,
        offset=neg15day,
        textalignment=L,
        marker='.'),

    grantt.Event(
        text='D1.3',
        date=datetime(2026, 8, 1),
        color=red,
        level_increment=0,
        textalignment=C,
        marker='.'),

    grantt.Event(
        text='D1.4',
        date=datetime(2026, 9, 1),
        color=red,
        level_increment=0,
        textalignment=R,
        offset=pos15day,
        marker='.'),

    grantt.Event(
        text='D1.5',
        date=datetime(2027, 9, 1),
        color=red,
        level_increment=0.75,
        textalignment=R,
        offset=neg15day,
        marker='.'),
]

wp2_data = [
    grantt.Span(
        text="WP2: Ut enim ad minim veniam",
        start=datetime(2025, 1, 1),
        end=datetime(2028, 1, 1),
        color=green,
        level_increment=0.75),

    grantt.Period(
        text="Task 1: quis nostrud exercitation",
        start=datetime(2025, 1, 1),
        end=datetime(2026, 1, 1),
        color=green,
        textalignment=R,
        offset=pos20day,
        lw=local_lw),

    grantt.Period(
        text="Task 2: ullamco laboris nisi",
        start=datetime(2026, 1, 1),
        end=datetime(2027, 1, 1),
        color=green,
        textalignment=C,
        offset=timedelta(days=0),
        lw=local_lw),

    grantt.Period(
        text="Task 3: ut aliquip ex ea",
        start=datetime(2025, 7, 1),
        end=datetime(2027, 7, 1),
        color=green,
        textalignment=C,
        offset=timedelta(days=0),
        lw=local_lw),

    grantt.Period(
        text="Task 4: commodo consequat",
        start=datetime(2026, 1, 1),
        end=datetime(2028, 1, 1),
        color=green,
        textalignment=C,
        offset=timedelta(days=0),
        lw=local_lw),

    grantt.Event(
        text="D2.1",
        date=datetime(2026, 1, 1),
        color=green,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D2.2",
        date=datetime(2027, 1, 1),
        color=green,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D2.3",
        date=datetime(2027, 1, 1),
        color=green,
        textalignment=R,
        offset=timedelta(days=15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D2.4",
        date=datetime(2027, 7, 1),
        color=green,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D2.5",
        date=datetime(2027, 11, 1),
        color=green,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D2.6",
        date=datetime(2027, 11, 1),
        color=green,
        textalignment=R,
        offset=timedelta(days=15),
        marker=".",
        level_increment=0.75),
]

wp3_data = [
    grantt.Span(
        text="WP3: Duis aute irure",
        start=datetime(2025, 1, 1),
        end=datetime(2028, 1, 1),
        color=blue,
        level_increment=0.75),

    grantt.Period(
        text="Task 1: dolor in reprehenderit",
        start=datetime(2025, 1, 1),
        end=datetime(2026, 1, 1),
        color=blue,
        textalignment=R,
        offset=pos20day,
        lw=local_lw),

    grantt.Period(
        text="Task 2: in voluptate velit",
        start=datetime(2025, 10, 1),
        end=datetime(2026, 4, 1),
        color=blue,
        textalignment=R,
        offset=pos20day,
        lw=local_lw),

    grantt.Period(
        text="Task 3: esse cillum dolore",
        start=datetime(2026, 1, 1),
        end=datetime(2028, 1, 1),
        color=blue,
        textalignment=L,
        textcolor='k',
        offset=timedelta(days=-20),
        lw=local_lw),

    grantt.Period(
        text="Task 4: eu fugiat nulla pariatur",
        start=datetime(2026, 7, 1),
        end=datetime(2028, 1, 1),
        color=blue,
        textalignment=L,
        textcolor='k',
        offset=timedelta(days=-20),
        lw=local_lw),

    grantt.Event(
        text="D3.1",
        date=datetime(2026, 1, 1),
        color=blue,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D3.2",
        date=datetime(2027, 4, 1),
        color=blue,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D3.3",
        date=datetime(2027, 11, 1),
        color=blue,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0.75),
]

wp4_data = [
    grantt.Span(
        text="WP4: Excepteur sint",
        start=datetime(2025, 1, 1),
        end=datetime(2028, 1, 1),
        color=orange,
        level_increment=0.75),

    grantt.Period(
        text="Task 1: occaecat cupidatat",
        start=datetime(2025, 4, 1),
        end=datetime(2027, 4, 1),
        color=orange,
        textalignment=R,
        offset=pos20day,
        lw=local_lw),

    grantt.Period(
        text="Task 2: non proident",
        start=datetime(2025, 7, 1),
        end=datetime(2027, 7, 1),
        color=orange,
        textalignment=C,
        offset=timedelta(days=0),
        lw=local_lw),

    grantt.Period(
        text="Task 3: sunt in culpa",
        start=datetime(2025, 1, 1),
        end=datetime(2028, 1, 1),
        color=orange,
        textalignment=C,
        offset=timedelta(days=0),
        lw=local_lw),

    grantt.Event(
        text="D4.1",
        date=datetime(2027, 4, 1),
        color=orange,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D4.2",
        date=datetime(2027, 7, 1),
        color=orange,
        textalignment=R,
        offset=timedelta(days=15),
        marker=".",
        level_increment=0.75),
]

wp5_data = [
    grantt.Span(
        text="WP5: qui officia deserunt",
        start=datetime(2025, 1, 1),
        end=datetime(2028, 1, 1),
        color=gray,
        level_increment=0.75),

    grantt.Period(
        text="Task 1: mollit anim",
        start=datetime(2025, 1, 1),
        end=datetime(2028, 1, 1),
        color=gray,
        lw=local_lw),

    grantt.Period(
        text="Task 2: id est",
        start=datetime(2025, 1, 1),
        end=datetime(2028, 1, 1),
        color=gray,
        lw=local_lw),

    grantt.Period(
        text="Task 3: laborum",
        start=datetime(2025, 7, 1),
        end=datetime(2028, 1, 1),
        color=gray,
        textalignment=C,
        offset=timedelta(days=0),
        lw=local_lw),

    grantt.Period(
        text="Task 4: Lorem ipsum",
        start=datetime(2025, 10, 1),
        end=datetime(2028, 1, 1),
        color=gray,
        textalignment=C,
        offset=timedelta(days=0),
        lw=local_lw),

    grantt.Event(
        text="D5.1",
        date=datetime(2025, 5, 1),
        color=gray,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D5.2",
        date=datetime(2025, 6, 1),
        color=gray,
        textalignment=C,
        offset=timedelta(days=0),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D5.3",
        date=datetime(2025, 7, 1),
        color=gray,
        textalignment=R,
        offset=timedelta(days=15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D5.4",
        date=datetime(2026, 1, 1),
        color=gray,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0),

    grantt.Event(
        text="D5.5",
        date=datetime(2027, 7, 1),
        color=gray,
        textalignment=L,
        offset=timedelta(days=-15),
        marker=".",
        level_increment=0)
]

data = milestone_data + wp1_data + wp2_data + wp3_data + wp4_data + wp5_data

# %%

fig, ax = grantt.chart(data, (12, 10), fontsize=fontsize)

# Only label each full year
ticklabels = ["Start", "", "", "", "Year 1", "", "", "",
              "Year 2", "", "", "", "Year 3"]
ax.set_xticklabels(ticklabels)

# Add line increments
ylim = ax.get_ylim()
ax.grid(which='major', axis='x', linestyle='--', color="#ddd")
plt.show()
