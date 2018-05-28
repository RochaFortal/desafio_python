myApp
    .service('LoginService', function($rootScope, $resource, $window, $location) {
        var self = this;
        var login = $resource("api/login/");

        self.login = function(params) {
            login.save(params).$promise.then(function(response) {
                console.log(response);
                $window.localStorage.token = response.token;
                $rootScope.user = response.user;
                $location.path('/home');
            }, function(err) {
                console.log(err);
                $location.path('/login');
            });
        };
    });