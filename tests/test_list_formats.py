# Copyright © 2017 Collabora Ltd.
#
# This file is part of pfg.
#
# pfg is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# pfg is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for
# more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pfg. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#   Alexandros Frantzis <alexandros.frantzis@collabora.com>

import unittest
import pfg

class ListFormatsTest(unittest.TestCase):
    def test_lists_formats(self):
        for pfg_family in pfg.commands.families:
            family = pfg_family.__name__.replace("pfg.", "")
            formats = pfg.list_formats(family)
            self.assertGreater(len(formats), 0)
