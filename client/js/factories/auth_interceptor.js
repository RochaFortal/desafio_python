'use strict';

myApp
    .factory('AuthInterceptor', function($rootScope, $q, $window, $location) {
        return {
            request: function(config) {
                config.headers = config.headers || {};
                if($window.localStorage.token) {
                    config.headers.Authorization = 'Token ' + $window.localStorage.token;
                }
                return config;
            },
            response: function(response) {
                if(!$window.localStorage.token && $location.path() != '/register') {
                    $location.path('/login');
                }
                return response;
            },
            responseError: function(response) {
                if(response.status == 401) {
                    $window.localStorage.removeItem('token');
                    $location.path('/login');
                    return;
                }
                return $q.reject(response);
            }
        }
    });