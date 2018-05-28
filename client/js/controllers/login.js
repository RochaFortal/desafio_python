myApp
    .controller('LoginCtrl', function(LoginService) {
        var self = this;
        self.user = null;

        self.login = function() {
           LoginService.login(self.user); 
        };
    });