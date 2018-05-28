myApp
    .service('CreateUserService', function($resource) {
        var self = this;
        var user = $resource('api/users/register/');


        self.save = function(params) {
            user.save(params).$promise.then(function(response) {
                console.log(response);
            })
        }
    });