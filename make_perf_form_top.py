#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
import csv

if __name__ == "__main__":
        argvs = sys.argv
        argc = len(argvs)
        if (argc != 2):
                print "\nUsage: %s [FILENAME]\n" % argvs[0]
                sys.exit()

        ############################
        # make dict data from file
        ############################
        f = open(sys.argv[1], "rt")

        rows = [{}]
        nrow = 0

        for f_line in f:
                f_line_sp = f_line.split()

                # skip
                if 0 == len(f_line_sp):
                        continue
                # search "top" for [time]
                elif "top" in f_line_sp and 0 == f_line_sp.index("top"):
                        nrow += 1
                        rows.append({})
                        rows[nrow]["time"] = f_line_sp[2]
                # search "trae*" for [CPU]
                elif 11 < len(f_line_sp) and "trae" in f_line_sp[11]:
                        if 12 < len(f_line_sp):
                                rows[nrow][f_line_sp[11] + f_line_sp[12]] = f_line_sp[8]
                        else:
                                rows[nrow][f_line_sp[11]] = f_line_sp[8]
                else:
                        if 11 < len(f_line_sp) and "ntservice" in f_line_sp[11]:
                                rows[nrow]["ntservice"] = f_line_sp[8]
                        else:
                                rows[nrow]["others"] = f_line_sp[8]
        f.close()

        ##################
        # make header(rows[0].val) from rows[1].key
        ##################
        for key,val in rows[1].items():
                rows[0][key] = key

        ##################
        # create csv file
        ##################
        fieldnames = rows[0].keys()
        f = open("top.csv", "wb")
        dw = csv.DictWriter(f, delimiter=",", fieldnames=fieldnames)
        dw.writerows(rows)
        f.close()

