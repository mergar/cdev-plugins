#!/usr/bin/env python3

import sqlite3
import argparse
import json

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_args():
    parser = argparse.ArgumentParser(description='convert virtual environment settings from SQL to JSON')
    parser.add_argument('--dbfile',  type=str, nargs='?', const=True, help='path to settings.sqlite')
    parser.add_argument('--sqlquery',  type=str, nargs='?', const=True, help='execute SQL query,e.g: "SELECT * FROM settings"')
    return parser.parse_args()

def sql2json(dbfile,sqlquery):
  connection = sqlite3.connect(dbfile)
  connection.row_factory = dict_factory

  cursor = connection.cursor()

  cursor.execute(sqlquery)
  # fetch all or one we'll go for all.
  results = cursor.fetchall()
  #print(results)
  print(json.dumps(results))
  connection.close()


def main(args):
  if(args.dbfile):
    sql2json(args.dbfile,args.sqlquery)

if __name__ == '__main__':
    main(get_args())
