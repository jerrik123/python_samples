# -*- coding: utf-8 -*-"
'''
# Description:
# @author: jerrikyang
'''
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def handle(count, name):
    print "count is: %d" % count
    print "name: %s" % name


handle()
