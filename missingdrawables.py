# -*- coding: utf-8 -*-

import sys
import os


BUCKETS = ('l', 'm', 'h', 'xh', 'xxh')


class COLORS:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    END = '\033[0m'

    @staticmethod
    def colorize(message, color):
        return color + message + COLORS.END


class DrawableFinder(object):
    def __init__(self, res_path):
        self.res_path = res_path

    def find_drawables(self):
        self.drawables = {}  # map bucket name to set of files

        for bucket in BUCKETS:
            bucket_dir = os.path.join(res_path, 'drawable-%sdpi' % bucket)
            if os.path.exists(bucket_dir):
                self.drawables[bucket] = set(os.listdir(bucket_dir))

        self.buckets = [
            bucket for bucket in BUCKETS if bucket in self.drawables]

    def get_bucket_row(self, name):
        flags = [name in self.drawables[bucket] for bucket in self.buckets]
        return (
            all(flags),
            '|'.join('  %s  ' % ('+' if flag else '-') for flag in flags)
        )

    def get_title_row(self, left_padding):
        headers = '|'.join('  ' + bucket.ljust(3) for bucket in self.buckets)
        return ' ' * left_padding + headers

    def print_table(self):
        self.find_drawables()

        all_set = set()
        all_set.update(*self.drawables.values())
        all = sorted(list(all_set))

        longest = max(len(s) for s in all)

        print self.get_title_row(longest + 3)

        for drawable in all:
            complete, row = self.get_bucket_row(drawable)
            color = COLORS.OKGREEN if complete else COLORS.FAIL
            name = COLORS.colorize(drawable.rjust(longest), color)

            print ' %s |%s|' % (name, row)


if __name__ == '__main__':
    res_path = 'res'
    if len(sys.argv) > 1:
        res_path = sys.argv[1]

    DrawableFinder(res_path).print_table()
