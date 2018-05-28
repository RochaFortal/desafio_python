myApp
    .controller('CreateUserController', function(CreateUserService) {
        var self = this;
        self.user = null;

        self.save = function() {
            CreateUserService.save(self.user);
        };
    });