var movieControllers = angular.module('movieControllers',[]);

/**
 *  Now identify the API call for Movie Details
 */
movieControllers.controllers('MovieDetailController',['$scope','$routeParams','$http',
    function($scope,$routeParams,$http){
        $http.get('http://127.0.0.1:8000/movie/api/movie/'+routeParams.movieId+'/?format=json')
            .success(function(data){
                //  DATA is passed back to here from the API
                //  where something can be done with it
                $scope.movie = data;
            });
    }
])