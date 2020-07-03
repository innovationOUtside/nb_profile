import click
from .nb_visualiser import nb_vis_parse_nb

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--out', '-o', default='nb_quality_review.png',  help='Image outfile')
@click.option('--gap', '-g', default=0, type=int, help='Gap')
@click.option('--linewidth', '-l', default=5, type=int, help='Line width')
def review(path, out, gap, linewidth):
	click.echo('Using directory: {}'.format(path))
	#nb_vis_parse_nb('../Documents/GitHub/tm351-undercertainty/notebooks/tm351/Part 02 Notebooks',
    #        linewidth=10, gap=0, img_file='test-nbvis.png')
	nb_vis_parse_nb(path, img_file=out,  linewidth = linewidth, w=20, gap=gap, gap_boost=1, gap_colour='lightgrey')
