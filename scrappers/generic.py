import requests


class Scrapper:
    """
    Allows to download and debug a html sample or an specific url source.

    To run the script:
        manage.py runscript path/to/script --script-args arg1 arg2
    """

    # url of the source
    url = None

    # getting info from the sample (useful for testing and debugging)
    use_sample = True
    html_sample = "sample.html"

    @classmethod
    def get_source(cls, *args, **kwargs):
        if cls.use_sample:
            # getting html from the sample
            with open(cls.html_sample, "r") as file:
                return "".join(file.readlines())

        # getting the html from the webpage
        response = requests.get(cls.get_url(*args, **kwargs))
        if response.status_code == 404:
            raise Exception("Page does not exists [Error: 404]")
        return response.text

    @classmethod
    def get_url(cls, *args, **kwargs):
        return cls.url

    @classmethod
    def create_local_sample(cls, *args, **kwargs):
        response = requests.get(cls.get_url(*args, **kwargs))
        with open(cls.html_sample, "w") as file:
            file.writelines(response.text)

    @classmethod
    def create_model(cls, *args, **kwargs):
        raise NotImplemented()
