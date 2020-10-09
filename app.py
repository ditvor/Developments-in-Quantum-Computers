from flask import Flask, render_template, url_for
from final_project import top_quantum_comp, url, dwave_df
from qubits_double_law import num_qubits


app = Flask(__name__)


post_info = f'{top_quantum_comp[0]} has created {top_quantum_comp[1]} quantum computer ' \
            f' with {top_quantum_comp[2]} qubits. \nThis is a top record right now.' \
            f'\nThis information was obtained from: {url}\n' \
            f'\nD-wave creates quantum annealer with noisy qubits ' \
            f'and doubles its amount every two year. \n' \
            f"Does it looks like the Moor's law? " \
            f'Check the table and the plot!'

posts = [
    {
        'author': 'He Who Must Not Be Named',
        'title': 'Qubits',
        'content': post_info,
        'date_posted': 'September 7, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, tables=[dwave_df.to_html(header="true")])


@ app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
