from dash import html, dcc
import dash_bootstrap_components as dbc

def serve_layout(fig_hist, fig_bar, fig_scatter, fig_box, fig_violin):
    layout = dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    html.H1("10 Academy Moodle Logs Dashboard", className="text-center my-4"),
                    width=12,
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(figure=fig_hist),
                        md=6
                    ),
                    dbc.Col(
                        dcc.Graph(figure=fig_bar),
                        md=6
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(figure=fig_scatter),
                        md=12
                    )
                ],
                className="my-4"
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(figure=fig_box),
                        md=6
                    ),
                    dbc.Col(
                        dcc.Graph(figure=fig_violin),
                        md=6
                    )
                ]
            )
        ],
        fluid=True,
    )
    return layout