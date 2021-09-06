import http from 'k6/http';
import { sleep } from 'k6';


def load_test():
  http.get('https://test.k6.io')
  sleep(1)
