angular.module('movieApp',[
    'ngRoute',
    'movieModule'
]).config(function($routeProvider){
    $routeProvider.when('/movie/:movieId',{
        templateUrl: 'http://127.0.0.1:8000/static/js/movie/partials/movie_details.html',
        controller: 'movieDetailsController'
    });
}).config(['$httpProvider', function($httpProvider){
    /**
     *  Need to add the following for routes to work
     *  with Django (CSRF workaroud for RESTFUL reequests)
     */
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);