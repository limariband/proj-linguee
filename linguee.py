# linguee functions 

def search(arg):
    if 'exact_matches' in arg:
        for elem in arg['exact_matches']:

            if 'translations' in elem:
                for item in elem['translations']:

                    if 'examples' in item:
                        for sentence in item['examples']:

                            yield(sentence['source'],
                                sentence['target'])


def pronunc(arg):
    return arg['results'][0]['lexicalEntries'][0]['pronunciations'][0]['phoneticSpelling']
