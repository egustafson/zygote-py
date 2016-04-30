##
##
## ############################################################
import click

from time import sleep


@click.command()
def run():
    print('zygote daemon stub.')
    while True:
        sleep(1)
        
