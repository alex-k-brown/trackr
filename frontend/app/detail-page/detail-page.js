'use strict';

angular.module('myApp.detail-page', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/detail-page/:goalId', {
            templateUrl: 'detail-page/detail-page.html',
            controller: 'DetailPageCtrl'
        });
    }])

    .controller('DetailPageCtrl', ["Restangular", "$scope", "$routeParams", function (Restangular, $scope, $routeParams) {
        var goalId = $routeParams.goalId;
        Restangular.one("goals", goalId).get().then(function (goal) {
            $scope.goal = goal
        });

        $scope.inactiveButtons = "partials/inactive-buttons.html";
        $scope.activeButtons = "partials/active-buttons.html";
        $scope.completeButtons = "partials/complete-buttons.html";
        $scope.detailBox = "partials/detail-box.html";
        $scope.activeStepsBox = "partials/active-steps-box.html";
        $scope.inactiveStepsBox = "partials/inactive-steps-box.html";
        $scope.completedStepsBox = "partials/completed-steps-box.html";
        $scope.mountainGraphic = "partials/mountain-graphic.html";


        $scope.stepAdd = function (goal, step) {

            var childGoal = {
                "goal": goal.id,
                "step": step,
                "timeFrame": $scope.timeFrame
            };

            Restangular.one("child-goals/").customPOST(childGoal).then(function (step) {
                goal.child_goals.push(step);
            });
            $scope.timeFrame = "";
            $scope.step = "";

            $scope.addStepEdit = false;

        };

        Restangular.all("time-frame/").customGET().then(function (timeFrames) {
            $scope.timeFrames = timeFrames;
        });

        $scope.stepDelete = function (childGoal) {
            if (confirm("Are you sure you want to delete this step?")) {
                Restangular.one("child-goals", childGoal.id).customDELETE().then(function () {
                    var index = $scope.goal.child_goals.indexOf(childGoal);
                    $scope.goal.child_goals.splice(index, 1);
                })
            }
        };


        $scope.statusChange = function (childGoal, status) {
            childGoal.status = status;

            Restangular.one("child-goals", childGoal.id).customPUT(childGoal).then(function (chGoal) {
                childGoal = chGoal;
            });
        };

        $scope.completeChange = function (childGoal, complete) {
            childGoal.complete = complete;

            Restangular.one("child-goals", childGoal.id).customPUT(childGoal).then(function (chGoal) {
                childGoal = chGoal;
            });

        };

        $scope.stepChange = function (keyEvent, childGoal) {

            if (keyEvent.which === 13) {

                Restangular.one("child-goals", childGoal.id).customPUT(childGoal).then(function (chGoal) {
                    childGoal = chGoal;
                });

                childGoal.editing = false;
            }
        };

        $scope.activeGoalsEmpty = function (goal) {
            if ($scope.hasOwnProperty('goal')) {
                return $scope.goal.child_goals.filter(returnStatus).length;
            }
        };

        var returnStatus = function (elem) {
            return elem.status && !elem.complete
        }

        $scope.inactiveGoalsEmpty = function (goal) {
            if ($scope.hasOwnProperty('goal')) {
                return $scope.goal.child_goals.filter(returnStatus2).length;
            }
        };

        var returnStatus2 = function (elem) {
            return elem.status
        }

        $scope.completeGoalsEmpty = function (goal) {
            if ($scope.hasOwnProperty('goal')) {
                return $scope.goal.child_goals.filter(returnStatus3).length;
            }
        };

        var returnStatus3 = function (elem) {
            return elem.complete
        }

    }]);
