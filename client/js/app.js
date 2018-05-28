var myApp = angular.module('myApp', [
    'ngResource',
    'ui.router'
]).config(function($httpProvider, $resourceProvider){
    $httpProvider.interceptors.push('LoadingInterceptor');
    $httpProvider.interceptors.push('AuthInterceptor');

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.withCredentials = true;
    $resourceProvider.defaults.stripTrailingSlashes = false;
});