var movieApp = angular.module('movieApp',['ngRoute','movieControllers']);

movieApp.config(['routeProvider',
    function($routeProvider){
        $routeProvider.
        when('/movie/:movideId',{
            templateUrl: 'http://127.0.0.1:8000/static/js/movie/partials/movide_details.html',
            controller: 'movieController'
        });

    }
]);

/**
 *  Need to add the following for routes to work
 *  with Django (CSRF workaroud for RESTFUL reequests)
 */
movieApp.config([
'$httpProvider', function($httpProvider){
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);