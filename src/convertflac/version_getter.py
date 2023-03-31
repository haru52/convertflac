import pkg_resources


class VersionGetter:
    @staticmethod
    def run():
        try:
            return pkg_resources.get_distribution('convertflac').version
        except pkg_resources.DistributionNotFound:
            return '0.1.0'
