from typing import Optional
from asgiref.sync import sync_to_async
from inspect import iscoroutinefunction
from strawberry.extensions import Extension
from pyinstrument import Profiler
from viztracer import VizTracer


class SyncToAsync(Extension):
    def resolve(self, _next, root, info, *args, **kwargs):
        field = info.parent_type.fields[info.field_name]
        resolver = field.resolve

        if not resolver._is_default and not iscoroutinefunction(resolver):
            return sync_to_async(_next)(root, info, *args, **kwargs)

        return _next(root, info, *args, **kwargs)


class PyInstrumentExtension(Extension):
    profiler: Optional[Profiler] = None

    def on_request_start(self):
        self.profiler = Profiler()
        self.profiler.start()

    def on_request_end(self):
        self.profiler.stop()

        output_html = self.profiler.output_html()
        with open("profiler.html", "w") as output_file:
            output_file.write(output_html)


class VizTracerExtension(Extension):
    profiler: Optional[Profiler] = None

    def on_request_start(self):
        self.profiler = VizTracer()
        self.profiler.start()

    def on_request_end(self):
        self.profiler.stop()
        self.profiler.save("report.html")