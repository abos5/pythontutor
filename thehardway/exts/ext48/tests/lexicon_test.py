from nose.tools import assert_equal
from app import lexicon


def test_direction():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east'),
    ])


def test_verbs():
    assert_equal(lexicon.scan('go'), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [
        ('verb', 'go'),
        ('verb', 'kill'),
        ('verb', 'eat'),
    ])


def test_stops():
    assert_equal(lexicon.scan('the'), [('stop', 'the')])
    result = lexicon.scan('tHe in of')
    assert_equal(result, [
        ('stop', 'tHe'),
        ('stop', 'in'),
        ('stop', 'of'),
    ])


def nouns():
    assert_equal(lexicon.scan('bear'), [('noun', 'bear')])
    result = lexicon.scan('bear prINcess')
    assert_equal(result, [(
        ('noun', 'bear'),
        ('noun', 'prINcess'),
    )])


def numbers():
    assert_equal(lexicon.scan('1234'), [('number', 1234)])
    result = lexicon.scan('3 91234')
    assert_equal(result, [
        ('number', 3),
        ('number', 91234),
    ])


def test_errors():
    assert_equal(lexicon.scan('ASDFASDFASDF'), [('error', 'ASDFASDFASDF')])
    result = lexicon.scan('bear IAS prINCess')
    assert_equal(result, [
        ('noun', 'bear'),
        ('error', 'IAS'),
        ('noun', 'prINCess'),
    ])


#end of file
