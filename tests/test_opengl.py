from . import pfgtest

class OpenGLTest(pfgtest.TestCase):
    def test_non_packed_formats(self):
        self.assertFormatMatches(
            format_str = "GL_RGBA+GL_UNSIGNED_BYTE",
            native = None,
            memory_le = ["R" * 8, "G" * 8, "B" * 8, "A" * 8],
            memory_be = ["R" * 8, "G" * 8, "B" * 8, "A" * 8]);

    # TODO: Express the internal order of multibyte components
    def test_non_packed_formats_with_multibyte_components(self):
        self.assertFormatMatches(
            format_str = "GL_RGB+GL_UNSIGNED_SHORT",
            native = None,
            memory_le = ["R" * 8, "R" * 8, "G" * 8, "G" * 8, "B" * 8, "B" * 8],
            memory_be = ["R" * 8, "R" * 8, "G" * 8, "G" * 8, "B" * 8, "B" * 8])

    def test_packed_formats(self):
        self.assertFormatMatches(
            format_str = "GL_BGRA+GL_UNSIGNED_INT_10_10_10_2",
            native = "B" * 10 + "G" * 10 + "R" * 10 + "A" * 2,
            memory_le = ["R" * 6 + "A" * 2, "G" * 4 + "R" * 4, "B" * 2 + "G" * 6, "B" * 8],
            memory_be = ["B" * 8, "B" * 2 + "G" * 6, "G" * 4 + "R" * 4, "R" * 6 + "A" * 2])

        self.assertFormatMatches(
            format_str = "GL_RGBA+GL_UNSIGNED_INT_2_10_10_10_REV",
            native = "A" * 2 + "B" * 10 + "G" * 10 + "R" * 10,
            memory_le = ["R" * 8, "G" * 6 + "R" * 2, "B" * 4 + "G" * 4, "A" * 2 + "B" * 6],
            memory_be = ["A" * 2 + "B" * 6, "B" * 4 + "G" * 4, "G" * 6 + "R" * 2, "R" * 8])

    def test_single_component_formats(self):
        self.assertFormatMatches(
            format_str = "GL_RED+GL_UNSIGNED_BYTE",
            native = None,
            memory_le = ["R" * 8],
            memory_be = ["R" * 8])

        self.assertFormatMatches(
            format_str = "GL_GREEN+GL_UNSIGNED_BYTE",
            native = None,
            memory_le = ["G" * 8],
            memory_be = ["G" * 8])

        self.assertFormatMatches(
            format_str = "GL_BLUE+GL_UNSIGNED_BYTE",
            native = None,
            memory_le = ["B" * 8],
            memory_be = ["B" * 8])

    def test_integer_formats(self):
        self.assertFormatMatches(
            format_str = "GL_RG_INTEGER+GL_UNSIGNED_BYTE",
            native = None,
            memory_le = ["R" * 8, "G" * 8],
            memory_be = ["R" * 8, "G" * 8])

    def test_documentation(self):
        self.assertHasDocumentationFor("opengl")