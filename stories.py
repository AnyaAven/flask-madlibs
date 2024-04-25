"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, ...):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.get_result_text(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with words and template text."""

        self.title = title
        self.prompts = words
        self.template = text

    def __repr__(self):
        return f""" Story class prompts={self.prompts} template={self.template}"""

    def get_result_text(self, answers):
        """Return result text from dictionary of {prompt: answer, ...}."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started
silly_story = Story(
    "Silly Story",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, in a long-ago {place}, there lived an exceptionally
       {adjective} {noun}. It loved to {verb} with {plural_noun}."""
)

# Here's another --- you should be able to swap in app.py to use this story,
# and everything should still work

excited_story = Story(
    "Excited Story",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

scary_story = Story(
    "Scary Story",
    ["adjective1", "noun1", "verb1", "adjective2", "noun2"],
    """In the dark, {adjective1} forest, there lurked a terrifying {noun1}.
    It would {verb1} with its {adjective2} {noun2}, sending shivers down
    the spine of anyone who dared to venture near."""
)

campfire_story = Story(
    "Campfire Story",
    ["adjective1", "noun1", "verb1", "adjective2", "noun2"],
    """Gather 'round the campfire, children, and listen closely to the tale
    of the {adjective1} {noun1}. Legend has it that it would {verb1}
    with its {adjective2} {noun2} under the light of the moon."""
)

swimming_pool_story = Story(
    "Swimming Pool Story",
    ["adjective1", "noun1", "verb1", "adjective2", "noun2"],
    """As the sun set over the shimmering {noun1}, a mysterious {adjective1}
    figure emerged. It seemed to {verb1} with the grace of a {adjective2}
    {noun2}, captivating all who watched from the poolside."""
)

pets_story = Story(
    "Pets Story",
    ["adjective1", "noun1", "verb1", "adjective2", "noun2"],
    """In the cozy corner of the house, there lived a peculiar {adjective1}
    {noun1}. It would {verb1} with such {adjective2} {noun2}, bringing joy
    to all who knew its playful antics."""
)

story_list = [
    excited_story,
    scary_story,
    campfire_story,
    swimming_pool_story,
    pets_story,
    ]

stories = {story.title: story for story in story_list}
