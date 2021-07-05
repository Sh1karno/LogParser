IP_ADDRESS_REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

METHODS_REGEX = r"(POST|GET|PUT|DELETE|HEAD)"

DURATION_REQUEST_REGEX = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.{26}\] \"(POST|GET|PUT|DELETE|HEAD)" \
                         r" \/[\w\d\/\.\-\_\:\;\+\!\?]+ HTTP/1.1\" \d{3} (\d+)"

CLIENT_ERROR_REGEX = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.{26}\] \"(POST|GET|PUT|DELETE|HEAD)" \
                     r" (\/[\w\d\/\.\-\_\:\;\+\!\?]+) HTTP/1.1\" (4\d{2}) "

SERVER_ERROR_REGEX = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.{26}\] \"(POST|GET|PUT|DELETE|HEAD)" \
                     r" (\/[\w\d\/\.\-\_\:\;\+\!\?]+) HTTP/1.1\" (5\d{2}) "
