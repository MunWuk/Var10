def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            var = item.get(args[0])
            if var is not None:
                yield var
        else:
            new_dic = {}
            all_none = True
            for key in args:
                var = item.get(key)
                if var is not None:
                    new_dic[key] = var
                    all_none = False
                if not all_none:
                    yield var
