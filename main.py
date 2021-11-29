from linkml_runtime.utils.schemaview import SchemaView

if __name__ == '__main__':
    view = SchemaView("https://raw.githubusercontent.com/biolink/biolink-model/latest/biolink-model.yaml")
    for c in view.class_descendants('entity'):
        for p in view.class_parents(c, mixins=False):
            print("\t".join([c, "biolink:is_a", p]))
